from django.db import models


# Create your models here.


class Family(models.Model):

    # Fields
    familyName = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ('-pk',)


class FamilyMembers(models.Model):

    yesOrNo = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    # Fields
    Admin = models.CharField(max_length=3, choices=yesOrNo)
    Name = models.CharField(max_length=30)
    Email = models.EmailField()

    # Relationship Fields
    familyName = models.ForeignKey(
        'Family',
        on_delete=models.CASCADE, related_name="familyMembers",
    )


    class Meta:
        ordering = ('-pk',)
