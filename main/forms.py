from django.forms import ModelForm
from main.models import Product

class EntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]