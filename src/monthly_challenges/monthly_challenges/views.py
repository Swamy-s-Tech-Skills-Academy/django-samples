from django.shortcuts import render

def index_view(request):
    """
    View function for the main landing page of the project.
    This renders the main index.html template from the project-level templates.
    """
    return render(request, 'index.html')