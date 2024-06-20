from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from rest_framework import status
from home.serializers import PeopleSerializer

@api_view(['GET','POST'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'names' : ['django','flask','Tornado','fastapi'],
        'course_provider' : 'scaler'
    }
    if request.method == 'GET':
        print('Get request hit')
    elif request.method == "POST":
        data = request.data
        print('****')
        print(data)
        print('****')
        print('Post request hit')
    return Response(courses)

@api_view(['GET','POST'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)

