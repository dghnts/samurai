from django.db import models
from django.urls import reverse

class Category(models.Model):
    name    = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name                = models.CharField(verbose_name="商品名", max_length=200)
    price               = models.PositiveIntegerField(verbose_name="金額")
    category            = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    img                 = models.ImageField(verbose_name="画像", blank=True, default='noImage.png')
    detail_description  = models.TextField(verbose_name="商品詳細の説明", blank=True, null=True,)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('crud:list')

    