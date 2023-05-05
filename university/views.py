from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import University
from .serializers import UniversitySerializer
from .forms import UniversityForm


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


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.using("university_db").all()
    serializer_class = UniversitySerializer

   