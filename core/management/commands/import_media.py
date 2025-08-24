from django.core.management.base import BaseCommand
import os
from django.core.files import File
from core.models import BackgroundImage, MusicTrack

class Command(BaseCommand):
    help = "批量导入图片和音乐"

    def add_arguments(self, parser):
        parser.add_argument("--images", type=str, help="图片文件夹路径")
        parser.add_argument("--music", type=str, help="音乐文件夹路径")

    def handle(self, *args, **options):
        if options["images"]:
            img_dir = options["images"]
            for fname in os.listdir(img_dir):
                path = os.path.join(img_dir, fname)
                if os.path.isfile(path):
                    with open(path, "rb") as f:
                        BackgroundImage.objects.create(image=File(f, name=fname))
            self.stdout.write(self.style.SUCCESS("图片导入完成！"))

        if options["music"]:
            music_dir = options["music"]
            for fname in os.listdir(music_dir):
                path = os.path.join(music_dir, fname)
                if os.path.isfile(path):
                    with open(path, "rb") as f:
                        MusicTrack.objects.create(title=fname, audio=File(f, name=fname))
            self.stdout.write(self.style.SUCCESS("音乐导入完成！"))
