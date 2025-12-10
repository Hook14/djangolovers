from django.conf import settings
from django.db import models
from django.utils import timezone

"""
class Post(models.Model):– эта строка определяет нашу модель (это object).

class— специальное ключевое слово, указывающее, что мы определяем объект.
Post - Имя нашей модели. Мы можем дать ей другое имя (но следует избегать специальных символов и
 пробелов). Имя класса всегда должно начинаться с заглавной буквы.
models.
Model - означает, что Post является моделью Django, поэтому Django знает, что ее следует 
сохранить в базе данных.
Теперь определим свойства, о которых мы говорили: title, text, created_date, published_date и 
author. Для этого нам нужно определить тип каждого поля (текст? Число? Дата? Связь с другим 
объектом, например, «Пользователь»?).
"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # models.ForeignKey– это ссылка на другую модель.
    title = models.CharField(max_length=200) # models.CharField– так определяется текст с ограниченным количеством символов.
    text = models.TextField() # models.TextField– это для длинных текстов без ограничений. Звучит идеально для контента блога, правда?
    created_date = models.DateTimeField(default=timezone.now) # models.DateTimeField– это дата и время
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
