from django.shortcuts import render
from django.utils import timezone
from .models import Post

"""нужно включить модель, которую мы написали в другом файле models.py. Мы добавим строку from .models import
 Post следующим образом:)
Представления размещаются в views.py файле. Мы добавим наши представления в этот blog/views.py файл."""

def post_list(request):
    "нужно отсортировать опубликованные записи блога по условию published_date"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
"""сохраняет return значение, полученное в результате вызова другой функции render, которая визуализирует (собирает) 
наш шаблон blog/post_list.html."""

