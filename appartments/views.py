from django.shortcuts import render


def tenants(request):
    """
    Renders the Tenant Profiles page with database data, search, and pagination.
    """
    from django.core.paginator import Paginator
    from users.services import get_all_riders

    search_query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', '')
    page_number = request.GET.get('page', 1)

    tenants_queryset = get_all_riders(search_query, sort_option, user_type='TENANT')

    paginator = Paginator(tenants_queryset, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'tenants': page_obj,
        'search_query': search_query,
        'sort_option': sort_option,
    }
    return render(request, 'appartments/tenants.html', context)


def register_tenant(request):
    """
    Handles the 2-step tenant registration process.
    View only orchestrates — validation is in forms, creation is in services.
    """
    from django.contrib import messages
    from django.shortcuts import redirect
    from users.forms import UserRegistrationForm
    from users.services import create_user

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        user, error = create_user(form)

        if user:
            messages.success(request, f"Tenant '{user.full_name()}' registered successfully!")
            return redirect('tenants')

        messages.error(request, error)
        return render(request, 'appartments/tenant_registration.html')

    return render(request, 'appartments/tenant_registration.html')


def apartments(request):
    """
    Renders the Apartments listing page with search, filtering, and pagination.
    """
    from django.core.paginator import Paginator
    from .services import get_all_apartments

    search_query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    page_number = request.GET.get('page', 1)

    apartments_queryset = get_all_apartments(search_query, status_filter or None)

    paginator = Paginator(apartments_queryset, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'apartments': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    return render(request, 'appartments/apartments.html', context)


def _get_available_tenants():
    """Helper to fetch active tenants for dropdowns."""
    from users.models import Custom_user
    return Custom_user.objects.filter(user_type='TENANT', is_active=True)


def register_apartment(request):
    """
    Handles apartment registration.
    View only orchestrates — validation is in forms, creation is in services.
    """
    from django.contrib import messages
    from django.shortcuts import redirect
    from .forms import ApartmentForm
    from .services import create_apartment

    available_tenants = _get_available_tenants()

    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES)
        apartment, error = create_apartment(form)

        if apartment:
            messages.success(request, f"Apartment '{apartment}' registered successfully!")
            return redirect('apartments')

        messages.error(request, error)
        return render(request, 'appartments/apartment_registration.html', {
            'available_tenants': available_tenants,
        })

    return render(request, 'appartments/apartment_registration.html', {
        'available_tenants': available_tenants,
    })


def edit_apartment(request, apartment_id):
    """
    Handles editing an existing apartment.
    View only orchestrates — validation is in forms, update is in services.
    """
    from django.contrib import messages
    from django.shortcuts import redirect
    from django.http import Http404
    from .forms import ApartmentForm
    from .services import get_apartment_by_id, update_apartment

    apartment = get_apartment_by_id(apartment_id)
    if not apartment:
        raise Http404("Apartment not found.")



    if request.method == 'POST':
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        apartment_obj, error = update_apartment(form)

        if apartment_obj:
            messages.success(request, f"Apartment '{apartment_obj}' updated successfully!")
            return redirect('apartments')

        messages.error(request, error)
        return render(request, 'appartments/apartment_edit.html', {
            'apartment': apartment,
            'form': form,
        })

    form = ApartmentForm(instance=apartment)
    return render(request, 'appartments/apartment_edit.html', {
        'apartment': apartment,
        'form': form,
    })
