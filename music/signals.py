import os
from django.db import models
from .models import Music
from django.dispatch import receiver
# from django.utils.translation import ugettext_lazy as _

@receiver(models.signals.post_delete, sender=Music)
def auto_delete_audio_file_on_delete(sender, instance, **kwargs):
    if instance.audio_file:
        if os.path.isfile(instance.audio_file.path):
            os.remove(instance.audio_file.path)