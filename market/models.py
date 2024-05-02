from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Product(models.Model):
    category = models.ManyToManyField('Category', verbose_name=_("Category"),
                                      related_name='products')
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=5, decimal_places=2)
    stock = models.IntegerField(verbose_name=_("Stock"))
    image = models.ImageField(verbose_name=_("Image"), upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")