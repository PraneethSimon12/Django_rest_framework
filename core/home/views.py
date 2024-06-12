from rest_framework.decorators import api_view
from rest_framework.response import Response

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