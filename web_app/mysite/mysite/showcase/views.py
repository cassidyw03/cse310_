from django.shortcuts import render
# from .models import Project

# Create your views here.

def portfolio_view(request):
    # projects = Project.objects.all()  # Get all projects from the database
    # return render(request, 'portfolio.html', {'projects': projects})
    return render(request, 'portfolio.html')


