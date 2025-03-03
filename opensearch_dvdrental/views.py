from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework import status

from search.models import Actor, Film
from search.serializers import ActorSerializer, FilmSerializer


class ActorSearchViewSet(ViewSet):
    @action(detail=False, methods=['get'])
    def search(self, request):
        actor_search = request.query_params.get("q", "")

        if not actor_search:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        actors = Actor.objects.filter(Q(first_name__icontains = actor_search) | Q(last_name__icontains = actor_search))
        actor_data = ActorSerializer(actors, many=True).data

        return Response({
            "actors":actor_data,
        })


class FilmsSearchViewSet(ViewSet):
    @action(detail=False, methods=['get'])
    def search(self, request):
        film_search = request.query_params.get("q", "")

        if not film_search:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        films = Film.objects.filter(Q(title__icontains = film_search))
        film_data = FilmSerializer(films, many=True).data
        
        return Response({
            "films": film_data
        })