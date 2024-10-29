from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """form to create a recipe"""

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "prep_time",
            "cook_time",
            "serves",
            "lowsugar",
            "glutenfree",
            "dairyfree",
            "vegan",
            "vegitarian",
            "highfiber",
            "highprotein",
            "nutfree",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widgets = {"description": forms.Textarea(attrs={"rows": 5})}

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "prep_time": "Preparation Time",
            "cook_time": "Cooking Time",
            "serves": "Serves for (number)",
            "lowsugar": "Lowsugar",
            "glutenfree": "Gluten-Free",
            "dairyfree": "Dairy-Free",
            "vegan": "Vegan",
            "vegitarian": "Vegitarian",
            "highfiber": "High-fiber",
            "highprotein": "High-protein",
            "nutfree": "Nut-Free",
        }
