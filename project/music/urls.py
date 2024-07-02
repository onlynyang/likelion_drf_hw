from django.urls import path
from .views import *
from . import views

app_name="music"
urlpatterns = [
    path('song', views.song_list_create),
    path('', views.singer_list_create),
    path('<int:singer_id>', views.singer_detail_update_delete),
    path('<int:song_id>', views.song_detail_update_delete),
    path('<int:song_id>/comment', views.comment_read_create),
]