from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "instructions",
        "ingredients",
        "image",
        "lowsugar",
        "glutenfree",
        "dairyfree",
        "vegan",
        "vegitarian",
        "highfiber",
        "highprotein",
        "nutfree",
        "posted_date",
    )
