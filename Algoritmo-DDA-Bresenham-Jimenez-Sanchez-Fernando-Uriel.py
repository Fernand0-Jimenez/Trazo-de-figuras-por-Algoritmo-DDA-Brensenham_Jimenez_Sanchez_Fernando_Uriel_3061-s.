
def dda(x,y,x2,y2):
    
    dx = abs(x2-x)
    dy = abs(y2-y)
    steps = 0
    if dx>dy:
        steps = dx
    else:
        steps = dy

    increment_x = dx / steps     
    increment_y = dy / steps

    p1 = x
    p2 = y
    puntosx=[p1]
    puntosy=[p2]
    for i in range(steps):
        if x2 < x:
            p1 -= increment_x
        else:
            p1 += increment_x
        n = round(p1)
        puntosx.append(n)
        if y2>y:
            p2 += increment_y
        else:
            p2 -= increment_y 
        n = round(p2)
        puntosy.append(n)
    return puntosx,puntosy



def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0
    D = 2*dy - dx
    y = 0

    puntosx = []
    puntosy = []
    for x in range(dx + 1):
        puntosx.append(x0 + x*xx + y*yx)
        puntosy.append(y0 + x*xy + y*yy)
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    return puntosx,puntosy