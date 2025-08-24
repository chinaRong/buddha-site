import csv
import os

from django.core.management.base import BaseCommand, CommandError
from core.models import Quote  # 你的 app 名要改成实际的

class Command(BaseCommand):
    help = "批量导入佛教教言（CSV 文件，字段：text, author）"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help="CSV 文件路径")

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        if not os.path.exists(csv_file):
            raise CommandError(f"CSV 文件不存在: {csv_file}")

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0

            for row in reader:
                text = row.get("text")
                author = row.get("author")

                if not text:
                    self.stderr.write("⚠️ 跳过一行：text 为空")
                    continue

                Quote.objects.create(
                    text=text.strip(),
                    author=author.strip() if author else None
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ 成功导入 {count} 条教言"))
