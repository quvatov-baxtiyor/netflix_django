from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Actor, Movie
from .serializers import ActorSerializer, MovieSerializer


# class ResAPIView(APIView):
#     def get(self,request,format=None):
#         return Response(data={'message':'Hello Netflix!'})
#
#     def post(self,request,format=None):
#         return Response(data={'message':f"Hello {request.data['name']}"})

class ActorAPIView(APIView):
    def get(self,request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors,many=True)
        return Response(data=serializer.data)

class MovieAPIView(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(data=serializer.data)