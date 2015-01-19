from django.db import models
from django.conf import settings
from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from django.utils.translation import ugettext_lazy as _

# Create your models here.

YEAR_CHOICES = (
    (2015,'2015'),
    (2016,'2016'), 
    (2017,'2017'), 
    (2018,'2018'),
    (2019,'2019'),
)

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    firstName = models.CharField(max_length=50, blank= False)
    lastName = models.CharField(max_length=50, blank=False)
    mobileNo = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        blank=False)
    graduation_year = models.IntegerField(blank=False, choices=YEAR_CHOICES)
    college = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return 'Participant-' + str(self.id)

class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields= '__all__'
        labels = {
            'firstName': _('First Name'),
            'lastName': _('Last Name'),
            'mobileNo': _('Mobile Number'),
            'graduation_year': _('Year of Graduation'),
            'college': _('College'),
        }
        widgets = {
            'firstName': TextInput(attrs={'required':'True', 'size':'50'}),
            'lastName': TextInput(attrs={'required':'True', 'size':'50'}),
            'mobileNo': TextInput(attrs={'required':'True', 'maxlength':'10', 'size':'50'}),
            'college': TextInput(attrs={'required':'True', 'size':'50'}),
        }