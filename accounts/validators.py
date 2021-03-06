from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class RegisteredEmailValidator:
    user_model = get_user_model()
    code = 'invalid'

    def __call__(self, email): #필드의 유효성 검증 필터는 __call__을 반드시 오버라이딩 해줘야 함
        try:
            user = self.user_model.objects.get(email=email)
        except self.user_model.DoesNotExist:
            raise ValidationError('가입되지 않은 이메일입니다.', code=self.code)
        else:
            if user.is_active:
                raise ValidationError('이미 인증되어 있습니다.', code=self.code)
        return