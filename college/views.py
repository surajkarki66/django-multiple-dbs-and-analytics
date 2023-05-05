from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import College, Faculty
from .forms import CollegeForm
from .serializers import CollegeSerializer, FacultySerializer

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


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.using("college_db").all()
    serializer_class = CollegeSerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.using("college_db").all()
    serializer_class = FacultySerializer
