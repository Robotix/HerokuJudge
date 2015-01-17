import os, sys, subprocess, cv2, math
import numpy as np

def main():
    full_img = cv2.imread('raid2_test.jpg',1)                               #TestImage
    query_img = np.zeros((600,800,3), np.uint8)                                   

    sys.stdin.readline()                                            # Language:
    LANG = sys.stdin.readline().rstrip()
    
    sys.stdin.readline()                                            # Executable:
    FILE = sys.stdin.readline().rstrip()

    sys.stdin.readline()                                          # Army R C and resource:
    
    start_position = {
        'R': int(sys.stdin.readline()),
        'C': int(sys.stdin.readline()),
    }
    army = {                                        
        'R': start_position['R'],
        'C': start_position['C'],
        'resource': int(sys.stdin.readline()),
    }
    
    sys.stdin.readline()                                            # Number of enemies:
    enemy_count = int(sys.stdin.readline())

    sys.stdin.readline()                                            # Enemies R C and resource:
    enemy = {}
    for i in range(enemy_count):
        enemy[i] = {
            'R': int(sys.stdin.readline()), 
            'C': int(sys.stdin.readline()),
            'resource': int(sys.stdin.readline()),
            'alive': True,
        }

    sys.stdin.readline()                                            # Travel Cost Army Spy:
    travel_cost = {
        'army': float(sys.stdin.readline()),
        'spy': float(sys.stdin.readline()),
    }

    # Initializing SPY status
    sys.stdin.readline()                                            # Spy Assign Cost:
    spy = {                                                        
        'alive': False,
        'R': army['R'],
        'C': army['C'],
        'assign_cost': int(sys.stdin.readline()),
    }

    # Constants
    r2r_ratio = 250                                                  # Resource to radius ratio
    discover_radius = 20
    iterate_dist = 10

    # Uncover area around army
    cv2.circle(
        img= query_img, 
        center= (army['C'], army['R']), 
        radius= int(1.5*army['resource']/r2r_ratio),
        color= [255,255,255], 
        thickness=-1,
        lineType=8,
        shift=0)
    
    participant_image = np.bitwise_and(query_img, full_img)

    #Draw army circle
    cv2.circle(
        img= participant_image, 
        center= (army['C'], army['R']), 
        radius= army['resource']/r2r_ratio,
        color= [255,255,255], 
        thickness=-1,
        lineType=8,
        shift=0)

    cv2.imwrite('image.jpg', participant_image)
    # cv2.imshow('Participant', participant_image)
    # cv2.waitKey(10)

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
        if enemy_count == 0:
            army['resource'] -= int(math.sqrt((army['R']-start_position['R'])**2 + (army['C']-start_position['C'])**2)*travel_cost['army'])
            print 'Yay! You emerged victorius with %d resources left' %(army['resource'])
            print str(int(army['resource']))
            sys.exit()
        if p.poll() != None:            #Participant killed the program
            break
    
        input = p.stdout.readline()

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
            r = float(r)
            c = float(c)

            distance = math.sqrt((r - spy['R'])**2 + (c - spy['C'])**2)
            if(abs(r - spy['R']) < iterate_dist/2):
                dr = 0
                if c > spy['C']:
                    dc = iterate_dist
                else:
                    dc = -iterate_dist
            elif(abs(c - spy['C']) < iterate_dist/2):
                dc = 0
                if r > spy['R']:
                    dr = iterate_dist
                else:
                    dr = -iterate_dist
            else:
                dr = (r - spy['R'])*iterate_dist/distance
                dc = (c - spy['C'])*iterate_dist/distance            
            
            while abs(r-spy['R']) > iterate_dist or abs(c-spy['C']) > iterate_dist:
                if spy['alive'] is False:
                    break
                spy['R'] += dr
                spy['C'] += dc
                cv2.circle(
                    img= query_img,
                    center= (int(spy['C']), int(spy['R'])), 
                    radius= discover_radius,
                    color= [255,255,255], 
                    thickness=-1,
                    lineType=8,
                    shift=0)

                for i in enemy:
                    if enemy[i]['alive'] is True:
                        if math.sqrt((enemy[i]['R'] - spy['R'])**2 + (enemy[i]['C'] - spy['C'])**2) < discover_radius:
                            spy['alive'] = False
                            p.stdin.write('Spy_killed\n')
                            p.stdin.flush()
                            break                           

                army['resource'] -= math.sqrt((dr)**2 + (dc)**2)*travel_cost['spy']
                # cv2.imshow('Participant', query_img)
                # cv2.waitKey(10)

            if spy['alive'] is True:
                spy['R'] = int(r)
                spy['C'] = int(c)
                p.stdin.write("DONE\n")
                p.stdin.flush()

        elif input.find('MOVE ARMY') >= 0:
            r,c = p.stdout.readline().split()
            r = float(r)
            c = float(c)
            distance = math.sqrt((r - army['R'])**2 + (c - army['C'])**2)
            if(abs(r - army['R']) < iterate_dist/2):
                dr = 0
                if c > army['C']:
                    dc = iterate_dist
                else:
                    dc = -iterate_dist
            elif(abs(c - army['C']) < iterate_dist/2):
                dc = 0
                if r > army['R']:
                    dr = iterate_dist
                else:
                    dr = -iterate_dist
            else:
                dr = (r - army['R'])*iterate_dist/distance
                dc = (c - army['C'])*iterate_dist/distance    
            
            radius_army = int(1.5*army['resource']/r2r_ratio)

            while abs(r-army['R']) > iterate_dist or abs(c-army['C']) > iterate_dist:
                army['R'] += dr
                army['C'] += dc
                cv2.circle(
                    img= query_img,
                    center= (int(army['C']), int(army['R'])), 
                    radius= radius_army,
                    color= [255,255,255], 
                    thickness=-1,
                    lineType=8,
                    shift=0)

                for i in enemy:
                    if enemy[i]['alive'] is True:
                        if math.sqrt((enemy[i]['R'] - army['R'])**2 + (enemy[i]['C'] - army['C'])**2) < radius_army:
                            if army['resource'] >= enemy[i]['resource']:
                                enemy[i]['alive'] = False
                                enemy_count -= 1
                                army['resource'] += enemy[i]['resource']/2
                            else:
                                print 'You failed in your conquest to win over the world. Your resources (%d) was no match against your opponents (%d)' %(army['resource'], enemy[i]['resource'])
                                sys.exit()

                army['resource'] -= int(math.sqrt((dr)**2 + (dc)**2))*travel_cost['army']
                
                if army['resource'] <=10:
                    print 'You wasted all your resources in travelling without fighting wars'
                    sys.exit()
                # cv2.imshow('Participant', query_img)
                # cv2.waitKey(10)


            army['R'] = int(r)
            army['C'] = int(c)
            p.stdin.write("DONE\n")
            p.stdin.flush()

        elif input.find('SNAPSHOT') >= 0:

            participant_image = cv2.bitwise_and(query_img,full_img)
            
            #Draw army circle
            cv2.circle(
                img= participant_image, 
                center= (army['C'], army['R']), 
                radius= int(army['resource']/r2r_ratio),
                color= [255,255,255], 
                thickness=-1, 
                lineType=8, 
                shift=0)

            # Draw enemy circles
            for i in enemy:
                if enemy[i]['alive'] is True:
                    colour = full_img[enemy[i]['R']+enemy[i]['resource']/r2r_ratio+2,enemy[i]['C']+enemy[i]['resource']/r2r_ratio+2]
                    colour = (255,255,255) - colour
                    cv2.circle(
                        img= participant_image, 
                        center= (enemy[i]['C'], enemy[i]['R']), 
                        radius= int(enemy[i]['resource']/r2r_ratio),
                        color= colour,
                        thickness=-1, 
                        lineType=8, 
                        shift=0)

            participant_image = cv2.bitwise_and(query_img,participant_image)
            
            cv2.imwrite('image.jpg',participant_image)
            p.stdin.write("DONE\n")
            p.stdin.flush()
        
        # cv2.imshow('Participant', participant_image)    
        # cv2.waitKey(500)

if __name__ == '__main__': 
    main()