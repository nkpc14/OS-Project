from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Process)
admin.site.register(Processed)
admin.site.register(QunatumTime)
# admin.site.register(FacultyQueryManagement)
# admin.site.register(StudentQueryManagement)
admin.site.register(UserQueue)
admin.site.site_header = "Query Management System"
admin.site.site_title = "Round Robin"
admin.site.index_title = "Welcome Mr. Nitish Kumar"