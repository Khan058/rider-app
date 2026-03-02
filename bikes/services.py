"""
Service layer for bike-related business logic.
Views must only orchestrate — all creation, update, and query logic lives here.
"""
import logging
from .models import Bike

logger = logging.getLogger(__name__)


def create_bike(form):
    """
    Creates a new bike from validated form data.
    Returns a tuple of (bike, error_message).
    """
    if not form.is_valid():
        errors = "; ".join(
            f"{field}: {', '.join(msgs)}"
            for field, msgs in form.errors.items()
        )
        logger.warning("Bike registration validation failed: %s", errors)
        return None, errors

    bike = form.save()
    logger.info("Bike registered successfully: %s", bike)
    return bike, None


def update_bike(form):
    """
    Updates an existing bike from validated form data.
    Returns a tuple of (bike, error_message).
    """
    if not form.is_valid():
        errors = "; ".join(
            f"{field}: {', '.join(msgs)}"
            for field, msgs in form.errors.items()
        )
        logger.warning("Bike update validation failed: %s", errors)
        return None, errors

    bike = form.save()
    logger.info("Bike updated successfully: %s", bike)
    return bike, None


def get_bike_by_id(bike_id):
    """
    Fetches a single bike by ID.
    Returns the bike instance or None.
    """
    try:
        return Bike.objects.select_related('rider').get(pk=bike_id)
    except Bike.DoesNotExist:
        logger.warning("Bike not found: %s", bike_id)
        return None


def get_all_bikes(search_query=None):
    """
    Fetches all bikes with optional search filtering by model, registration, or rider name.
    Uses select_related for rider to avoid N+1 queries.
    """
    from django.db.models import Q

    queryset = Bike.objects.select_related('rider').all()

    if search_query:
        queryset = queryset.filter(
            Q(model__icontains=search_query) |
            Q(registration__icontains=search_query) |
            Q(rider__first_name__icontains=search_query) |
            Q(rider__last_name__icontains=search_query)
        )

    return queryset.order_by('-created_at')
