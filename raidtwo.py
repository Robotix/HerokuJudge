import os, sys, subprocess, cv2, math
import numpy as np
from PIL import Image, ImageDraw, ImageMath

def main():
    full_img = cv2.imread('raid2_test.jpg',1)                               #TestImage
    query_img = Image.new('RGB', (800, 600), (0,0,0))                                    

    draw_query = ImageDraw.Draw(query_img)

    sys.stdin.readline()                                            # Language:
    LANG = sys.stdin.readline().rstrip()
    
    sys.stdin.readline()                                            # Executable:
    FILE = sys.stdin.readline().rstrip()

    sys.stdin.readline()                                            # Army R C and resource:
    army = {                                        
        'R': int(sys.stdin.readline()),
        'C': int(sys.stdin.readline()),
        'resource': int(sys.stdin.readline())}
    
    sys.stdin.readline()                                            # Number of enemies:
    enemy_count = int(sys.stdin.readline())

    sys.stdin.readline()                                            # Enemies R C and resource:
    enemy = {}
    for i in range(enemy_count):
        enemy[i] = {
            'R': int(sys.stdin.readline()), 
            'C': int(sys.stdin.readline()),
            'resource': int(sys.stdin.readline()),
            'alive': True}

    sys.stdin.readline()                                            # Travel Cost Army Spy:
    travel_cost = {
        'army': int(sys.stdin.readline()),
        'spy': int(sys.stdin.readline())}

    # Initializing SPY status
    sys.stdin.readline()                                            # Spy Assign Cost:
    spy = {                                                        
        'alive': False,
        'R': army['R'],
        'C': army['C'],
        'assign_cost': int(sys.stdin.readline())}

    # Uncover area around army
    r2r_ratio = 25                                                  # Resource to radius ratio
    
    draw_query.rectangle(
        xy= [(army['R']-40, army['C']-40), (army['R']+40, army['C']+40)],
        fill= (255,255,255))
    query_img.show()
    
    participant_image = np.array(query_img)
    participant_image = np.bitwise_and(participant_image, full_img)

    cv2.imshow('Query Rect', participant_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Draw army circle
    cv2.circle(
        img= participant_image, 
        center= (army['R'], army['C']), 
        radius= army['resource']/r2r_ratio,
        color= [255,255,255], 
        thickness=-1, 
        lineType=8, 
        shift=0)

    cv2.imwrite('image.jpg', participant_image)
    cv2.imshow('Participant', participant_image)
    cv2.waitKey(0)

    RUN_CMD = {
        'c': './',
        'cpp': './',
        'python2': 'python2 ./',
        'python3': 'python3 ./',
    }
    
    p = subprocess.Popen(
        RUN_CMD[LANG]+FILE,
        shell=False,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)  

    p.stdin.write("%d\n" % (army['resource']))
    p.stdin.write("%d\n" % (enemy_count))
    p.stdin.write("%d\n" % (spy['assign_cost']))                     
    p.stdin.write("%d %d\n" % (travel_cost['spy'], travel_cost['army']))
    p.stdin.flush()

    while True:
        if p.poll() != None:            #Participant killed the program
            break
    
        input = p.stdout.readline()
        print input

        if input.find('ABANDON SPY') >= 0:
            spy['alive'] = False
            p.stdin.write("DONE\n")
            p.stdin.flush()

        elif input.find('ASSIGN SPY') >= 0:
            if spy['alive'] is True:
                print 'You cannot assign more than one spy'
                sys.exit()
            spy['alive'] = True
            army['resource'] -= spy['assign_cost']
            spy['R'] = army['R']
            spy['C'] = army['C']
            p.stdin.write("DONE\n")
            p.stdin.flush()
            
        elif input.find('MOVE SPY') >= 0:
            r,c = p.stdout.readline().split()
            if spy['alive'] is False:
                print 'You tried moving a spy without assigning him'
                sys.exit()
            r = int(r)
            c = int(c)
            print r,c
            dist = int(math.sqrt((spy['R']-r)**2 + (spy['C']-c)**2))

            query_rect = [(army['R'] - 40*(r-army['R'])/dist, army['C'] + 40*(c-army['C'])/dist),
                          (r - 40*(r-army['R'])/dist, c + 40*(c-army['C'])/dist),
                          (r + 40*(r-army['R'])/dist, c + 40*(c-army['C'])/dist),
                          (army['R'] + 40*(r-army['R'])/dist, army['C'] + 40*(c-army['C'])/dist),]

            print query_rect

            draw_query.polygon(query_rect)
            query_img.show()
            participant_image = np.array(query_img)
            participant_image = np.bitwise_and(participant_image, full_img)

            cv2.imshow('Query Rect', participant_image)
            cv2.waitKey(0)

    #         p.stdin.write("DONE\n")
    #         p.stdin.flush()

    #     elif input.find('SNAPSHOT') >= 0:
    #         participant_image = cv2.bitwise_and(query_img,full_img)
            
    #         #Draw army circle
    #         cv2.circle(
    #             img= participant_image, 
    #             center= (army['R'], army['C']), 
    #             radius= army['resource']/r2r_ratio,
    #             color= [255,255,255], 
    #             thickness=-1, 
    #             lineType=8, 
    #             shift=0)

    #         cv2.imshow('Participant', participant_image)
    #         cv2.waitKey(0)
            
    #         cv2.imwrite('image.jpg',participant_image)
    #         p.stdin.write("DONE\n")
    #         p.stdin.flush()

    # cv2.imshow('Participant', participant_image)
    # cv2.waitKey(0)

    # # print 'correct= %d total= %d' %(correct_query_count, query_count)
    # if correct_query_count >= bunker_count:
    #     print 'Yay! You successfully bombed all the bunkers. You bombed %d bunkers with %d queries' %(bunker_count, query_count)
    #     print int(query_count)
    # else:
    #     print 'You could only bomb %d bunkers out of %d bunkers. You sent %d queries' %(correct_query_count, bunker_count, query_count)

if __name__ == '__main__': 
    main()