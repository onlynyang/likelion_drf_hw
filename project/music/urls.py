from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="music"
urlpatterns = [
    path('song', views.song_list_create),
    path('', views.singer_list_create),
    path('singer/<int:singer_id>', views.singer_detail_update_delete),
    path('song/<int:song_id>', views.song_detail_update_delete),
    path('song/<int:song_id>/comment', views.comment_read_create),
    path('singer/tags/<str:tag_name>', views.find_tag),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)