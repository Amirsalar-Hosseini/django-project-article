from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import CreateArticleForm, UpdateArticleForm
from plyer import notification
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from category.models import Category


def blog_page(request):
    articles = Article.article.all()
    categories = Category.objects.all()
    search = request.GET.get('search')
    if search:
        articles = articles.filter(title__icontains=search)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object,
        'categories': categories
    }
    return render(request, 'blog/index.html', context)


def article_page(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    articles = Article.article.all()
    context = {
        'article': article,
        'articles': articles
    }
    return render(request, 'blog/detail.html', context)


@login_required(redirect_field_name='redirect')
def create_article(request):
    form = CreateArticleForm(data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        article_title = form.cleaned_data.get('title')
        article_text = form.cleaned_data.get('text')
        article_image = form.cleaned_data.get('image')
        Article.article.create(title=article_title, text=article_text, image=article_image, author=request.user)
        notification.notify(
            title='Successful!!',
            message=f'Article({article_title}) created successfully',
            timeout=2
        )
        return redirect('blog:blog_page')
    context = {
        'form': form
    }
    return render(request, 'blog/create_article.html', context)


@login_required
def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author_id=request.user.id)
    if request.method == 'GET':
        form = UpdateArticleForm(initial={'title': article.title, 'text': article.text})
    else:
        form = UpdateArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article_title = form.cleaned_data.get('title')
            article_text = form.cleaned_data.get('text')
            article_image = form.cleaned_data.get('image')
            if article_image:
                article.image = article_image
            article.title = article_title
            article.text = article_text
            article.save()
            return redirect('blog:article_page', article_id)
    context = {
        'form': form,
        'article': article
    }
    return render(request, 'blog/update_article.html', context)


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author_id=request.user.id)
    article.delete()
    return redirect('blog:blog_page')


def get_article_by_category(request, category_id):
    articles = Article.article.filter(categories=category_id)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object
    }
    return render(request, 'blog/index.html', context)


def get_article_by_author(request, author_id):
    author = get_object_or_404(User, id=author_id)
    articles = author.articles.all()
    # articles = Article.article.filter(author_id=author_id)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object,
        'author': author
    }
    return render(request, 'blog/index.html', context)

