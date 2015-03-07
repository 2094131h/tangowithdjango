from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
from django.contrib.auth.models import User

admin.site.register(UserProfile)

# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','website', 'picture','user')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])





