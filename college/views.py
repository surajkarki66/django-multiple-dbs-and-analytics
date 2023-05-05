from django.shortcuts import render, redirect

from .models import College
from .forms import CollegeForm


def college(request):
    college = College.objects.all()
    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CollegeForm()

    context = {
        'college': college,
        'form': form,
    }
    return render(request, "college/college.html", context)