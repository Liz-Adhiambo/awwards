from rest_framework import serializers
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'id_user','bio','profileimg', 'date_joined','location')