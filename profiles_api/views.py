from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

# Create your views here.
class HelloWorldAPI(APIView):
    """Test API view"""
    
    serializer_class = serializer.HelloWorldSerializer
    
    def get(self,request,format=None):
        """Returns an APIView of the function"""
        an_apiview = [
            "Shabuddin Pre-Cadet School",
            "Chilld Laboratory School",
            "Adarsha School Narayonganj",
            "Govt. Tolaram College",
            "Patuakhali Science and Technology University",
        ]
        return Response({'message':'HelloWorld','an_apiview':an_apiview})
    def post(self,request):
        """Create a api call with a given name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            #return Response({'message':"Hey you fool"})
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})