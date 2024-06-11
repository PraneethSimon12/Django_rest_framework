from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'names' : ['django','flask','Tornado','fastapi'],
        'course_provider' : 'scaler'
    }
    return Response(courses)