from django.contrib import admin

from .models import Session, Artist, Contributions, Action

admin.site.register(Session)
admin.site.register(Artist)
admin.site.register(Action)
admin.site.register(Contributions)
