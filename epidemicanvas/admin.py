from django.contrib import admin

from .models import Session, Artist, Contributions

admin.site.register(Session)
admin.site.register(Artist)
admin.site.register(Contributions)
