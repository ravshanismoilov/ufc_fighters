from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=155)

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.name


class Fighter(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    date_birth = models.DateField()
    country = models.ForeignKey(to=Country, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    height = models.IntegerField()
    wins = models.IntegerField()
    loss = models.IntegerField()
    draw = models.IntegerField()
    photo = models.ImageField(upload_to='', blank=True, null=True)

    class Meta:
        db_table = 'fighter'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.category}'