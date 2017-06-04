from django.db import models

from .fields import ImageBase64Field


class Artist(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Session(models.Model):
    name = models.CharField(max_length=50, null=True)
    artist = models.ForeignKey(Artist)
    # add field for storing flattened image in Base64
    image = models.ImageField(default=None, upload_to="images")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __unicode__(self):
        return self.name


class Contributions(models.Model):
    session = models.ForeignKey(Session)
    artist = models.ForeignKey(Artist)
    # add field for storing flattened image in Base64
    image = ImageBase64Field()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contribution"
        verbose_name_plural = "Contributions"

