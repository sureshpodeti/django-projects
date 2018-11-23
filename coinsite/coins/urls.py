from django.urls import path
from .views import QueryPageView
urlpatterns = [
    path('', QueryPageView.as_view(), name='query_page'),
]