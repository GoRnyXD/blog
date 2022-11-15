from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField('Изображение', upload_to='profile/', blank=True, null=True)
    number = models.CharField('Номер', max_length=14)
    description = models.CharField('Описание', max_length=255)
    country = models.CharField('Страна', max_length=100)
    city = models.CharField('Город', max_length=100)
    language = models.CharField('Язык', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
      

    class Meta:  
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('created',)  

    def __str__(self):
        return f'{self.user.username} {self.country} {self.city}'


class Category(models.Model):
    name = models.CharField('Название категории', max_length=255)
    slug = models.SlugField(max_length=24)

    class Meta:  
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Tags(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=24)

    class Meta:  
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField('Загаловок', max_length=255)
    text = models.TextField('Текст')
    image = models.ImageField('Изображение', upload_to='blog/')
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=24)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True) 
    published = models.BooleanField()

    class Meta:  
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('created',)  

    def __str__(self):
        return f'{self.user} {self.title} {self.slug}'


class Comments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.CharField('Текст', max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Публикация')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True) 

    class Meta:  
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)  

    def __str__(self):
        return f'{self.user} {self.text}'
