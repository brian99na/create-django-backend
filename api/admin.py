from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.post import Post


admin.site.register(User)
admin.site.register(Post)