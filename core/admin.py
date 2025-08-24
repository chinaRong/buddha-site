from django.contrib import admin
from .models import BackgroundImage, MusicTrack, Quote

@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title",)

@admin.register(MusicTrack)
class MusicTrackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title",)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "language", "is_active", "created_at")
    list_filter = ("language", "is_active")
    search_fields = ("text", "author", "source")

