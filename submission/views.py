from django.shortcuts import render, get_object_or_404
from submission.models import Submission
from django.template import RequestContext
from django.http import Http404

# Create your views here.

def submission(request, uniqueID):
	if not request.user.is_authenticated():
		raise Http404
	print uniqueID
	submissionObject = get_object_or_404(Submission, id= int(uniqueID))
	if request.user.email != submissionObject.user:
		if request.user.email != 'narayanaditya95@gmail.com':
			raise Http404
	return render(request, 'submission/submission.html', 
		{'id': submissionObject.id,
		'source': submissionObject.source,
		'language': submissionObject.language,
		'status': submissionObject.stat})

