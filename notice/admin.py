from django.contrib import admin
from . import models
from .models import Question

# Register your models here.


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = [
        "subject",
    ]
