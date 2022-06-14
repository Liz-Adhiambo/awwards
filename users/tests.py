from django.test import TestCase
from django.test import TestCase

from .models import   Profile
# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        self.prof = Profile(name="Liz")
        self.prof.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_method(self):
        self.prof.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.prof.save_profile()
        self.prof.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def test_update(self):
        profile = Profile.get_profile_id(self.prof.id)
        profile.update_profile('liz')
        profile = Profile.get_profile_id(self.prof.id)
        self.assertTrue(profile.username == 'liz')
 
 
 
# Create your tests here.
