from django import forms 

from .models import ProductReviews



class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReviews
        fields = ['name','email','rate','reviews']