from django.contrib import admin
from courses.models import Category, Course, Lesson
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import (CKEditorUploadingWidget)
# Register your models here.

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)


class Meta:
    model = Lesson
    fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    list_display = ['id','subject','active','created_at']
    list_filter = ['subject','id']
    readonly_fields = ['avatar']
    forms = LessonForm

    def avatar(self, lesson):
        return mark_safe(f"<img src ='/static/{lesson.image.name}' width = '200'/>")

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
