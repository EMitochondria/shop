from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=60, decimal_places=2, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Картинка',
        upload_to='product/',
        blank=True
    )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
