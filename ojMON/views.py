import os, subprocess, Image
from django.http import *
from django.shortcuts import render_to_response

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib import auth
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.csrf import csrf_exempt
# import MySQLdb

def result(request):
    raid1_sim()
    f = open("result.txt","r")
    return HttpResponse(f,content_type='text/plain; charset=utf8')

def status_false(request):
    f = open("error.txt","r")
    return HttpResponse(f,content_type='text/plain; charset=utf8')

def submitPage(request):
    return HttpResponse('home.html')

def submit(request):
    if request.method == 'GET':
        str = request.GET["source"]
        if request.GET["lang"]=="C":
            f = open("main.c", "w")
            f.write(str)
            f.close()
        if request.GET["lang"]=="C++":
            f = open("main.cpp", "w")
            f.write(str)
            f.close()
        if request.GET["lang"]=="JAVA":
            f = open("Main.java", "w")
            f.write(str)
            f.close()
        if compile(request.GET["lang"]) == True:
            return HttpResponseRedirect('/result')
        else:
            return HttpResponseRedirect('/status/fail')
    raise Http404

def compile(language):
    language = language.lower()
    dir_work = os.path.dirname(os.path.dirname(__file__))
    build_cmd = {
        "c": "gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
        "c++": "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "java": "javac Main.java",
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
    out, err = p.communicate()
    f = file("error.txt", "w")
    f.write(err)
    f.write(out)
    f.close()
    if p.returncode == 0: 
        return True
    return False

def raid1_sim():
    
    img = Image.open("raid1_test.jpg")
    pix = img.load()

    count = 0
    
    result = open("result.txt", "w")
    
    p = subprocess.Popen(
        "./main",
        shell=False,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)

    while True:
        if p.poll() != None:
            break
        
        x,y = p.stdout.readline().split()
        
        if pix[int(x),int(y)]>200:
            p.stdin.write("YES\n")

        else:
            p.stdin.write("NO\n")
        
        p.stdin.flush()
        count = count +1
        print count

    result.write(str(count))
    result.close()