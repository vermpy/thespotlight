from django.contrib import admin

from .forms import InterviewModelForm
from .models import Interview


class InterviewModelAdmin(admin.ModelAdmin):
    form = InterviewModelForm
    change_form_template = 'interviews/admin/change_form.html'
    list_display = ['title', 'publish', 'updated']
    list_filter = ['publish', 'updated', 'timestamp']
    search_fields = ['title', 'content', 'interviewee']


admin.site.register(Interview, InterviewModelAdmin)
