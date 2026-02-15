from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import QuestionForm
from .models import Question, Course, Tag
from django.db import models

class QuestionListView(ListView):
    """質問一覧ページ"""
    model = Question
    template_name = 'records/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        """検索・フィルタ機能"""
        queryset = Question.objects.all()

        # キーワード検索
        keyword = self.request.GET.get('keyword')
        if (keyword):
            queryset = queryset.filter(models.Q(question_content__icontains=keyword) | models.Q(answer_content__icontains=keyword))

        # コースでフィルタ
        course_id = self.request.GET.get('course')
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        # タグでフィルタ
        tag_id = self.request.GET.get('tag')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        # ハッカソン期間でフィルタ
        hackathon = self.request.GET.get('hackathon')
        if hackathon:
            queryset = queryset.filter(hackathon_name=hackathon)
            
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        """テンプレートに渡すデータを追加"""
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['tags'] = Tag.objects.all()
        context['hackathons'] = Question.objects.values_list('hackathon_name', flat=True).distinct()
        return context

class QuestionCreateView(CreateView):
    """質問登録ページ"""
    model = Question
    form_class = QuestionForm
    template_name = 'records/question_form.html'
    success_url = reverse_lazy('records:question_list')

class QuestionUpdateView(UpdateView):
    """質問編集ページ"""
    model = Question
    form_class = QuestionForm
    template_name = 'records/question_form.html'
    success_url = reverse_lazy('records:question_list')

class QuestionDeleteView(DeleteView):
    """質問削除ページ"""
    model = Question
    template_name = 'records/question_confirm_delete.html'
    success_url = reverse_lazy('records:question_list')