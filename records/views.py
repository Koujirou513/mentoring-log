from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import QuestionForm
from .models import Question

class QuestionListView(ListView):
    """質問一覧ページ"""
    model = Question
    template_name = 'records/question_list.html'
    context_object_name = 'questions'


class QuestionCreateView(CreateView):
    """質問登録ページ"""
    model = Question
    form_class = QuestionForm
    template_name = 'records/question_form.html'
    success_url = reverse_lazy('records:question_list')