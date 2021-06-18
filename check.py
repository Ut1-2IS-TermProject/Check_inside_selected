def is_in_poly(p, poly):
    """
    :param p: [x, y]
    :param poly: [[], [], [], [], ...]
    :return:
    """
    px, py = p
    is_in = False
    for i, corner in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = corner
        x2, y2 = poly[next_i]
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = True
                break
            elif x > px:  # if point is on left-side of line
                is_in = not is_in
    return is_in


def is_in_circle(p,c, rad):
    px, py = p
    cx,cy = c
    if ((px - cx) * (px - cx) +
            (py - cy) * (py - cy) <= rad * rad):
        return True;
    else:
        return False;





if __name__ == '__main__':
    point = [3, 3]
    poly = [[0, 0], [7, 3], [8, 8], [5, 5]]
    c = [1,1]
    r=3
    if (is_in_circle(point,c, r)):
        print("Inside");
    else:
        print("Outside");
    print(is_in_poly(point, poly))
