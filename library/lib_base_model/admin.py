from django.contrib import admin

from .models import Book, Publisher, Section, User as My_User, Membership, Borrow

from django.contrib.auth.models import User, Group

# Register your models here.


admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Section)
admin.site.register(My_User)
admin.site.register(Membership)
admin.site.register(Borrow)

