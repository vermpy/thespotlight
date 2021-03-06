from django.contrib import admin

from interviews.forms import InterviewModelForm
from interviews.models import Interview


class InterviewModelAdmin(admin.ModelAdmin):
    form = InterviewModelForm
    change_form_template = 'interviews/admin/change_form.html'
    list_display = ['interviewee', 'title', 'publish', 'updated']
    list_filter = ['publish', 'updated', 'timestamp']
    search_fields = ['title', 'content', 'interviewee']


admin.site.register(Interview, InterviewModelAdmin)
