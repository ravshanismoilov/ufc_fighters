from django.urls import path
from .views import get_home, CategoryFighters, CategoryDetailFighter


urlpatterns = [
    path('', get_home, name='homepage'),
    path('category-fighter/', CategoryFighters.as_view(), name='category-fighter'),
    path('fighters/<int:pk>', CategoryDetailFighter.as_view(), name='fighters'),
]