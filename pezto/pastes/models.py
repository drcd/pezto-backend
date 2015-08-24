from django.db import models

from django.conf import settings

from hashids import Hashids


class Paste(models.Model):
    """ Paste Model

    uid:        A unique identifier that is generated using the Hashids library.
                It basically creates YouTube-like IDs using alphanumeric characters.
    title:      The title of the paste. Default value is 'Untitled Paste'.
    content:    The text content of the paste.
    created_at: The creation date of the paste.
    ip_addr:    The uploaders IP address. It accepts both IPv4 and IPv6.

    """
    uid = models.CharField(max_length=16, blank=True)
    title = models.CharField(max_length=80, default="Untitled Paste")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    password = models.CharField(blank=True, null=True, max_length=128)
    ip_addr = models.GenericIPAddressField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Paste, self).save(*args, **kwargs)  # Save to DB
        # Generate UID from current ID
        self.uid = Hashids(min_length=6, salt=settings.PEZTO_HASHIDS_SEED).encode(self.id)
        super(Paste, self).save(*args, **kwargs)  # Apply changes
        
    class Meta:
        ordering = ('created_at',)
