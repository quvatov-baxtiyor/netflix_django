from django.urls import path
from .views import ActorAPIView,MovieAPIView
# ResAPIView,
urlpatterns = [
    # path('kino/',ResAPIView.as_view(), name='kino')
    path('movies/',MovieAPIView.as_view(),name='movies'),
    path('actors/',ActorAPIView.as_view(),name='actors'),
]
