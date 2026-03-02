"""
Earnings service layer.
All business logic for earnings data lives here.
Views only orchestrate — they never contain business logic.
"""


def get_rider_earnings_context():
    """Return mock rider earnings data for the dashboard."""
    return {
        'daily_earnings': '$450.00',
        'daily_change': '+8%',
        'weekly_earnings': '$2,840.00',
        'weekly_change': '+5.4%',
        'monthly_earnings': '$11,200.00',
        'top_riders': [
            {'name': 'Alex Rivera', 'initials': 'AR', 'total_rides': 342, 'total_earnings': '$4,250.00'},
            {'name': 'Marcus Chen', 'initials': 'MC', 'total_rides': 318, 'total_earnings': '$3,910.50'},
            {'name': 'Sarah Jenkins', 'initials': 'SJ', 'total_rides': 295, 'total_earnings': '$3,620.00'},
        ],
        'all_riders': [
            {'name': 'Alex Rivera', 'initials': 'AR', 'total_rides': 342, 'total_earnings': '$4,250.00'},
            {'name': 'Marcus Chen', 'initials': 'MC', 'total_rides': 318, 'total_earnings': '$3,910.50'},
            {'name': 'Sarah Jenkins', 'initials': 'SJ', 'total_rides': 295, 'total_earnings': '$3,620.00'},
        ],
    }


def get_tenant_earnings_context():
    """Return mock tenant earnings data for the dashboard."""
    return {
        'total_rent_paid': '$85,400.00',
        'rent_vs_last_month': 'vs. last month',
        'paid_tenants': 142,
        'paid_tenants_total': 150,
        'pending_payments': 8,
        'pending_estimated': '$9,600.00',
        'recent_billing': [
            {
                'name': 'Apt 402 - Skyline Tower',
                'paid_on': 'Oct 12, 2025',
                'amount': '$1,450.00',
            },
            {
                'name': 'Apt 115 - Garden Suites',
                'paid_on': 'Oct 10, 2025',
                'amount': '$980.00',
            },
            {
                'name': 'Unit 30C - Metro Lofts',
                'paid_on': 'Sep 29, 2025',
                'amount': '$2,100.00',
            },
        ],
    }
