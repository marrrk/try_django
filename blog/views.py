from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleForm


# Create your views here.
# Very simple class based views being shown rn:
class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # queryset = Article.objects.all() basically confines wher you beed to look for objects

    def get_object(self):
        my_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=my_id)
    # class based views have different pieces. the way to change them is to overrite them yourself


class ArticleCreateView(CreateView):

    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    # by automatic, when the form is filled it goes to the url of the new model.
    # you can overrite it using:
    # success_url = '/'
    # or
    # def get_success_url(self):
    #     return '/'

    def is_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

    # need to create a get absolute url method  =


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        my_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=my_id)

    def is_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        my_id = self.kwargs.get('id')
        return get_object_or_404(Article, id=my_id)

    def get_success_url(self):
        return reverse('articles:article-list')



