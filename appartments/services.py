"""
Service layer for apartment-related business logic.
Views must only orchestrate — all creation and query logic lives here.
"""
import logging
from .models import Apartment

logger = logging.getLogger(__name__)


def create_apartment(form):
    """
    Creates a new apartment from validated form data.
    Returns a tuple of (apartment, error_message).
    """
    if not form.is_valid():
        errors = "; ".join(
            f"{field}: {', '.join(msgs)}"
            for field, msgs in form.errors.items()
        )
        logger.warning("Apartment registration validation failed: %s", errors)
        return None, errors

    apartment = form.save()
    logger.info("Apartment registered successfully: %s", apartment)
    return apartment, None


def update_apartment(form):
    """
    Updates an existing apartment from validated form data.
    Returns a tuple of (apartment, error_message).
    """
    if not form.is_valid():
        errors = "; ".join(
            f"{field}: {', '.join(msgs)}"
            for field, msgs in form.errors.items()
        )
        logger.warning("Apartment update validation failed: %s", errors)
        return None, errors

    apartment = form.save()
    logger.info("Apartment updated successfully: %s", apartment)
    return apartment, None


def get_apartment_by_id(apartment_id):
    """
    Fetches a single apartment by ID.
    Returns the apartment instance or None.
    """
    try:
        return Apartment.objects.select_related('tenant').get(pk=apartment_id)
    except Apartment.DoesNotExist:
        logger.warning("Apartment not found: %s", apartment_id)
        return None


def get_all_apartments(search_query=None, status_filter=None):
    """
    Fetches all apartments with optional search and status filtering.
    Uses select_related for tenant to avoid N+1 queries.
    """
    from django.db.models import Q

    queryset = Apartment.objects.select_related('tenant').all()

    if status_filter:
        queryset = queryset.filter(status=status_filter)

    if search_query:
        queryset = queryset.filter(
            Q(unit_number__icontains=search_query) |
            Q(building_name__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(tenant__first_name__icontains=search_query) |
            Q(tenant__last_name__icontains=search_query)
        )

    return queryset.order_by('-created_at')
