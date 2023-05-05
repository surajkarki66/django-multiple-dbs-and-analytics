from django.shortcuts import render, redirect

from .models import University
from .forms import UniversityForm

# Create your views here.
def university(request):
    university = University.objects.using("university_db").all()
  
    if request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/university")
    else:
        form = UniversityForm()

    context = {
        'university': university,
        'form': form,
    }
    return render(request, "university/university.html", context)