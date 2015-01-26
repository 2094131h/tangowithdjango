from django.contrib import admin
from rango.models import Category, Page

<<<<<<< HEAD
# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
=======
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    def __unicode__(self):
        return self.name
    
#Register models
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
>>>>>>> 12659ef... Chapter 4 - completed





