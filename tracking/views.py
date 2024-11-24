from django.shortcuts import render, redirect
from .models import Consignment
from .forms import dashboardIn

# Create your views here.
def homepage(request):
    # consignments = Consignment.objects.all()
    return render(request, 'tracking/home.html')

def aboutpage(request):
    return render(request, 'tracking/about.html')

def contactpage(request):
    return render(request, 'tracking/contact.html')

def tracking_page(request):
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            consignment = Consignment.objects.get(tracking_number=tracking_number)
            tracking_data = {
                'tracking_number': consignment.tracking_number,
                'bookedOn': consignment.booked_on,
                'category': consignment.category,
                'destination': consignment.destination,
                'tariff': consignment.tariff,
                'source_country': consignment.source_country,
                # Add delivery details
                'status': consignment.status,
                'delivered': consignment.delivered_to,
                'delivered_to_date': consignment.delivered_on,
                # Add Sender details
                'senderName': consignment.sender_name,
                'senderEmail': consignment.sender_email,
                'senderAddress': consignment.sender_address,
                'senderPhone': consignment.sender_mobile,
                # Add receiver details
                'receiverName': consignment.receiver_name,
                'receiverEmail': consignment.receiver_email,
                'receiverAddress': consignment.receiver_address,
                'receiverPhone': consignment.receiver_mobile,

                'goods': consignment.content_of_shipment,
            }
        except  Consignment.DoesNotExist:
            tracking_data = {'error': 'Tracking number not found'}
        return render(request, 'tracking/tracking_page.html', {'tracking_data': tracking_data})
    tracking_data = {'error': 'Tracking number not found'}
    return render(request, 'tracking/tracking_page.html', {'tracking_data': tracking_data})


def dashboard_page(request):
    consignments = Consignment.objects.all()  # Fetch all consignments (you can filter as needed)
    if request.method == 'POST':
        form = dashboardIn(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('homepage')
    else:
        form = dashboardIn()
    return render(request, 'tracking/dashboard_page.html', {'consignments': consignments, 'form': form})
