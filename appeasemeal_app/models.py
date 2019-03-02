from django.db import models


# Create your models here.


class Family(models.Model):

    # Fields
    familyName = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ('-pk',)


class FamilyMembers(models.Model):

    # Fields
    Admin = models.BooleanField()
    Name = models.CharField(max_length=30)
    Email = models.EmailField()

    # Relationship Fields
    familyName = models.ForeignKey(
        'Family',
        on_delete=models.CASCADE, related_name="users",
    )

    class Meta:
        ordering = ('-pk',)