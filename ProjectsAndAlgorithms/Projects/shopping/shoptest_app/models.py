from django.db import models
from django.urls import reverse
import bcrypt
import re

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(username=postData['username'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name should be at least 2 characters with only letters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name should be at least 2 characters with only letters"
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "The email address is not in the correct format"
        if len(existing_users) != 0:
            errors['email'] = "Your email that you have chosen cannot be used" 
        if len(postData['password']) < 8:
            errors['password'] = "Your password should be at least 8 characters"
        if (postData['password'] != postData['confirm']):
            errors['confirm'] = "Your passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(username=postData['login_username'])

        if len(postData['login_username']) == 0:
            errors ['login_username'] = "Your username needs to be entered"
        if len(postData['login_pass']) == 0:
            errors ['login_pass'] = "Your password needs to be entered"
        if len(postData['login_pass']) < 8:
            errors ['login_pass'] = "An eight character password must be entered"
        if not existing_users:
            errors ['login_pass'] = "Incorrect username or password (not user)"
        elif bcrypt.checkpw(postData['login_pass'].encode(), existing_users[0].password.encode()) != True:
            errors ['login_pass'] = "Incorrect username or password (password)"
        return errors
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    #product.category
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop_app:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop_app:ProdCatDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class User(models.Model):
    username = models.CharField(max_length=255, default=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField(null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User object: {self.username} ({self.id})>"