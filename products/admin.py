from django.contrib import admin
from . models import Product , ProductReviews,Brand,Category
from django_summernote.admin import SummernoteModelAdmin


class ProductModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description',)


admin.site.register(Product)
admin.site.register(ProductReviews)
admin.site.register(Brand)
admin.site.register(Category)

# Register your models here.
