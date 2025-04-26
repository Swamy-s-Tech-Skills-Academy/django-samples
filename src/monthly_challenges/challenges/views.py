from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
    View function for the home page that renders the index.html template.
    """
    return render(request, 'index.html')
