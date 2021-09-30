import graphene
from graphene.types import decimal
from graphene_django import DjangoObjectType
from .models import Category, Book, Home_Electronics, Body_Care

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = (
            'id',
            'title',)

class Home_ElectronicsType(DjangoObjectType):
    class Meta: 
        model = Home_Electronics
        fields = (
            'id',
            'item_type',
            'item_name',
            'category',
            'brand_name',
            'description',
            'item_weight',
            'price',
            'discount',
            'imageurl',
            'stock_availability',
            'quantity_in_stock',
            'date_created',
        )  

class BookType(DjangoObjectType):
    class Meta: 
        model = Book
        fields = (
            'id',
            'title',
            'author_name',
            'publisher',
            'educational_field',
            'isbn',
            'pages',
            'price',
            'discount',
            'item_weight',
            'quantity',
            'description',
            'stock_availability',
            'quantity_in_stock',
            'category',
            'date_created',
        )  

class Body_CareType(DjangoObjectType):
    class Meta: 
        model = Body_Care
        fields = (
            'id',
            'product_tag',
            'item_type',
            'name',
            'category',
            'status',
            'brand_name',
            'description',
            'item_weight',
            'price',
            'discount',
            'imageurl',
            'stock_availability',
            'quantity_in_stock',
            'date_created',
        )  

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    home_electronics = graphene.List(Home_ElectronicsType)
    books = graphene.List(BookType)
    bodycares = graphene.List(Body_CareType)

    # Querying a list
    def resolve_categories(root, info, **kwargs):      
        return Category.objects.all()

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()

    def resolve_home_electronics(root, info, **kwargs):
        # Querying a list
        return Home_Electronics.objects.all()

    def resolve_bodycares(root, info, **kwargs):
        # Querying a list
        return Body_Care.objects.all()


#################################
#                               #
#       MUTUATIONS              #
#                               #
#################################

#-----------
# Category
#-----------

class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        
        return CreateCategory(category=category)

class UpdateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        id = graphene.ID()
    category = graphene.Field(CategoryType)

    # Mutation to update a category 
    @classmethod
    def mutate(cls, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)

class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, id):
        category = Category.objects.get(pk=id)
        category.delete()


#-----------
# Books
#-----------
class BookInput(graphene.InputObjectType):

    title = graphene.String()
    author_name = graphene.String()
    publisher = graphene.String()
    educational_field = graphene.String()
    isbn = graphene.Int()
    pages = graphene.Int()
    price = graphene.Float()
    discount = graphene.Float()
    item_weight = graphene.Float()
    quantity = graphene.Int()
    description = graphene.String()
    stock_availability = graphene.Int()
    quantity_in_stock = graphene.Int()
    category = graphene.String()

class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title 
        book.author_name = input.author_name
        book.publisher = input.publisher
        book.educational_field = input.educational_field
        book.isbn = input.isbn
        book.pages = input.pages
        book.price = decimal.Decimal(input.price)
        book.discount = decimal.Decimal(input.discount)
        book.item_weight = decimal.Decimal(input.item_weight)
        book.description = input.description
        book.stock_availability = input.stock_availability
        book.quantity_in_stock = input.quantity_in_stock
        book.category = input.category
        book.save()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.get(pk=id)
        book.title = input.title 
        book.author_name = input.author_name
        book.publisher = input.publisher
        book.educational_field = input.educational_field
        book.isbn = input.isbn
        book.pages = input.pages
        book.price = decimal.Decimal(input.price)
        book.discount = decimal.Decimal(input.discount)
        book.item_weight = decimal.Decimal(input.item_weight)
        book.description = input.description
        book.stock_availability = input.stock_availability
        book.quantity_in_stock = input.quantity_in_stock
        book.category = input.category
        book.save()
        return UpdateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    book= graphene.Field(BookType)

    @classmethod
    def mutate(cls, id):
        book = Book.objects.get(pk=id)
        book.delete()


class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    delete_category = CreateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

#################################
#                               #
#       SCHEMA                  #
#                               #
#################################

schema = graphene.Schema(query=Query, mutation=Mutation)
