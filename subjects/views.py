from django.shortcuts import render
from django.views.generic import View
from . import models
from . import forms


class SearchView(View):
    def get(self, request):
        track = request.GET.get("track")
        if track:
            form = forms.SubjectSearchForm(request.GET)
            if form.is_valid():
                year = form.cleaned_data.get("year")
                track = form.cleaned_data.get("track")
                subjects = form.cleaned_data.get("subjects")
                filter_args = {}
                filter_args["year__lte"] = year
                filter_args["track"] = track
                for subject in subjects:
                    filter_args["subjects"] = subject
                results = models.Subject.objects.filter(**filter_args).order_by("year")

                return render(
                    request,
                    "subjects/home.html",
                    {"form": form, "results": results},
                )
        else:
            form = forms.SubjectSearchForm()
        return render(
            request,
            "subjects/home.html",
            {"form": form},
        )
