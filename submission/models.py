from django.db import models

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
                print 'found system'
                return False
            print 'not found'
            return True

    def compile(self):

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
            build_cmd[self.language]+str(self.id)+FILE_NAME[self.language],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        error, out = buildProcess.communicate()

        if buildProcess.returncode != 0: 
            self.stat = 'Compilation error:\n', out
        else:
            self.stat = 'Compiled successfully'
        os.remove()
