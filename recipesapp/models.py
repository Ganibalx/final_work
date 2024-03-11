from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    time = models.TimeField(verbose_name='Время приготовления')
    img = models.ImageField(upload_to='recipes', verbose_name='Изображение')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
