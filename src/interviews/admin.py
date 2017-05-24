from django.contrib import admin

from .models import Interview


class InterviewModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'updated']
    list_filter = ['publish', 'updated', 'timestamp']
    search_fields = ['title', 'content', 'interviewee']

    class Meta:
        model = Interview


admin.site.register(Interview, InterviewModelAdmin)
