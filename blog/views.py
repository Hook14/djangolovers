from django.shortcuts import render

# Create your views here.
"Представления размещаются в views.pyфайле. Мы добавим наши представления в этот blog/views.pyфайл."
def post_list(request):
    return render(request, 'blog/post_list.html', {})
("сохраняет returnзначение, полученное в результате вызова другой функции render, которая визуализирует (собирает) "
 "наш шаблон blog/post_list.html.")
