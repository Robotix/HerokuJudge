from django.shortcuts import render, get_object_or_404
from submission.models import Submission
from django.template import RequestContext
from django.http import Http404

# Create your views here.

def submission(request, uniqueID):
	if not request.user.is_authenticated():
		raise Http404
	submissionObject = get_object_or_404(Submission, id= int(uniqueID))
	if request.user.email != submissionObject.user:
		if request.user.email != 'aditya.narayan@robotix.in':
			raise Http404
	# if submissionObject.stat == 'Safe for compilation':
	if True:
		if submissionObject.raidone_compile():
			submissionObject.raidone_simulate()
	return render(request, 'submission/submission.html', 
		{'id': submissionObject.id,
		'source': submissionObject.source,
		'language': submissionObject.language,
		'status': submissionObject.stat,
		'queries': submissionObject.queries,
		'cpu': submissionObject.cpu,
		'memory': submissionObject.memory})

