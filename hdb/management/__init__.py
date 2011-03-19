import models
#from django.db.models import signals, get_apps, get_models
from django.dispatch import receiver

@receiver(post_syncdb, sender=models)
def init_data(app, created_models, verbosity, **kwargs):
    if models.DNSZone in created_models:
        zone = models.DNSZone(
            zonename="Global",
            ttl = 43200 # 12Hr TTL
        )
        zone.save()
