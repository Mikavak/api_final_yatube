from django.contrib.auth import get_user_model
from django.db import models

from .constant import TITLE_FIELD_LEN

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=TITLE_FIELD_LEN,
        verbose_name='Название категории')
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = 'категория'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор')
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='каритинка')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='категория поста'
    )

    class Meta:
        verbose_name = 'Пост'
        ordering = ('id',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор коммента')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост комеентария')
    text = models.TextField(verbose_name='Текст коммента')
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'комментарий'

    def __str__(self):
        return self.post


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Пользователь')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписки')

    class Meta:
        verbose_name = 'подписка'
        unique_together = ('user', 'following')

    def __str__(self):
        return self.user
