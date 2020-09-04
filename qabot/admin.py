from django.contrib import admin

# Register your models here.

from .models import FQA, SimilarQuestion


class FQAAdmin(admin.ModelAdmin):
    list_display = ['question', 'html_answer', 'valid']
    empty_value_display = 'Unknown Item field'
    list_per_page = 15
    search_fields = ['question', 'answer']
    list_filter = ['valid']


class SimilarQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'fqa']
    empty_value_display = 'Unknown Item field'
    list_per_page = 15


admin.site.register(FQA, FQAAdmin)
admin.site.register(SimilarQuestion, SimilarQuestionAdmin)
