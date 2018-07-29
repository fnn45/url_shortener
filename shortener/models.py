from django.db import models
import datetime
from django.conf import settings
from shortener.validators import validate_url


SHORT_CODE_MAX = getattr(settings, 'SHORT_CODE_MAX', 15)
TRADEMARK_ICON = u"\u2122"

class UrlDetails(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORT_CODE_MAX, blank=True, null=True)
    description_text = models.TextField( blank=True, null=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name_plural='UrlDetails'

    def save(self, *args, **kwargs):
        if not 'http' in self.url:
            self.url = 'http//' + self.url
        self.description_text = self.modify_description_text(self.description_text)
        super(UrlDetails, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def modify_description_text(self, text):
        try:
            for word in text.split():
                if len(word) == 6:
                    text = text.replace(word, word + TRADEMARK_ICON)
            return text
        except:
            return 'no description'

    def get_short_url(self):
        return self.shortcode

    @property
    def clicks(self):
        try:
            return self.clickevent.count
        except: return 0

 
