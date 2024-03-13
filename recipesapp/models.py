from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Recipes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    time = models.CharField(verbose_name='Время приготовления')
    img = models.ImageField(upload_to='recipes', verbose_name='Изображение')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse("update", kwargs={"pk": self.pk})

