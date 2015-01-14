from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from participant.models import Participant, ParticipantForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('participant:register'))
    else:
        form = ParticipantForm()
    return render(request, 'participant/register.html', {'form': form})

def info(request, number):
	participant_object = get_object_or_404(Participant, id=number)
	