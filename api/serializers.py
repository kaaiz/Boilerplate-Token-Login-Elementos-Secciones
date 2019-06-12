from rest_framework import serializers
from .models import Contact, User, Seccion, Elemento


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        # what fields to include?
        fields = ('first_name', 'last_name', 'phone_number', 'email')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # what fields to include?
        fields = ('id', 'first_name', 'last_name', 'username',
                  'is_staff', 'is_active', 'email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data('username'),
            email=validated_data('email'),
            first_name=validated_data('first_name'),
            last_name=validated_data('last_name'),
            is_staff=validated_data('is_staff'),
        )

        user.set_password(validated_data('password'))
        user.save()

        return user


class SeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seccion
        # what fields to include?
        fields = ('titulo', 'id_elemento')


class ElementoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elemento
        # what fields to include?
        fields = ('titulo', 'descripcion', 'imagen', 'fecha')
