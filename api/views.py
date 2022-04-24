from fileinput import filename
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Resto
from .serializers import restoSerializer
from utils import get_db_handle

# Create your views here.
db, client = (get_db_handle())
collection = db['restoman']


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/resto/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of scripts'
        },
        {
            'Endpoint': '/resto/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single script object'
        },
        {
            'Endpoint': '/resto/create/',
            'method': 'POST',
            'body': {'body': {}},
            'description': 'Creates new script with data sent in post request'
        },
        {
            'Endpoint': '/resto/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing script with data sent in post request'
        },
        {
            'Endpoint': '/file/upload/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a script'
        },
        {
            'Endpoint': '/resto/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting script'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getRest(request):
    probs = Resto.objects.all().order_by('-updated')
    serializer = restoSerializer(probs, many=True)

    return Response(serializer.data)
