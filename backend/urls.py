from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import RandomBackgroundImage, RandomMusicTrack, RandomQuote

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/random/image", RandomBackgroundImage.as_view()),
    path("api/random/music", RandomMusicTrack.as_view()),
    path("api/random/quote", RandomQuote.as_view()),
]

# 开发环境用 Django 直接提供媒体文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

