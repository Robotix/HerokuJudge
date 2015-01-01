from django.shortcuts import resolve_url, render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from submission.models import Submission
from django.http import Http404
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'sudocode/index.html', {})

def dashboard(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'sudocode/dashboard.html', {
        'user': request.user.username,
        })

def theraidone(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'sudocode/theraidone.html',{})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def submit(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        submissionObject = Submission(
            user= request.user.email,
            problem= request.POST['problem'],
            source= request.POST['source'],
            language= request.POST['lang'],
            stat= '',
            queries= 2500,
            cpu= 05.000,
            memory= 999.99,)
        if submissionObject.checkSafe() is True:
            submissionObject.stat= 'Safe for compilation'
            submissionObject.save()
            return HttpResponseRedirect(reverse('status', args=[submissionObject.id]))
        else:
            submissionObject.stat= 'Library Import Error'
            submissionObject.save()
            return HttpResponseRedirect(reverse('status', args=[0]))
    else:
        raise Http404

def status(request, uniqueID):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    try:
        submissionObject= Submission.objects.get(id= uniqueID)
        return render(request, 'sudocode/post_submit.html', {
            'result': 'true',
            'id': uniqueID,
            })
    except:
        return render(request, 'sudocode/post_submit.html', {
            'result': 'false',
            'id': 0,
            })