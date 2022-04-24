from django.contrib import admin

# Register your models here.
from .models import Resto
from .models import User

admin.site.register(Resto)
admin.site.register(User)
