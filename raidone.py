import os
import sys
import subprocess

import cv2
import numpy as np


def main():
    img = cv2.imread('raid1_test.jpg', cv2.IMREAD_GRAYSCALE)
    counter_img = img.copy()

    LANG = sys.stdin.readline().rstrip()
    FILE = sys.stdin.readline().rstrip()

    query = 0
    correct_query = 0
    bunker = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[0]):
            if img[i, j] == 255:
                bunker += 1

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
        stdin=subprocess.PIPE
    )
    p.stdin.write("%d\n" % (img.shape[0]))
    p.stdin.write("%d\n" % (bunker))
    p.stdin.flush()

    while True:
        if p.poll() != None:
            # Participant killed the program
            break
        try:
            x, y = p.stdout.readline().split()
            x = int(x)
            y = int(y)
        except ValueError:
            if p.poll() != None:
                # Participant killed the program
                break
            else:
                # Deadlock!
                print 'We faced a deadlock while evaluating your queries'
                sys.exit()

        if x >= img.shape[0] or y >= img.shape[0]:
            print 'Incorrect query! ',
            print 'You queried for %d %d in a %d sized grid'\
                % (x, y, img.shape[0])
            sys.exit()
        if img[x, y] == 255:
            if counter_img[x, y] == 255:
                counter_img[x, y] = 0
                correct_query += 1
            p.stdin.write("YES\n")
        else:
            p.stdin.write("NO\n")
        query += 1

    if correct_query >= bunker:
        print 'Yay! You successfully bombed all the bunkers. ',
        print 'You bombed %d bunker cells with %d queries' % (bunker, query)
        print int(query)
    else:
        print 'You bombed %d bunker cells out of %d. You sent %d queries' \
            % (correct_query, bunker, query)

if __name__ == '__main__':
    main()
