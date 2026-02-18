from django.shortcuts import render

def riders(request):
    """
    Renders the Rider Profiles page with hardcoded data.
    """
    riders_data = [
        {
            'name': 'Alex Johnson',
            'rides': '1,240',
            'earned': '$3,450.00',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'Sedan',
            'avatar': 'https://i.pravatar.cc/150?u=alex',
            'rating': 4.9, # Kept in data but won't be displayed
            'reviews': 240
        },
        {
            'name': 'Sarah Connor',
            'rides': '980',
            'earned': '$2,100.50',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'Motorbike',
            'avatar': 'https://i.pravatar.cc/150?u=sarah',
            'rating': 4.8,
            'reviews': 180
        },
        {
            'name': 'Michael Chen',
            'rides': '450',
            'earned': '$1,200.00',
            'status': 'Pending Docs',
            'status_class': 'warning',
            'vehicle': 'Scooter',
            'avatar': 'https://i.pravatar.cc/150?u=michael',
            'rating': 4.7,
            'reviews': 95
        },
        {
            'name': 'David Smith',
            'rides': '2,100',
            'earned': '$5,600.00',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'Van',
            'avatar': 'https://i.pravatar.cc/150?u=david',
            'rating': 5.0,
            'reviews': 520
        },
        {
            'name': 'Emma Wilson',
            'rides': '150',
            'earned': '$450.00',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'E-Bike',
            'avatar': 'https://i.pravatar.cc/150?u=emma',
            'rating': 4.6,
            'reviews': 89
        },
        {
            'name': 'James Rodriguez',
            'rides': '3,400',
            'earned': '$8,900.00',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'SUV',
            'avatar': 'https://i.pravatar.cc/150?u=james',
            'rating': 4.9,
            'reviews': 890
        },
        {
            'name': 'Lisa Chang',
            'rides': '890',
            'earned': '$2,300.00',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'Moped',
            'avatar': 'https://i.pravatar.cc/150?u=lisa',
            'rating': 4.8,
            'reviews': 210
        },
        {
            'name': 'Robert Taylor',
            'rides': '1,670',
            'earned': '$4,100.00',
            'status': 'Verified',
            'status_class': 'success',
            'vehicle': 'Luxury',
            'avatar': 'https://i.pravatar.cc/150?u=robert',
            'rating': 4.9,
            'reviews': 412
        },
    ]
    
    context = {
        'riders': riders_data
    }
    return render(request, 'users/riders.html', context)
