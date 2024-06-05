from django.forms import ModelForm
from django import forms
from products.models import *


class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = '__all__'


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']


class UpdateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
