from django.urls import path
from .views import RevieEmailView

urlpatterns = [
    path('review/', RevieEmailView.as_view(), name='reviews'),
]
