from django.db.models import Max
import random
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView, UpdateView
from .models import Recipes, Category
from .form import RecipesForm


class Index(TemplateView):
    template_name = 'recipesapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = Category.objects.all()
        max_id = Recipes.objects.all().aggregate(max_id=Max("id"))['max_id']
        if max_id > 5:
            id = []
            while len(id) < 5:
                r_id = random.randint(1, max_id)
                if r_id not in id:
                    id.append(r_id)
        else:
            id = [i for i in range(1, max_id+1)]
        context['object_list'] = []
        for i in id:
            context['object_list'].append(Recipes.objects.get(id=i))
        return context


class CreateRecipies(View):
    def get(self, request):
        return render(self.request, 'recipesapp/addrecipes.html', {'form': RecipesForm()})

    def post(self, request):
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            Recipes.objects.create(category=form.cleaned_data['category'],
                                   name=form.cleaned_data['name'],
                                   description=form.cleaned_data['description'],
                                   cooking_steps=form.cleaned_data['cooking_steps'],
                                   time=form.cleaned_data['time'],
                                   img=form.cleaned_data['img'],
                                   autor=request.user)
            return HttpResponseRedirect(reverse('index'))


class CategoryList(ListView):
    model = Recipes
    template_name = 'recipesapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super(CategoryList, self).get_queryset()
        filter = self.kwargs.get('pk')
        return queryset.filter(category_id=filter) if filter else queryset


class RecipesDetail(DetailView):
    model = Recipes
    template_name = 'recipesapp/recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Рецепт {self.object.name}'
        context['categories'] = Category.objects.all()
        return context


class UpdateRecipes(UpdateView):
    model = Recipes
    fields = ['name', 'description', 'cooking_steps', 'time', 'img']
    template_name = 'recipesapp/addrecipes.html'

    def form_valid(self, form):
        if self.object.autor != self.request.user:
            return HttpResponseRedirect(reverse('index'))
        return super().form_valid(form)
