from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from processor.processors.user import User


class UserRegisterViewSet(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            User('register').start(request.data)
        except Exception as e:
            pass
        else:
            resp = {
                'message': "Your account has been registered."
            }
            status_code = status.HTTP_201_CREATED
        return Response(resp, status=status_code)
        
