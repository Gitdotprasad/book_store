from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length=20)
    code= models.CharField(max_length=3)

    def __str__(self):
    
        return f"{self.name}"

    class Meta:
        verbose_name_plural= "countries published"

     


class Address(models.Model):
    street = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.street},{self.city}"
    
    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name_plural= "Address Entries"
        

class Author(models.Model):
    first_name= models.CharField(max_length=80)
    last_name= models.CharField(max_length=80)
    Address= models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name.capitalize()}"
    
    def __str__(self):
        return self.full_name()

class book(models.Model):
    title = models.CharField(max_length= 25)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author =models.ForeignKey("Author", on_delete=models.CASCADE,null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False)  #harry potter 1 --> harry-potter-1
    published_countries= models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
     

    def __str__(self):
        return f"{self.title}({self.rating})"
             