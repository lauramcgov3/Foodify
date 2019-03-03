from django import forms
from .models import Family, FamilyMembers


class FamilyForm(forms.ModelForm):

    familyName = forms.CharField()

    class Meta:
        model = Family
        fields = ('familyName',)


class MemberForm(forms.ModelForm):

    yesOrNo = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    Admin = forms.ChoiceField(choices=yesOrNo)
    Name = forms.CharField()
    Email = forms.EmailField()
    familyName = forms.CharField()

    class Meta:
        model = FamilyMembers
        fields = ('Admin', 'Name', 'Email', 'familyName')

