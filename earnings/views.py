from django.shortcuts import render
from .services import get_rider_earnings_context, get_tenant_earnings_context


def earnings_overview(request):
    """Earnings overview page — orchestrates service calls only."""
    context = {}
    context.update(get_rider_earnings_context())
    context.update(get_tenant_earnings_context())
    return render(request, 'earnings/earnings.html', context)
