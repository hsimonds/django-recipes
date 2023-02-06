from django.urls import path
from . import views
from .views import RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='recipe-home'),
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/update/<pk>', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/delete/<pk>', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
