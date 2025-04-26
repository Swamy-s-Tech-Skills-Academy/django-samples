from django.shortcuts import render

# Create your views here.


def challenges_index_view(request):
    """
    View function for the challenges app's index page.
    This renders the challenges-specific index.html template from the challenges app.
    """
    # Monthly challenges dictionary
    monthly_challenges = {
        'january': 'Run 20 minutes every day!',
        'february': 'Walk for at least 30 minutes daily!',
        'march': 'Learn Django for 20 minutes daily!',
        'april': 'Eat a vegetable with every meal!',
        'may': 'Read 20 pages daily!',
        'june': 'Practice meditation for 10 minutes daily!',
        'july': 'Drink 8 glasses of water daily!',
        'august': 'Write in a journal every day!',
        'september': 'Complete 30 minutes of coding practice!',
        'october': 'Learn a new word daily!',
        'november': 'Practice gratitude journaling!',
        'december': 'Connect with a friend or family member daily!'
    }

    return render(request, 'challenges/index.html', {
        'challenges': monthly_challenges
    })
