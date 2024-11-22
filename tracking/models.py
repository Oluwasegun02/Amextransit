from django.db import models

class Consignment(models.Model):
    tracking_number = models.CharField(max_length=20, unique=True)
    booked_on = models.DateTimeField()
    category = models.CharField(max_length=50)
    destination = models.CharField(max_length=100)
    # Add other fields:
    tariff = models.DecimalField(max_digits=10, decimal_places=2)
    source_country = models.CharField(max_length=50)
    # Add delivery details (status, delivered_to, delivered_on, delivered_at)
    status = models.CharField(max_length=20)
    delivered_to = models.CharField(max_length=100)
    delivered_on = models.DateTimeField(null=True, blank=True)
    delivered_at = models.CharField(max_length=100)
    # Add sender details
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    sender_address = models.TextField()
    sender_mobile = models.CharField(max_length=20)
    # Add receiver details
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.TextField()
    receiver_mobile = models.CharField(max_length=20)
    receiver_email = models.EmailField()
    # Add content of shipment list (if applicable)
    content_of_shipment = models.TextField()

    def __str__(self):
        return self.tracking_number
