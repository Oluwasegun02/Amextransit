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
                'status': consignment.status,
                'source_country': consignment.source_country,
                'destination': consignment.destination,
                'tariff': consignment.tariff,
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
