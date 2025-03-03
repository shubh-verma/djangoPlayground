from django.urls import path
from search.views import ActorSearchViewSet, FilmsSearchViewSet

urlpatterns = [
    path(r'actor', ActorSearchViewSet.as_view({'get': 'search'}), name='actor_search'),
    path(r'films', FilmsSearchViewSet.as_view({'get': 'search'}), name='films_search'),
]