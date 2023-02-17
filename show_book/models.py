from django.db import models

class ShowBook(models.Model):
    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('MELODRAMME', 'MELODRAMME'),
    )

    title = models.CharField('Название книги', max_length=100)
    description = models.TextField('Описание книги')
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колличество серий')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('Цена книги', null=True)

    def __str__(self):
        return self.title