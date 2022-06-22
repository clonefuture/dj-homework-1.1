from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book
from collections import OrderedDict


def books_view(request, date=False):
    template = 'books/books_list.html'
    date_sort = [str(items.pub_date) for items in Book.objects.all().order_by('pub_date')]
    date_list_sort = list(OrderedDict.fromkeys(date_sort))
    date_dict = {date: page for page, date in enumerate(date_list_sort, 1)}

    if date:
        book = Book.objects.filter(pub_date=date)
        page_num = date_dict[date]
        paginator = Paginator(date_list_sort, 1)
        page = paginator.get_page(page_num)
        index = date_list_sort.index(date)
        if index == 0:
            prev_date = date_list_sort[index]
            next_date = date_list_sort[index + 1]
        elif index == len(date_list_sort) - 1:
            prev_date = date_list_sort[index - 1]
            next_date = date_list_sort[index]
        else:
            prev_date = date_list_sort[index - 1]
            next_date = date_list_sort[index + 1]
        context = {
            'books': book,
            'page': page,
            'prev_date': prev_date,
            'next_date': next_date
        }
    else:
        book = Book.objects.all()
        context = {
            'books': book,
        }
    return render(request, template, context)
