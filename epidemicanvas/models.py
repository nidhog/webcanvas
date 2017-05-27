from django.db import models


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
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __unicode__(self):
        return self.name


class Contributions(models.Model):
    session = models.ForeignKey(Session)
    artist = models.ForeignKey(Artist)
