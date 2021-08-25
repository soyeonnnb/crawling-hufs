from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from hupstudy import settings
from accounts.forms import UserRegistrationForm, LoginForm, VerificationEmailForm
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import CreateView, FormView
from .mixins import VerifyEmailMixin


class UserRegistrationView(VerifyEmailMixin, CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/'
    verify_url = '/accounts/verify/'
    email_template_name = 'accounts/email/registration_verification.html'
    token_generator = default_token_generator

    def form_valid(self, form):
        response = super().form_valid(form)
        if form.instance:
            self.send_verification_email(form.instance)
        return response

    def build_verification_link(self, user, token):
        return '{}/accounts/{}/verify/{}/'.format(self.request.META.get('HTTP_ORIGIN'), user.pk, token)

    def send_verification_email(self, user):
        token = self.token_generator.make_token(user)
        url = self.build_verification_link(user, token)
        subject = '회원가입을 축하드립니다.'
        message = '다음 주소로 이동하셔서 인증하세요. {}'.format(url)
        html_message = render(self.request, self.email_template_name, {'url': url}).content.decode('utf-8')
        user.email_user(subject, message, settings.EMAIL_HOST_USER, html_message=html_message)
        messages.info(self.request, '회원가입을 축하드립니다. 가입하신 이메일주소로 인증메일을 발송했으니 확인 후 인증해주세요.')

class UserVerificationView(TemplateView):
    model = get_user_model()
    redirect_url = '/accounts/login/'
    token_generator = default_token_generator

    def get(self, request, *args, **kwargs):
        if self.is_valid_token(**kwargs):
            messages.info(request, '인증이 완료되었습니다.')
        else:
            messages.error(request, '인증이 실패되었습니다.')
        return HttpResponseRedirect(self.redirect_url)   # 인증 성공여부와 상관없이 무조건 로그인 페이지로 이동

    def is_valid_token(self, **kwargs):
        pk = kwargs.get('pk')
        token = kwargs.get('token')
        user = self.model.objects.get(pk=pk)
        is_valid = self.token_generator.check_token(user, token)
        if is_valid:
            user.is_active = True
            user.save()     # 데이터가 변경되면 반드시 save() 메소드 호출
        return is_valid

class ResendVerifyEmailView(FormView):
    model = get_user_model()
    form_class = VerificationEmailForm
    success_url = '/accounts/login/'
    template_name = 'accounts/resend_verify_email.html'
    email_template_name = 'accounts/email/registration_verification.html'
    token_generator = default_token_generator

    def send_verification_email(self, user):
        token = self.token_generator.make_token(user)
        url = self.build_verification_link(user, token)
        subject = '회원가입을 축하드립니다.'
        message = '다음 주소로 이동하셔서 인증하세요. {}'.format(url)
        html_message = render(self.request, self.email_template_name, {'url': url}).content.decode('utf-8')
        user.email_user(subject, message, from_email=settings.EMAIL_HOST_USER, html_message=html_message)
        messages.info(self.request, '회원가입을 축하드립니다. 가입하신 이메일주소로 인증메일을 발송했으니 확인 후 인증해주세요.')
    
    def build_verification_link(self, user, token):
        return '{}/accounts/{}/verify/{}/'.format(self.request.META.get('HTTP_ORIGIN'), user.pk, token)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            messages.error(self.request, '알 수 없는 사용자 입니다.')
        else:
            self.send_verification_email(user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login_form.html'
    success_url = '/'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)