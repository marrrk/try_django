from django import forms
from .models import Product


class ProductForm(forms.ModelForm):  # first one made. the "easy" one. Can override the tings using:
    title = forms.CharField(label='Title', widget=forms.TextInput( #overrides the title
                                                attrs={
                                                    'placeholder': 'Your Title'
                                                }
                                        )
                            )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'new-class-name two',
                                          'id': 'my-id',
                                          'rows': 20,
                                          'cols': 20
                                      }
                                  )
                                  )
    price = forms.DecimalField()
    # feature = forms.BooleanField()

    # can comment this out, the form will render the same, but it changes how the view
    # function handles this form. the current uncommented one is the one that runs this
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'featured'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        # this function makes sure the form field corresponds to desired things, can be used for other fields
        #if 'mark' not in title:
        #    raise forms.ValidationError("This is not a valid title")
        # if 'dana' not in title:
        #    raise forms.ValidationError("This is not a valid title")
        # if 'potato' not in title:
        #    raise forms.ValidationError("This is not a valid title")
        # if 'car' not in title:
        #    raise forms.ValidationError("This is not a valid title")

        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
                                                attrs={
                                                    'placeholder': 'Your Title'
                                                }
                                        )
                            )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'class': 'new-class-name two',
                                          'id': 'my-id',
                                          'rows': 20,
                                          'cols': 20
                                      }
                                  )

                                  )
    price = forms.DecimalField()
    feature = forms.BooleanField()

# You can change the forms stuffs
# can change something like initial, label, required, etc
# thats how you override the forms
# also changes how the requirements work..?
