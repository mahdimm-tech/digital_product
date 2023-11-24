from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _





class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title =  models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)


    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')



class Product(models.Model):
    title =  models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    Categories = models.ManyToManyField('category', verbose_name=('categories'), blank=True)
    created_time = models.DateField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
            db_table = 'products'
            verbose_name = _('Product')
            verbose_name_plural = _('products')

class File(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('Product'), on_delete=models.CASCADE)
    title =  models.CharField(_('title'), max_length=50)
    description = models.FileField(upload_to = 'files/%Y/%m/%d/')
    # description = models.TextField(_('file'),upload_to = 'files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'),default=True)
    created_time = models.DateField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now=True)

    class Meta:
            db_table = 'files'
            verbose_name = _('file')
            verbose_name_plural = _('files')