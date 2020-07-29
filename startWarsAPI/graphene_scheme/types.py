import graphene

from graphene_django.types import DjangoObjectType

from graphQLStartwars.models import People, Movie, Planet

class PeopleType(DjangoObjectType):
    class Meta:
        model = People

class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class Query(object):
    movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())
    all_planet = graphene.List(PlanetType)
    all_people = graphene.List(PeopleType)
    all_movies = graphene.List(MovieType)

    def resolve_all_people(self, info, **kwargs):
        return People.objects.all()
    
    def resolve_all_planet(self, info, **kwargs):
        return Planet.objects.all()

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_people(self, info, **kwargs):
        name = kwargs.get('name')

        if name is not None:
            return People.objects.get(name=name)

        return People.objects.all()

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        if id is not None:
            return Movie.objects.get(pk=id)
        
        if title is not None:
            return Movie.objects.get(title=title)

        return None