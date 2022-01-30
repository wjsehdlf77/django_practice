from django.db import models

class Members(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name


class RendBook(models.Model):
    name = models.ForeignKey(Members, on_delete = models.CASCADE)
    book_name = models.CharField(max_length = 200)
    money = models.CharField(max_length=50)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.book_name





