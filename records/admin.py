from django.contrib import admin

from django.contrib import admin
from .models import Course, Tag, Mentor, Question


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """コース管理"""
    list_display = ['name', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """タグ管理"""
    list_display = ['name', 'order', 'created_at']
    list_editable = ['order']
    search_fields = ['name']


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    """メンター管理"""
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """質問記録管理"""
    list_display = ['question_date', 'hackathon_name', 'course', 'mentor', 'short_question']
    list_filter = ['hackathon_name', 'course', 'tags', 'mentor', 'question_date']
    search_fields = ['question_content', 'answer_content']
    filter_horizontal = ['tags']
    date_hierarchy = 'question_date'

    def short_question(self, obj):
        """質問内容を短縮表示"""
        if len(obj.question_content) > 50:
            return obj.question_content[:50] + '...'
        return obj.question_content
    short_question.short_description = '質問内容'