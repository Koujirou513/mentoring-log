from django.core.management.base import BaseCommand
from records.models import Course, Tag


class Command(BaseCommand):
    """初期マスタデータを投入するコマンド"""
    help = '初期マスタデータ（コース・タグ）を投入します'

    def handle(self, *args, **options):
        # コースの初期データ
        courses = [
            {'name': '入門コース', 'order': 1},
            {'name': '基礎コース', 'order': 2},
            {'name': '実践コース', 'order': 3},
        ]
        for course_data in courses:
            course, created = Course.objects.get_or_create(
                name=course_data['name'],
                defaults={'order': course_data['order']}
            )
            status = '作成' if created else 'スキップ（既存）'
            self.stdout.write(f"コース: {course.name} - {status}")

        # タグの初期データ
        tags = [
            {'name': '要件定義', 'order': 1},
            {'name': '環境構築', 'order': 2},
            {'name': 'Docker', 'order': 3},
            {'name': 'Git', 'order': 4},
            {'name': 'バックエンド', 'order': 5},
            {'name': 'フロントエンド', 'order': 6},
            {'name': 'インフラ', 'order': 7},
            {'name': 'DB', 'order': 8},
            {'name': '開発ツール', 'order': 9},
            {'name': 'HTML/CSS', 'order': 10},
            {'name': 'JavaScript', 'order': 11},
            {'name': 'Flask', 'order': 12},
            {'name': 'Django', 'order': 13},
            {'name': 'その他', 'order': 99},
        ]
        for tag_data in tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_data['name'],
                defaults={'order': tag_data['order']}
            )
            status = '作成' if created else 'スキップ（既存）'
            self.stdout.write(f"タグ: {tag.name} - {status}")

        self.stdout.write(self.style.SUCCESS('初期データの投入が完了しました'))