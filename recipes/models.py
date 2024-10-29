from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# choices Field
SERVES = (
    (2, "2"),
    (4, "4"),
    (6, "6"),
    (8, "8"),
    (10, "10"),
)


class Recipe(models.Model):
    """
    A model to create and manage recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(
        max_length=10000, null=False, blank=False, default="Instructions"
    )
    ingredients = RichTextField(
        max_length=10000, null=False, blank=False, default="Ingredients"
    )
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    prep_time = models.IntegerField(default="15")
    cook_time = models.IntegerField(default="40")
    serves = models.IntegerField(choices=SERVES, default="2")
    posted_date = models.DateTimeField(auto_now=True)
    lowsugar = models.BooleanField()
    glutenfree = models.BooleanField()
    dairyfree = models.BooleanField()
    vegan = models.BooleanField()
    vegitarian = models.BooleanField()
    highfiber = models.BooleanField()
    highprotein = models.BooleanField()
    nutfree = models.BooleanField()

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return str(self.title)
