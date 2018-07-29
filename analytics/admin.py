from django.contrib import admin

from analytics.models import ClickEvent


class ClickEventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ClickEvent._meta.fields]
    class Meta:
        model = ClickEvent


admin.site.register(ClickEvent, ClickEventAdmin)
