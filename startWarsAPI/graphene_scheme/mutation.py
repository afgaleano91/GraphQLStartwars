import graphene
from graphQLStartwars.models import *
from .types import *

class CreatePeopleMutation(graphene.Mutation):
    class Input:
        name = graphene.String(required=True)

    people = graphene.Field(PeopleType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '').strip()
        obj = People.objects.create(name=name)
        return CreatePeopleMutation(people=obj)

class CreatePlanetMutation(graphene.Mutation):
    class Input:
        name = graphene.String(required=True)
        gravity = graphene.String()
    
    planet = graphene.Field(PlanetType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '').strip()
        gravity = kwargs.get('gravity', '').strip()
        obj = Planet.objects.create(name=name, gravity=gravity)
        return CreatePlanetMutation(planet=obj)

class CreateMovieMutation(graphene.Mutation):
    class Input(object):
        title = graphene.String(required=True)
        opening_crawl = graphene.String(required=True)
        director = graphene.String(required=True)
        producers = graphene.String(required=True)
    
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, **kwargs):
        title = kwargs.get('title', '').strip()
        opening_crawl = kwargs.get('opening_crawl', '')
        director = kwargs.get('director', '')
        producers = kwargs.get('producers', '')

        obj = Movie.objects.create(title=title, opening_crawl=opening_crawl, director=director, producers= producers)

        return CreateMovieMutation(movie=obj)

class Mutation(graphene.AbstractType):
    create_people = CreatePeopleMutation.Field()
    create_planet = CreatePlanetMutation.Field()
    create_movie = CreateMovieMutation.Field()