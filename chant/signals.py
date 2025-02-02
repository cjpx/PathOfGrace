from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Song, Category

@receiver(pre_save, sender=Song)
def handle_categories(sender, instance, **kwargs):
    if hasattr(instance, "category_names"):
        for category_name in instance.category_names:
            #Get or create Category
            category, created = Category.objects.get_or_create(name = category_name)
            instance.categories.add(category)