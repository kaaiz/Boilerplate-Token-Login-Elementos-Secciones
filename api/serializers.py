from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        # what fields to include?
        fields = ('first_name', 'last_name', 'phone_number', 'email')
