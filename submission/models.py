from django.db import models
import os, subprocess
import lorun

# Create your models here.

class Submission(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.EmailField(max_length=50)
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

    def raidone_compile(self):

        BUILD_CMD = {
            'c': 'gcc -o main -Wall -lm -O2 -std=c99 --static ./',
            'cpp': 'g++ -O2 -Wall -lm --static  -o main ./',
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
            # self.stat = 'Compiled successfully'
            self.save()
            return True

    def raidone_simulate(self):

        print 'opening input and output'
        fin = open('input.in')
        ftemp = open('output.out', 'w')
        
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
        print 'complete simulate'

        fin.close()
        ftemp.close()

        ftemp = open('output.out')
        if rst['result'] == 0:
            try:
                self.queries = int(ftemp.read())
                print 'read queries'
                self.cpu = rst['timeused']
                self.memory = rst['memoryused']
                print 'read cpu and memory'
                self.stat = 'Congratulations! Your submission ran successfully.'
                self.save()
                ftemp.close()
            except:
                self.stat = 'We faced a problem understanding your queries. Are your sure you have read the tutorial?'
                self.save()
                ftemp.close()
        else:
            self.queries = 99999
            self.cpu = 99999
            self.memory = 99999
            self.stat = 'Failed'
            self.save()
            ftemp.close()

