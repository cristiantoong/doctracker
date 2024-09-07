from django.urls import path
from photos.views import photo_gallery, upload_photo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', photo_gallery, name='photo_gallery'),
    path('upload-photo/', upload_photo, name='upload_photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)