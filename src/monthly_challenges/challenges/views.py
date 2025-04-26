from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
    View function for the home page that renders the index.html template.
    This is being deprecated in favor of the index_view in the main project folder.
    """
    return render(request, 'index.html')

def challenges_index_view(request):
    """
    View function for the challenges app's index page.
    This renders the challenges-specific index.html template from the challenges app.
    """
    return render(request, 'challenges/index.html')
