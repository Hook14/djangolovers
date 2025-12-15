from django import forms
from .models import Post
# Импортируем модель django(forms), а потом подключаем модель Post

class PostForm(forms.ModelForm): # Название нашей модели(PostForm)

    class Meta: #  где мы указываем Django, какую модель следует использовать для создания этой формы
        model = Post # где мы указываем Django, какую модель следует использовать для создания этой формы
        fields = ('title','text') # указываем поля, которые хотим создать
