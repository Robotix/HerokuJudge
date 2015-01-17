from django.db import models
import os, subprocess
from decimal import *
import lorun

# Create your models here.

class Submission(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    problem = models.IntegerField()
    source = models.TextField()
    language = models.CharField(max_length=4)
    stat = models.TextField()
    queries =models.IntegerField()
    cpu = models.DecimalField(max_digits=5, decimal_places=3)
    memory = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):       
      return str(self.id)

    def checkSafe(self):

        if self.language in ['python2', 'python3']:
            
            support_modules = [
                're', 
                'sys', 
                'string', 
                'scanf',
                'math',
                'cmath',
                'decimal',
                'numbers', 
                'fractions',
                'random', 
                'itertools',
                'functools',
                'operator',
                'readline',
                'json',
                'array',
                'sets',
                'queue',
                'types',
            ]
            
            for line in self.source:
            
                if line.find('import') >= 0:
            
                    words = line.split()
                    tag = 0
            
                    for w in words:
        
                        if w in support_modules:
                            tag = 1
                            break
        
                    if tag == 0:
                        return False
        
            return True
        
        if self.language in ['c', 'cpp']:
        
            if self.source.find('system') >= 0:
                return False
            return True

    def compile(self):
        if self.language == 1:
            return self.raidone_compile()
        else:
            return self.raidtwo_compile()

    def simulate(self):
        if self.language == 1:
            self.raidone_simulate()
        else:
            self.raidtwo_simulate()

    def raidone_compile(self):

        BUILD_CMD = {
            'c': 'gcc -o main -Wall -lm -O2 -std=c99 --static ./',
            'cpp': 'g++ -O2 -Wall -lm --static  -o main ./',
            # 'cpp':'g++ -o main `pkg-config opencv --cflags` `pkg-config opencv --libs` ./',
            # 'java': 'javac ./Main.java',
            'python2': 'python2 -m py_compile ./',
            'python3': 'python3 -m py_compile ./',
        }

        FILE_NAME = {
            'c': 'main.c',
            'cpp': 'main.cpp',
            # 'java': 'Main,java',
            'python2': 'main.py',
            'python3': 'main.py',
        }

        fileObject = open(str(self.id)+FILE_NAME[self.language], 'w')
        fileObject.write(self.source)
        fileObject.close()
            
        buildProcess = subprocess.Popen(
            BUILD_CMD[self.language]+str(self.id)+FILE_NAME[self.language],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        error, out = buildProcess.communicate()

        if buildProcess.returncode != 0: 
            self.stat = 'Compilation error:\n', out
            self.save()
            return False
        else:
            self.stat = 'Compiled successfully'
            self.save()
            return True

    def raidtwo_compile(self):

        FILE_NAME = {
            'c': 'main.c',
            'cpp': 'main.cpp',
            # 'java': 'Main,java',
            'python2': 'main.py',
            'python3': 'main.py',
        }

        SOURCE_FILE = str(self.id)+FILE_NAME[self.language]

        fileObject = open(SOURCE_FILE, 'w')
        fileObject.write(self.source)
        fileObject.close()
        
        fileObject = open('CMakeLists.txt', 'w')
        fileObject.write('cmake_minimum_required(VERSION 2.8)\n' +
            'project( main )\n' +
            'find_package( OpenCV REQUIRED )\n' +
            'add_executable( main %s )\n' %(SOURCE_FILE) +
            'target_link_libraries( main ${OpenCV_LIBS} )\n')
        fileObject.close()

        buildProcess = subprocess.Popen(
            'cmake .',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        error, out = buildProcess.communicate()

        if buildProcess.returncode != 0: 
            self.stat = 'Compilation error:\n', out
            self.save()
            return False
        
        buildProcess = subprocess.Popen(
            'make',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        error, out = buildProcess.communicate()

        if buildProcess.returncode != 0: 
            self.stat = 'Compilation error:\n', out
            self.save()
            return False
        else:
            self.stat = 'Compiled successfully'
            self.save()
            return True

    def raidone_simulate(self):

        fin = open('input.in', 'w')
        ftemp = open('output.out', 'w')
        
        EXEC_NAME = {
            'c': 'main',
            'cpp': 'main',
            # 'java': 'Main,java',
            'python2': 'main.py',
            'python3': 'main.py',
        }
        fin.write('%s\n%s\n' %(self.language, EXEC_NAME[self.language]))
        fin.close
        fin = open('input.in')

        runcfg = {
            'args':['python','raidone.py'],
            'fd_in':fin.fileno(),
            'fd_out':ftemp.fileno(),
            'timelimit':10000, #in MS
            'memorylimit':200000, #in KB
        }
        
        JUDGE_RESULT ={
            '0': 'Accepted',   
            '1': 'Presentation Error',
            '2': 'Time Limit Exceeded',
            '3': 'Memory Limit Exceeded',
            '4': 'Wrong Answer',
            '5': 'Runtime Error',
            '6': 'Output Limit Exceeded',
            '7': 'Compile Error',
            '8': 'System Error',
        }
        
        rst = lorun.run(runcfg)

        print rst 
        
        fin.close()
        ftemp.close()
        ftemp = open('output.out')

        if rst['result'] == 0:
            self.stat = ftemp.readline()
            self.cpu = Decimal(float(rst['timeused'])/1000).quantize(Decimal('.001'), rounding=ROUND_UP)
            self.memory = Decimal(float(rst['memoryused'])/1000).quantize(Decimal('.01'), rounding=ROUND_UP)
            if self.stat.find('Yay!')>=0:
                self.queries = int(ftemp.readline())
            else:
                self.queries = 9999
            self.save()
            ftemp.close()
        else:
            self.queries = 9999
            self.cpu = 99.999
            self.memory = 999.99
            self.stat = JUDGE_RESULT[str(rst['result'])]
            self.save()
            ftemp.close()

    def raidtwo_simulate(self):

        fin = open('input.in', 'w')
        ftemp = open('output.out', 'w')
        
        EXEC_NAME = {
            'c': 'main',
            'cpp': 'main',
            # 'java': 'Main,java',
            'python2': 'main.py',
            'python3': 'main.py',
        }

        fin.write('Language:\n' +
                '%s\n' %(self.language) +
                'Executable:\n' +
                'main\n' +
                'Army R C and resource:\n' +
                '100\n' +
                '70\n' +
                '7500\n' +
                'Number of enemies:\n' +
                '5\n' +
                'Enemies R C and resource:\n' +
                '125\n' +
                '400\n' +
                '5000\n' +
                '120\n' +
                '667\n' +
                '5000\n' +
                '290 \n' +
                '675 \n' +
                '4000\n' +
                '375\n' +
                '485\n' +
                '4000\n' +
                '438\n' +
                '62\n' +
                '5000\n' +
                'Travel Cost Army Spy:\n' +
                '0.5\n' +
                '0.01\n' +
                'Spy Assign Cost:\n' +
                '10\n')
        fin.close
        fin = open('input.in')

        runcfg = {
            'args':['python','raidtwo.py'],
            'fd_in':fin.fileno(),
            'fd_out':ftemp.fileno(),
            'timelimit':5000, #in MS
            'memorylimit':500000, #in KB
        }
        
        JUDGE_RESULT ={
            '0': 'Accepted',   
            '1': 'Presentation Error',
            '2': 'Time Limit Exceeded',
            '3': 'Memory Limit Exceeded',
            '4': 'Wrong Answer',
            '5': 'Runtime Error',
            '6': 'Output Limit Exceeded',
            '7': 'Compile Error',
            '8': 'System Error',
        }
        
        rst = lorun.run(runcfg)

        print rst 
        
        fin.close()
        ftemp.close()
        ftemp = open('output.out')

        if rst['result'] == 0:
            self.stat = ftemp.readline()
            self.cpu = Decimal(float(rst['timeused'])/1000).quantize(Decimal('.001'), rounding=ROUND_UP)
            self.memory = Decimal(float(rst['memoryused'])/1000).quantize(Decimal('.01'), rounding=ROUND_UP)
            if self.stat.find('Yay!')>=0:
                self.queries = int(ftemp.readline())
            else:
                self.queries = 9999
            self.save()
            ftemp.close()
        else:
            self.queries = 0
            self.cpu = 99.999
            self.memory = 999.99
            self.stat = JUDGE_RESULT[str(rst['result'])]
            self.save()
            ftemp.close()
