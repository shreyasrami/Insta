from django.contrib import admin
from .models import Post,Profile,Like,Comment

# Register your models here.

admin.site.register((Comment,Like,Post,Profile))
admin.site.site_header = 'My administration'
admin.site.site_title = 'Socio Insta'
admin.site.index_title = 'Site admin panel'