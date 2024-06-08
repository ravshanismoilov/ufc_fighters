from django.urls import path
from .views import get_home, CategoryFighters, CategoryDetailFighter, FighterDetail, CreateFighter


urlpatterns = [
    path('', get_home, name='homepage'),
    path('category-fighter/', CategoryFighters.as_view(), name='category-fighter'),
    path('category-detail/<int:pk>', CategoryDetailFighter.as_view(), name='category-detail'),
    path('fighter-detail/<int:pk>', FighterDetail.as_view(), name='fighter-detail'),
    path('add-fighter', CreateFighter.as_view(), name='add-fighter'),
]