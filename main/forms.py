from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class EntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
    def clean_mood(self):
        mood = self.cleaned_data["mood"]
        return strip_tags(mood)

    def clean_feelings(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)
        



