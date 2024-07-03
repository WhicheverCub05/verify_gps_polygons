from shapely.geometry import LineString
import random
# import matplotlib

def provideSolutions(polygon):
    completable = True
    solution = polygon
    
    iterations = 0
    while completable:

        if iterations >= len(solution) ** 2:
            completable = False

        if works(solution):
            print("what works: ", solution)
            return solution

        # try out different combinations of polygons
        # re-arrange polygons randomly then try
        random.shuffle(solution) 
        iterations += 1
    return False


def works(solution):
    # checks if any lines in solution intersect
    # print("testing: ", solution)
    length = len(solution)
    for i in range(len(solution)):
        line1 = [solution[i], solution[(i+1)]]
        for j in range(i+1, len(solution)):
            line2 = [solution[j], solution[(j+1)%length]]
            if intersects(line1, line2):
                return False
    return True

# https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
def intersects(line1, line2):
    # line = start and end points [[x1, y1], [x2, y2]]
    print("line1: ", line1, " line2: ", line2)
    
    ls1 = LineString(line1)
    ls2 = LineString(line2)
    if ls1.intersects(ls2):
        return True
    return False
