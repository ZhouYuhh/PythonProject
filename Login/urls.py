from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'Login'
urlpatterns = [
    path('',views.index, name='index'),
    path('index/', views.index, name='index'),
    path('index/<str:category>/', views.category, name='category'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('details/<int:rest_id>/', views.details, name='details'),
    path('details/<int:rest_id>/rate/', views.rate, name='rate'),
    path('details/<int:rest_id>/review/<int:review_id>/', views.comment, name='comment'),
    path('new_rest/', views.new, name='new'),
    path('add_rest/', views.add, name='add')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)