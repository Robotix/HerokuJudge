from django.shortcuts import render, get_object_or_404
from submission.models import Submission
from django.template import RequestContext
from django.http import Http404

# Create your views here.

def submission(request, uniqueID):
	if not request.user.is_authenticated():
		raise Http404
	submissionObject = get_object_or_404(Submission, id= int(uniqueID))
	if request.user.username != submissionObject.user:
		if request.user.username != 'admin':
			raise Http404

	if submissionObject.stat == 'Safe for compilation' or submissionObject.stat == 'Compiled successfully':
		if submissionObject.compile():
			submissionObject.simulate()
	return render(request, 'submission/submission.html', 
		{'id': submissionObject.id,
		'source': submissionObject.source,
		'problem': submissionObject.problem,
		'language': submissionObject.language,
		'status': submissionObject.stat,
		'queries': submissionObject.queries,
		'cpu': submissionObject.cpu,
		'memory': submissionObject.memory})

