from django.db import models

class People(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    movies = models.ManyToManyField('Movie')

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=200)
    gravity = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    opening_crawl = models.TextField()
    planets = models.ManyToManyField('Planet')
    director = models.CharField(max_length=255)
    producers = models.CharField(max_length=255)

    def __str__(self):
        return self.title