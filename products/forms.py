from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={"placeholder":'Your Description...'}))
    price = forms.DecimalField(initial=19.99)
    class Meta:
        model = Product
        fields = [
            'title', 'description', 'price'
        ]

    def clean_title(self, *args, **kwargs): #args and kwargs might not be required.
        title = self.cleaned_data['title']  #self.cleaned_data.get('title') also works.
        if not '@s' in title:
            raise forms.ValidationError('Invalid entry, does not contain "@"')
        return title
