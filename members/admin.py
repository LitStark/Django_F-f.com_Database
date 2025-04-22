from django.contrib import admin
from .models import Member,UserProfile

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user','first_name', 'last_name','phone','email','city','state')
admin.site.register(Member, MemberAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','dob','gender' )
admin.site.register(UserProfile, UserProfileAdmin)
