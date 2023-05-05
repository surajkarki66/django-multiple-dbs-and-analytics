from django.shortcuts import render, redirect

from .models import Organization
from .forms import OrganizationForm

# Create your views here.
def organization(request):
    organization = Organization.objects.using("organization_db").all() # manually selecting database
  
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/organization")
    else:
        form = OrganizationForm()

    context = {
        'organization': organization,
        'form': form,
    }
    return render(request, "organization/organization.html", context)