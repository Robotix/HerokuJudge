import os, subprocess, cv2

img = cv2.imread('raid1_test.jpg',cv2.IMREAD_GRAYSCALE)

count = 0
bunkers = 0

for i in (0,img.shape[0]-1):
    for j in (0,img.shape[1]-1):
        if img[i,j]>200:
            bunkers= bunkers +1

p = subprocess.Popen(
    './main',
    shell=False,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE)

p.stdin.write("%d\n" % (img.shape[0]))
p.stdin.write("%d\n" % (bunkers))
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
            print 'Failure'
            break

    if img[int(x),int(y)]>200:
        p.stdin.write("YES\n")
        bunkers = bunkers-1
    else:
        p.stdin.write("NO\n")
        
    p.stdin.flush()
    count = count + 1
if bunkers == 0:
    print str(count)
else:
    print 'Failure'