from django.test import TestCase
from tracking.models import Consignment

class ConsignmentModelTest(TestCase):
    def setUp(self):
        self.consignment = Consignment.objects.create(
            tracking_number="TEST123456",
            booked_on="2023-05-01T12:00:00Z",
            category="Standard",
            destination="Test Destination",
            tariff=10.50,
            source_country="Test Country",
            status="In Transit",
            delivered_to="",
            delivered_at="",
            sender_name="Test Sender",
            sender_email="sender@test.com",
            sender_address="Test Sender Address",
            sender_mobile="1234567890",
            receiver_name="Test Receiver",
            receiver_address="Test Receiver Address",
            receiver_mobile="0987654321",
            receiver_email="receiver@test.com",
            content_of_shipment="Test Content"
        )
def test_consignment_str_method(self):
    self.assertEqual(str(self.consignment), "TEST123456")
    
def test_consignment_str_method_empty_tracking_number(self):
        consignment = Consignment.objects.create(
            tracking_number="",
            booked_on="2023-05-01T12:00:00Z",
            category="Standard",
            destination="Test Destination",
            tariff=10.50,
            source_country="Test Country",
            status="In Transit",
            delivered_to="",
            delivered_at="",
            sender_name="Test Sender",
            sender_email="sender@test.com",
            sender_address="Test Sender Address",
            sender_mobile="1234567890",
            receiver_name="Test Receiver",
            receiver_address="Test Receiver Address",
            receiver_mobile="0987654321",
            receiver_email="receiver@test.com",
            content_of_shipment="Test Content"
        )
        self.assertEqual(str(consignment), "")

def test_consignment_str_method_multiple_calls(self):
    consignment = Consignment.objects.create(
        tracking_number="MULTI123",
        booked_on="2023-05-01T12:00:00Z",
        category="Standard",
        destination="Test Destination",
        tariff=10.50,
        source_country="Test Country",
        status="In Transit",
        delivered_to="",
        delivered_at="",
        sender_name="Test Sender",
        sender_email="sender@test.com",
        sender_address="Test Sender Address",
        sender_mobile="1234567890",
        receiver_name="Test Receiver",
        receiver_address="Test Receiver Address",
        receiver_mobile="0987654321",
        receiver_email="receiver@test.com",
        content_of_shipment="Test Content"
    )
    first_call = str(consignment)
    second_call = str(consignment)
    third_call = str(consignment)
    self.assertEqual(first_call, second_call)
    self.assertEqual(second_call, third_call)
    self.assertEqual(first_call, "MULTI123")

def test_consignment_str_method_does_not_modify_tracking_number(self):
    original_tracking_number = "ORIG123"
    consignment = Consignment.objects.create(
        tracking_number=original_tracking_number,
        booked_on="2023-05-01T12:00:00Z",
        category="Standard",
        destination="Test Destination",
        tariff=10.50,
        source_country="Test Country",
        status="In Transit",
        delivered_to="",
        delivered_at="",
        sender_name="Test Sender",
        sender_email="sender@test.com",
        sender_address="Test Sender Address",
        sender_mobile="1234567890",
        receiver_name="Test Receiver",
        receiver_address="Test Receiver Address",
        receiver_mobile="0987654321",
        receiver_email="receiver@test.com",
        content_of_shipment="Test Content"
    )
    str_result = str(consignment)
    self.assertEqual(str_result, original_tracking_number)
    self.assertEqual(consignment.tracking_number, original_tracking_number)