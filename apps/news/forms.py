from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms
from .models import NewsPreference


class NewsPreferenceForm(forms.ModelForm):
    class Meta:
        model = NewsPreference
        fields = ('country', 'source')
        widgets = {
            'source': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('country', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column('source', css_class='form-group col-md-12 mb-0'),
            ),
            Row(
                Column(
                    Submit('submit', 'Save')
                ),
            )
        )
