import os, subprocess, Image
from django.http import *
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth, messages
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from solutions.models import sol
from testResults.models import testResults

def result(request):
    f = open("result.txt","r")
    return HttpResponse(f,content_type='text/plain; charset=utf8')

def status_false(request):
    f = open("error.txt","r")
    return HttpResponse(f,content_type='text/plain; charset=utf8')

def homePage(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('code_1.html',
                             context_instance=context)

def landingPage(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('landcode.html',
                            context_instance=context)

def submit(request):
    if request.method == 'GET':
        str=request.GET["source"]
        p = sol(solution=request.GET["source"],lang=request.GET['lang'],prob=request.GET["prob"],team_id=request.GET["team"])
        p.save()
        if compile(p.id) == True:
            # if raid1_sim(p.lang)==True:
            #     return HttpResponseRedirect('/result/')
            if dummy_tester(p.id) == True:
                return HttpResponse("Successful submission. Matched with test result")
            else:
                return HttpResponse("Failure I/O")
        else:
            p.delete()
            return HttpResponseRedirect('/status/fail')
    raise Http404

def compile(num):
    
    dir_work = os.path.dirname(os.path.dirname(__file__))
    language = sol.objects.get(id=num).lang
    
    if language=="C":
        f = open("main.c", "w")
    elif language=="C++":
        f = open("main.cpp", "w")
    elif language=="JAVA":
        f = open("Main.java", "w")
    
    f.write(sol.objects.get(id=num).solution)
    f.close()
    
    build_cmd = {
        "C": "gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "C++": "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "JAVA": "javac Main.java",
        # "python2": 'python2 -m py_compile main.py',
        # "python3": 'python3 -m py_compile main.py',
    }
    if language not in build_cmd.keys():
        return False
    p = subprocess.Popen(
        build_cmd[language],
        shell=True,
        cwd=dir_work,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    err, out = p.communicate()
    f = file("error.txt", "w")
    f.write(err)
    f.close()
    if p.returncode == 0: 
        return True
    return False

def raid1_sim(language):
    
    img = Image.open("raid1_test.jpg")
    pix = img.load()

    count = 0
    
    result = open("result.txt", "w")
    
    run_cmd = {
        "C": "./main",
        "C++": "./main",
        "JAVA": "java -cp Main"
    }

    p = subprocess.Popen(
        run_cmd[language],
        shell=False,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)

    while True:
        if p.poll() != None:
            break
        
        try:
            x,y = p.stdout.readline().split()

        except ValueError:
            if p.poll() != None:
                break
            else:    
                return False

        if pix[int(x),int(y)]>200:
            p.stdin.write("YES\n")

        else:
            p.stdin.write("NO\n")
        
        p.stdin.flush()
        count = count +1

    result.write(str(count))
    result.close()
    return True

def dummy_tester(num):

    m=sol.objects.get(id=num)
    language = m.lang
    
    run_cmd = {
        "C": "./main",
        "C++": "./main",
        "JAVA": "java -cp Main"
    }

    p = subprocess.Popen(
        run_cmd[language],
        shell=False,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)

    result = p.communicate()[0]
    m.stdout=result.strip()
    m.save()

    for i in testResults.objects.all():
        if m.stdout==i.solution:
            return True
    return False