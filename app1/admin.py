from django.contrib import admin
from app1.models import Vehicle,User,Categories,Role
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Role)