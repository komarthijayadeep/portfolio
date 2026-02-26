from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated technologies")
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    date_issued = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    link = models.URLField(blank=True, help_text="Link to the certificate credential")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.issuer}"

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('skill', 'Core Skill'),
        ('tool', 'Tool'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='skill')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Training(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
