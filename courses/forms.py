from django import forms
from .models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]

    # raw validating the input
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'mark':
            raise forms.ValidationError('This is not a Valid Title')
        return title

