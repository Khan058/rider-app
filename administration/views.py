from django.shortcuts import render

def dashboard(request):
    """
    Renders the main dashboard for the administration app.
    """
    context = {
        # Add context data here later
    }
    return render(request, 'administration/dashboard.html', context)
