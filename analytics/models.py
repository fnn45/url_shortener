from django.db import models

from shortener.models import UrlDetails

class ClickEventManager(models.Manager):
    def create_event(self, instance, count=None):
        if isinstance(instance , UrlDetails):
            obj, created = self.get_or_create(st_url=instance)
            if not count:
                obj.count += 1
            else:
                obj.count = count
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    st_url = models.OneToOneField(UrlDetails, related_name='clickevent', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    objects = ClickEventManager()

    def __str__(self):
        return str(self.count)

