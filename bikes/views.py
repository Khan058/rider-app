from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404

from .forms import BikeForm
from .services import get_all_bikes, create_bike, get_bike_by_id, update_bike


def _get_available_riders():
    """Helper to fetch active riders for dropdowns."""
    from users.models import Custom_user
    return Custom_user.objects.filter(user_type='RIDER', is_active=True)


def bikes_list(request):
    """
    Renders the Bikes listing page with search and pagination.
    """
    search_query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)

    bikes_queryset = get_all_bikes(search_query)

    paginator = Paginator(bikes_queryset, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'bikes': page_obj,
        'search_query': search_query,
    }
    return render(request, 'bikes/bikes_page.html', context)


def register_bike(request):
    """
    Handles bike registration.
    View only orchestrates — validation is in forms, creation is in services.
    """
    available_riders = _get_available_riders()

    if request.method == 'POST':
        form = BikeForm(request.POST)
        bike, error = create_bike(form)

        if bike:
            messages.success(request, f"Bike '{bike.registration}' registered successfully!")
            return redirect('bikes_list')

        messages.error(request, error)
        return render(request, 'bikes/bike_registration.html', {
            'available_riders': available_riders,
            'form': form
        })

    form = BikeForm()
    return render(request, 'bikes/bike_registration.html', {
        'available_riders': available_riders,
        'form': form
    })


def edit_bike(request, bike_id):
    """
    Handles editing an existing bike.
    View only orchestrates — validation is in forms, update is in services.
    """
    bike = get_bike_by_id(bike_id)
    if not bike:
        raise Http404("Bike not found.")

    available_riders = _get_available_riders()

    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        bike_obj, error = update_bike(form)

        if bike_obj:
            messages.success(request, f"Bike '{bike_obj.registration}' updated successfully!")
            return redirect('bikes_list')

        messages.error(request, error)
        return render(request, 'bikes/bike_edit.html', {
            'bike': bike,
            'available_riders': available_riders,
            'form': form,
        })

    form = BikeForm(instance=bike)
    return render(request, 'bikes/bike_edit.html', {
        'bike': bike,
        'available_riders': available_riders,
        'form': form,
    })
