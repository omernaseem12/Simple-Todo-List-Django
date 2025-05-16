from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_cat = models.CharField(max_length=50,default="")
    product_subcat = models.CharField(max_length=50,default="")
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=300)
    product_pubdate = models.DateField()
    product_img = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name
