from django.contrib import admin
from . models import Product , ProductReviews,Brand,Category,ProductImage
from django_summernote.admin import SummernoteModelAdmin


class ProductModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description',)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','category','brand']
    list_filter = ['category','brand']
    search_fields = ['name','subtitle','description']


class ProductReviewsAdmin(admin.ModelAdmin):
    list_display=['product','rate','date','reviews']
    list_filter = ['rate']
    search_fields = ['name','product','reviews']  



admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReviews,ProductReviewsAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImage)

# Register your models here.
