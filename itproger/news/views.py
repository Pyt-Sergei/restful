from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Article
from .forms import FormArticle


def news_home(request):
    news = Article.objects.order_by('-date')
    data = {
        'news': news
    }
    return render(request, 'news/news_home.html', data)


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create_article.html'

    form_class = FormArticle


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create_news(request):
    error = ''

    if request.method == 'POST':
        form = FormArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Error occured while adding article"

    else:
        form = FormArticle()
        data = {
            'form': form,
            'error': error,
        }
    return render(request, 'news/create_article.html', data)
