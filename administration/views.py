from django.shortcuts import render

def dashboard(request):
    """
    Renders the main dashboard for the administration app.
    """
    context = {
        'total_apartments': 200,
        'occupied_apartments': 185,
        'rent_paid_count': 160,
        'rent_outstanding_count': 25,
        'active_riders_count': 84,
        'needs_attention_tenants': [
            {'initials': '4B', 'name': 'John Doe', 'overdue_days': 5},
            {'initials': '12C', 'name': 'Jane Smith', 'overdue_days': 3},
            {'initials': '8A', 'name': 'Robert Paulson', 'overdue_days': 2},
        ]
    }
    return render(request, 'administration/dashboard.html', context)
