from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    """質問フォーム"""

    class Meta:
        model = Question
        fields = [
            'hackathon_name',
            'question_date',
            'course',
            'mentor',
            'tags',
            'question_content',
            'answer_content',
        ]
        widgets = {
            'question_date': forms.DateInput(attrs={'type': 'date'}),
            'question_content': forms.Textarea(attrs={'rows': 4}),
            'answer_content': forms.Textarea(attrs={'rows': 4}),
            'tags': forms.CheckboxSelectMultiple(),
        }