import graphene

from .types import Query as SchemeQuery
from .mutation import Mutation as SchemeMutation

class Query(SchemeQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query = Query)

class Mutation(SchemeMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)