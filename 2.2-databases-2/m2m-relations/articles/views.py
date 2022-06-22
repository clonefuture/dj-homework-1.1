from django.shortcuts import render

from .models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().order_by('-published_at')
    tag_ob = Tag.objects.all()
    context = {'object_list': object_list,
               'tag_ob': tag_ob}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
