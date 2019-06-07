from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from api.models import Contact
from api.serializers import ContactSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class ContactsView(APIView):
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, contact_id):
        contact = Contact.objects.get(Contact, id=contact_id)
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id):
        contact = Contact.objects.get(id=contact_id)
        contact.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class Login(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_active': user.is_active
        })


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)