from django.shortcuts import render

def riders(request):
    """
    Renders the Rider Profiles page with real database data, search, and pagination.
    """
    from django.core.paginator import Paginator
    from .services import get_all_riders

    search_query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', '')
    page_number = request.GET.get('page', 1)

    # Fetch data via service
    riders_queryset = get_all_riders(search_query, sort_option)

    # Pagination (10 per page)
    paginator = Paginator(riders_queryset, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'riders': page_obj,
        'search_query': search_query,
        'sort_option': sort_option,
    }
    return render(request, 'users/riders.html', context)

def register_rider(request):
    """
    Handles the 4-step rider registration process.
    View only orchestrates — validation is in forms, creation is in services.
    """
    from django.contrib import messages
    from django.shortcuts import redirect
    from .forms import RiderRegistrationForm
    from .services import create_rider

    if request.method == 'POST':
        form = RiderRegistrationForm(request.POST, request.FILES)
        user, error = create_rider(form)

        if user:
            messages.success(request, f"Rider '{user.full_name()}' registered successfully!")
            return redirect('riders')

        messages.error(request, error)
        return render(request, 'users/rider_registration.html')

    return render(request, 'users/rider_registration.html')
