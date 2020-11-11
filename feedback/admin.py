from django.contrib import admin
from feedback.models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_feedback', )

admin.site.register(Feedback, FeedbackAdmin)