import os, sys, subprocess, cv2
import numpy as np

def main():
    img = cv2.imread('raid1_test.jpg',cv2.IMREAD_GRAYSCALE)         #TestImage
    counter_img = img.copy()                                        #Counting unique queries

    LANG = sys.stdin.readline().rstrip()
    FILE = sys.stdin.readline().rstrip()

    query_count = 0
    correct_query_count = 0  
    bunker_count = 0

    for i in range(0,img.shape[0]-1):                               #To get this through textfile
        for j in range(0,img.shape[0]-1):
            if img[i,j]==255:
                bunker_count += 1

    # print 'Bunkers %d' %bunker_count

    RUN_CMD = {
        'c': './',
        'cpp': './',
        # 'java': 'javac ./Main.java',
        'python2': 'python2 ./',
        'python3': 'python3 ./',
    }
    
    p = subprocess.Popen(
       RUN_CMD[LANG]+FILE,
        shell=False,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)  

    p.stdin.write("%d\n" % (img.shape[0]))                          #Print n
    p.stdin.write("%d\n" % (bunker_count))                          #Print m
    p.stdin.flush()

    while True:
        if p.poll() != None:            #Participant killed the program
            break
    
        try:
            x,y = p.stdout.readline().split()
            x = int(x)
            y = int(y)
        except ValueError:
            if p.poll() != None:        #Participant killed the program
                break
            else:                       #Deadlock!
                print 'We faced a deadlock while evaluating your queries'
                sys.exit()

        if x>= img.shape[0] or y>=img.shape[0]:
            print 'Incorrect query! You queried for %d %d in a %d sized grid' %x %y %img.shape[0]
            sys.exit()
        if img[x,y]==255:
            if counter_img[x,y]==255:
                counter_img[x,y]=0
                correct_query_count += 1
            p.stdin.write("YES\n")
        else:
            p.stdin.write("NO\n")
        query_count += 1

    # print 'correct= %d total= %d' %(correct_query_count, query_count)
    if correct_query_count >= bunker_count:
        print 'Yay! You successfully bombed all the bunkers. You bombed %d bunker cells with %d queries' %(bunker_count, query_count)
        print int(query_count)
    else:
        print 'You could only bomb %d bunker cells out of %d bunker cells. You sent %d queries' %(correct_query_count, bunker_count, query_count)

if __name__ == '__main__': 
    main()