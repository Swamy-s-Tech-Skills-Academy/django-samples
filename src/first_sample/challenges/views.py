from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    """
    View function for the home page.
    """
    return HttpResponse("<h1>Welcome to Django Samples</h1><p>A collection of Django examples and best practices.</p><p><a href='/challenges'>View Challenges</a></p>")

def challenges_view(request):
    """
    View function for the challenges landing page.
    """
    return HttpResponse("<h1>Challenges</h1><p>This is the landing page for Django challenges.</p><p><a href='/'>Back to Home</a></p>")
