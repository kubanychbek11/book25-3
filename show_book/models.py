import types

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


RAITING = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'4')
)
class Rating(models.Model):
    book = models.ForeignKey(ShowBook, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RAITING)

class RatingBook(models.Model):
    RAITING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '4')
    )
    choice_show = models.ForeignKey(ShowBook, on_delete=models.CASCADE,
                                    related_name='comment_object')
    rate = models.CharField(max_length=100, null=True, choices=RAITING)
    created_date = models.DateTimeField(auto_now_add=True)








