from hashlib import sha256
import requests
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.decorators import authentication_classes

from . import serializers


class ImportPhysicianApiView(APIView):
    # permission_classes = [AllowAny]
    serializer_class = serializers.PhysicianSerializer
    # authentication_classes = (TokenAuthentication, SessionAuthentication, )

    def post(self, request):
        """
        Connects to the Noteworth Challenge Api to retrieve a list of physician. Manage the
        authorization to the API.
        """

        host = 'http://127.0.0.1:5000'
        auth_endpoint = '/auth'
        providers_endpoint = '/providers'
        TRIES = 2

        if settings.SECURE_TOKEN is None:
            # authenticate
            for i in range(TRIES):
                print(f'trying auth {i} time{"s" if i>1 else ""}')
                try:
                    response = requests.get(f'{host}{auth_endpoint}', verify=False, timeout=5)
                except requests.exceptions.Timeout:
                    continue
                if response.status_code == 200:
                    break
            else:
                return Response(
                    {'message': 'Service unavailable'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )
            settings.SECURE_TOKEN = response.headers['Super-Secure-Token']

        # read provider endpoint for importing physician list
        message = ''.join([settings.SECURE_TOKEN, providers_endpoint]).encode('utf-8')
        checksum = sha256(message)
        headers = {'X-Request-Checksum': checksum.hexdigest()}
        for i in range(TRIES):
            print(f'trying providers {i} time{"s" if i>1 else ""}')
            try:
                response = requests.get(f'{host}/{providers_endpoint}',
                                        headers=headers, verify=False, timeout=5)
            except requests.exceptions.Timeout:
                continue
            if response.status_code == status.HTTP_200_OK:
                break
        else:
            return Response(
                {'message': 'Providers Service unavailable'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        # serializes physician data and save it on db
        providers = response.json()['providers']
        for physician_data in providers:
            serializer = self.serializer_class(data=physician_data)
            if serializer.is_valid():
                serializer.save()
        return Response({'message': 'Physicians imported'})
