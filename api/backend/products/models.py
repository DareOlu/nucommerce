from django.db import models

# Create your models here.
## Categories of products
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title

## Category = Books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    educational_field = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    item_weight = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    stock_availability = models.BooleanField()
    quantity_in_stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-educational_field']

    def __str__(self):
        return self.title

## Category = Home Electronics
class Home_Electronics(models.Model):
    item_type = models.CharField(max_length=150)
    item_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='grocery', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=150)
    description = models.TextField()
    item_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.URLField()
    stock_availability = models.BooleanField()
    quantity_in_stock = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
     
    class Meta:
        ordering = ['-item_type']

    def __str__(self):
        return self.item_name

## Category = Body Care
class Body_Care(models.Model):
    product_tag = models.CharField(max_length=10)
    item_type = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField()
    brand_name = models.CharField(max_length=150)
    description = models.TextField()
    item_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.URLField()
    stock_availability = models.BooleanField()
    quantity_in_stock = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-item_type']

    def __str__(self):
        return self.item_name