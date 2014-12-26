from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def myAccountPage(request):
	return HttpResponseRedirect(reverse('users:AccountPage', args=[request.user.username]))

def AccountPage(request, user_name):
	requestedUser = get_object_or_404(User, username= user_name)

	return render(request, 'users/my_account.html', {
		'name': requestedUser.get_full_name(),
		'username': requestedUser.username,
		'email': requestedUser.email,
		})