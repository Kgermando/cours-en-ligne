from django.contrib import admin

from courses.models import Category, Category_index, Courses
# Register your models here.
admin.site.site_header = 'COURSES ONLINE'

admin.site.register(Courses)
admin.site.register(Category)
admin.site.register(Category_index)
