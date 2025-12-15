from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect  # могли сразу перейти на post_detailстраницу с нашей только что созданной записью в блоге
from .forms import PostForm
"""нужно включить модель, которую мы написали в другом файле models.py. Мы добавим строку from .models import
 Post следующим образом:)
Представления размещаются в views.py файле. Мы добавим наши представления в этот blog/views.py файл."""

def post_list(request):
    """нужно отсортировать опубликованные записи блога по условию published_date"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

"Cоздаем новую форму"
def post_new(request):
    "Создаем новую Post форму, нам нужно вызвать PostForm()её и передать в шаблон"
    "метод отправки форм "
    if request.method == 'POST': #Если method этот POST так, то нам нужно построить объект
        form = PostForm(request.POST)
        if form.is_valid(): # проверить правильность заполнения формы (все обязательные поля заполнены и не были отправлены некорректные значения)
            post = form.save(commit=False)
            post.author = request.user # добавляем автора (поскольку author в исходной форме не было поля PostForm, а это поле обязательно).
            post.published_date = timezone.now()
            post.save() # действительна ли форма, и если да, то можем её сохранить
            return redirect('post_detail', pk=post.pk)
            """post_detail— это имя представления, на которое мы хотим перейти. Помните, что для этого представления 
            требуется pkпеременная? Чтобы передать её представлениям, мы используем `<имя_представления>` pk=post.pk, 
            где post`<имя_представления>` — это имя только что созданного поста в блоге!"""
    else:
            form=PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # # передаем дополнительный pk параметр из urls, получаем Postмодель, которую хотим редактировать, get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # request.POST атрибут будет содержать все поля из формы,  оно связано с тем, что мы «публикуем» данные
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  # а затем, при создании формы, передаем этот пост в качестве instance, как при сохранении формы
    return render(request, 'blog/post_edit.html', {'form': form})
"""сохраняет return значение, полученное в результате вызова другой функции render, которая визуализирует (собирает) 
наш шаблон blog/post_list.html."""

