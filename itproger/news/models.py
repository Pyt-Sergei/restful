from django.db import models


class Article(models.Model):
    title = models.CharField('title', max_length=50)
    anons = models.CharField('anons', max_length=250)
    full_text = models.TextField('article')
    date = models.DateTimeField('pub_date')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'
