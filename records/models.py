from django.db import models


class Course(models.Model):
    """コースマスタ（入門・基礎・実践）"""
    name = models.CharField(max_length=50, unique=True, verbose_name='コース名')
    order = models.IntegerField(default=0, verbose_name='表示順')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')

    class Meta:
        db_table = 'courses'
        ordering = ['order', 'id']
        verbose_name = 'コース'
        verbose_name_plural = 'コース'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ジャンル/タグマスタ"""
    name = models.CharField(max_length=50, unique=True, verbose_name='タグ名')
    order = models.IntegerField(default=0, verbose_name='表示順')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')

    class Meta:
        db_table = 'tags'
        ordering = ['order', 'id']
        verbose_name = 'タグ'
        verbose_name_plural = 'タグ'

    def __str__(self):
        return self.name


class Mentor(models.Model):
    """メンター/記録者マスタ"""
    name = models.CharField(max_length=100, unique=True, verbose_name='メンター名')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')

    class Meta:
        db_table = 'mentors'
        ordering = ['id']
        verbose_name = 'メンター'
        verbose_name_plural = 'メンター'

    def __str__(self):
        return self.name


class Question(models.Model):
    """質問記録"""
    hackathon_name = models.CharField(max_length=50, verbose_name='ハッカソン期間')
    question_date = models.DateField(verbose_name='質問日')
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='questions',
        verbose_name='コース'
    )
    mentor = models.ForeignKey(
        Mentor,
        on_delete=models.PROTECT,
        related_name='questions',
        verbose_name='記録者'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='questions',
        verbose_name='タグ'
    )
    question_content = models.TextField(verbose_name='質問内容')
    answer_content = models.TextField(verbose_name='回答内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    class Meta:
        db_table = 'questions'
        ordering = ['-question_date', '-created_at']
        verbose_name = '質問'
        verbose_name_plural = '質問'

    def __str__(self):
        return f'{self.question_date} - {self.course.name} - {self.question_content[:30]}'