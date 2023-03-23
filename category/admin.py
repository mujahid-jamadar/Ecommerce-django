from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    # slug pre-populated field

    prepopulated_fields={'slug':('Category_name',)}

    list_display=('Category_name','slug')

# Register your models here.

admin.site.register(Category,CategoryAdmin)


