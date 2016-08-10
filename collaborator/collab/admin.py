from django.contrib import admin

from .models import Action, Position, Student, Project

class ActionAdmin(admin.ModelAdmin):
    pass

class PositionAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Action, PositionAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Project, ProjectAdmin)
