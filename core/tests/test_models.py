from django.test import TestCase
from core.models import Physician


class PhysicianTest(TestCase):
    """Test module for Physician Model."""

    def test_create_new_physician(self):
        physician = {
            'name_given': 'Doctor',
            'name_family': 'House',
            'title': 'Dr',
            'clinic': 'Mayo Clinic'
        }
        created_physician = Physician.objects.create(**physician)

        self.assertTrue(isinstance(created_physician, Physician))
        self.assertEqual(created_physician.name_given, physician['name_given'])
        self.assertEqual(created_physician.name_family, physician['name_family'])
        self.assertEqual(created_physician.title, physician['title'])
        self.assertEqual(created_physician.clinic, physician['clinic'])
        self.assertEqual(str(created_physician), f"{physician['name_given']} {physician['name_family']}")
