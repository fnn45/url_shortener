from django import forms
from .models import UrlDetails
from shortener.validators import validate_url
import datetime

class CheckoutForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url],
                          widget=forms.TextInput(
                          attrs={'placeholder': 'URL',
                                 'class': 'form-control'}
                          ))


class AdjustmentForm(forms.ModelForm):
    count = forms.IntegerField()
    class Meta:
        model = UrlDetails
        fields = [ 'url', 'shortcode', 'description_text', 'timestamp' ]

    def clean(self):
        cleaned_data     = super(AdjustmentForm, self).clean()
        shortcode        = cleaned_data.get('shortcode')
        description_text = cleaned_data.get('description_text')
        count            = cleaned_data.get('count')
        timestamp        = cleaned_data.get('timestamp')

        if not shortcode or len(shortcode.split(' ')) > 1:
            raise forms.ValidationError('Short url is not valid')
        if len(description_text) > 300:
            raise forms.ValidationError('Description is too long')
        try:
            if int(count) < 0:
                raise forms.ValidationError('Count must be positive integer')
        except TypeError:
            raise forms.ValidationError('You must define count')
        try:
            datetime.datetime.strptime(str(timestamp), '%Y-%m-%d')
        except:
            raise forms.ValidationError("Incorrect data format, should be MM/DD/YYYY")
        return cleaned_data

