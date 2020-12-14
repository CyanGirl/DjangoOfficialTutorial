from django.contrib import admin

# Register your models here.
# importing the table model
from .models import Question

# saving it in th admin interface
admin.site.register(Question)
