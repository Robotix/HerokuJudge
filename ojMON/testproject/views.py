# import cv2
import os, subprocess, Image
from django.http import *
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth, messages
from django.contrib.auth import logout as auth_logout
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from solutions.models import sol

def homePage(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/landingPage/')
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('index.html',
                             context_instance=context)

def landingPage(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('landing.html',
                            context_instance=context)

def raid1(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('problem1.html',
                            context_instance=context)


# def raid2(request):
#     return render_to_response('raid2.html')

def submit(request):
    if request.method == "POST":
        
        dir_work = os.path.dirname(os.path.dirname(__file__))

        build_cmd = {
            "c": 'gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE',
            "cpp": 'g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main',
            "java": 'javac Main.java',
            "python2": 'python2 -m py_compile main.py',
        }

        if request.POST['lang'] not in build_cmd.keys():
            return HttpResponse("Failure in lang")

        print request.POST['lang']

        if request.POST['lang']=='c':
            f = open("main.c", "w")
        if request.POST['lang']=='cpp':
            f = open("main.cpp", "w")
        if request.POST['lang']=='java':
            f = open("Main.java", "w")
        if request.POST['lang']=='python2':
            f = open("main.py", "w")
        
        f.write(request.POST['source'])
        f.close()

        print "written"

        p = subprocess.Popen(
            build_cmd[request.POST['lang']],
            shell=True,
            # cwd=dir_work,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        err, out = p.communicate()

        print "compiled"

        print out;
        if p.returncode != 0: 
            return HttpResponse(out)

        queries = raid1_sim(request.POST['lang'])
        print "queries = " + str(queries)
        if queries==0:
            return HttpResponse("Failure in sim")
        else:
            p = sol(solution=request.POST["source"],lang=request.POST['lang'],email=request.user.email,queries=queries)
            p.save()
            return HttpResponse("queries = " + str(queries))
    return HttpResponse("Failure in post")


def raid1_sim(language):
    
    dir_work = os.path.dirname(os.path.dirname(__file__))

    img = Image.open("raid1_test.jpg")
    pix = img.load()

    count = 0
    
    run_cmd = {
        "c": "./main",
        "cpp": "./main",
        "java": "java -cp Main",
        "python2": "python2 %s main.pyc",
    }

    p = subprocess.Popen(
        run_cmd[language],
        shell=False,
        cwd=dir_work,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)

    print img.size[0]
    print img.size[1]
    p.stdin.write("%d\n" % (img.size[0]))
    p.stdin.flush()

    while True:
        if p.poll() != None:
            break
        
        try:
            x,y = p.stdout.readline().split()

        except ValueError:
            if p.poll() != None:
                break
            else:    
                return 0

        if pix[int(x),int(y)]>200:
            p.stdin.write("YES\n")

        else:
            p.stdin.write("NO\n")
        
        p.stdin.flush()
        count = count + 1

    return count

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')