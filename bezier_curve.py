import time
import pygame, math, random

width, height = 1280, 720

def main():

    pygame.init()
    pygame.display.set_caption("Bezeir_curve")

    screenf = pygame.display.set_mode([width, height])

    game_run = True

    points = [[100,100],[200,100],[300,100]]
    points2 = []

    drag_dist = 25
    curr_drag = None

    p_r = drag_dist*0.75

    num_points = 1
    change = 1/num_points
    percent = 0

    last = time.time()

    while game_run:
        dtime = time.time()-last

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass

        if pygame.mouse.get_pressed()[0]:
            if curr_drag == None:
                for i,p in enumerate(points):
                    if math.dist(p, pygame.mouse.get_pos()) < drag_dist/2:
                        curr_drag = i
            else:
                points[curr_drag] = pygame.mouse.get_pos()
        elif curr_drag != None:
            curr_drag = None

        screenf.fill(0)

        pygame.draw.lines(screenf, (255,255,255), False, points, 2)
        if len(points2) > 1:
            pygame.draw.lines(screenf, (255,0,0), False, points2, 2)

        for p in points:
            pygame.draw.ellipse(screenf, (200,255,0), (p[0]-drag_dist/2, p[1]-drag_dist/2, drag_dist, drag_dist))

        bp1 = [((points[1][i]-x)*percent)+x for i,x in enumerate(points[0])]
        bp2 = [((points[2][i]-x)*percent)+x for i,x in enumerate(points[1])]
        bp3 = [((bp2[i]-x)*percent)+x for i,x in enumerate(bp1)]
        
        points2.append(bp3)
        percent += change*dtime

        pygame.draw.line(screenf, (255,0,255), bp1, bp2, 2)

        pygame.draw.ellipse(screenf, (0,255,0), (bp1[0]-p_r/2, bp1[1]-p_r/2, p_r, p_r),)
        pygame.draw.ellipse(screenf, (0,0,255), (bp2[0]-p_r/2, bp2[1]-p_r/2, p_r, p_r))
        pygame.draw.ellipse(screenf, (255,0,0), (bp3[0]-p_r/2, bp3[1]-p_r/2, p_r, p_r))

        if percent > 1:
            points2 = []
            percent = 0

        last = time.time()

        pygame.display.flip()

if __name__ == "__main__":
    main()