from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class BackgroundImage(TimeStampedModel):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="backgrounds/")
    # 可加标签、作者等字段

    def __str__(self):
        return self.title or f"Image #{self.pk}"

class MusicTrack(TimeStampedModel):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to="music/")
    # 可扩展：duration, artist等
    def __str__(self):
        return self.title

class Quote(TimeStampedModel):
    text = models.TextField()
    author = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=20, default="zh")
    def __str__(self):
        return (self.text[:30] + "...") if len(self.text) > 30 else self.text
