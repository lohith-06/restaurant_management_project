from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Contact

class ContactFormTests(TestCase):
    def test_contact_form_submission_creates_record(self):
        """Submitting the form should create a new Contact entry"""
        response = self.client.post(reverse("contact"), {
            "name": "John Doe",
            "email": "john@example.com"
        })

        # Check redirect or success response
        self.assertEqual(response.status_code, 302)  # assuming redirect after submit

        # Verify record saved
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "john@example.com")

    def test_empty_form_does_not_create_record(self):
        """Empty submission should not create a record"""
        response = self.client.post(reverse("contact"), {})
        self.assertEqual(response.status_code, 200)  # stays on same page
        self.assertEqual(Contact.objects.count(), 0)