from django.shortcuts import render
from .models import Recipe
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    search_filter = request.GET.get('filter', '')
    if search_filter != '':
        title_match = Recipe.objects.filter(title__contains=search_filter)
        ingredient_match = Recipe.objects.filter(ingredients__contains=search_filter)
        description_match = Recipe.objects.filter(description__contains=search_filter)
        content_match = Recipe.objects.filter(content__contains=search_filter)
        context = {
            'recipes': title_match | ingredient_match | description_match | content_match
        }
    else:
        context = {
            'recipes': Recipe.objects.all()
        }
    return render(request, 'recipe/home.html', context)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description', 'prep_time', 'cook_time', 'ingredients', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'prep_time', 'cook_time', 'ingredients', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RecipeDetailView(DetailView):
    model = Recipe
