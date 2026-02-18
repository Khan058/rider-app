"""
Service layer for user-related business logic.
Views must only orchestrate — all creation and validation logic lives here.
"""
import logging
from .models import Custom_user

logger = logging.getLogger(__name__)


def create_rider(form):
    """
    Creates a new rider from validated form data.
    Returns a tuple of (user, error_message).
    - On success: (user, None)
    - On failure: (None, error_string)
    """
    if not form.is_valid():
        # Collect all validation errors into a single readable string
        errors = "; ".join(
            f"{field}: {', '.join(msgs)}"
            for field, msgs in form.errors.items()
        )
        logger.warning("Rider registration validation failed: %s", errors)
        return None, errors

    data = form.cleaned_data
    user = Custom_user.objects.create_user(
        username=data['email'],  # Use email as username
        password='DefaultPassword123!',
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        phone=data['phone'],
        address=data['address'],
        picture=data.get('picture'),
        license_number=data.get('license_number', ''),
        license_expiry_date=data.get('license_expiry_date'),
        license_image=data.get('license_image'),
        ejari_number=data.get('ejari_number', ''),
        ejari_expiry_date=data.get('ejari_expiry_date'),
        ejari_image=data.get('ejari_image'),
    )

    logger.info("Rider registered successfully: %s", user.email)
    return user, None


def get_all_riders(search_query=None, sort_option=None):
    """
    Fetches all riders (Custom_user) with search and sorting.
    Annotates mock metrics (rides, earnings) since Ride app is not yet implemented.
    """
    from django.db.models import Q, Value, IntegerField, DecimalField
    
    # Base queryset - active users excluding superusers/staff if needed, 
    # but for now let's just get all Custom_users who are not superusers
    queryset = Custom_user.objects.filter(is_superuser=False).annotate(
        rides_count=Value(0, output_field=IntegerField()),
        total_earnings=Value(0.00, output_field=DecimalField(max_digits=10, decimal_places=2)),
        avg_rating=Value(5.0, output_field=DecimalField(max_digits=3, decimal_places=1)) # Mock rating
    )

    # Search
    if search_query:
        queryset = queryset.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(license_number__icontains=search_query)
        )

    # Sorting
    if sort_option == 'highest_rides':
        queryset = queryset.order_by('-rides_count', '-date_joined')
    elif sort_option == 'lowest_rides':
        queryset = queryset.order_by('rides_count', '-date_joined')
    else:
        # Default sort
        queryset = queryset.order_by('-date_joined')

    return queryset
