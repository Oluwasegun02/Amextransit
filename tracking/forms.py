from django import forms
from .models import Consignment

class dashboardIn(forms.ModelForm):
    booked_on = forms.DateTimeField()
    tariff = forms.DecimalField(max_digits=10, decimal_places=2)
    sender_email = forms.EmailField()
    receiver_email = forms.EmailField()
    class Meta:
        model = Consignment
        fields = ['tracking_number', 'booked_on', 'category', 'destination', 'tariff', 'source_country','status','delivered_to', 'delivered_on','delivered_at', 'sender_name','sender_email','sender_address','sender_mobile','receiver_name','receiver_address','receiver_mobile','receiver_email','content_of_shipment']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

