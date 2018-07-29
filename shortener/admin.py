from django.contrib import admin
from shortener.models import UrlDetails

class UrlDetailsAdmin(admin.ModelAdmin):
    list_display = ('url', 'clicks', 'description_text', 'shortcode', 'timestamp')
    class Meta:
        model = UrlDetails

admin.site.register(UrlDetails, UrlDetailsAdmin)