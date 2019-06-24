#The purpose of this program is to allow the user to choose between calculating the area of 2D shapes and the volume of 3D figures .


import math

# 2D formulas:
def artriangle(height, base):
    trianglearea = 0.5 * (base * height)
    return trianglearea

def artcircle(radius):
    circlearea = math.pi * radius * radius
    return circlearea

def artrapezoid(base1, base2, heighttrap):
    trapezoidarea = (base1 + base2) * heighttrap
    return trapezoidarea

def arquad(heightq, baseq):
    quadrilateralarea = (heightq * baseq)
    return quadrilateralarea

def volcube(edgelength):
    cubevolume = edgelength * edgelength * edgelength
    return cubevolume

def volsphere(sphereradius):
    spherevolume = (4 * math.pi * sphereradius * sphereradius * sphereradius) / 3
    return spherevolume

def volcyl(cylinderradius, cylinderheight):
    cylindervolume = (math.pi * cylinderradius * cylinderradius * cylinderheight)
    return cylindervolume

def volpyr(pyrw, pyrh, pyrl):
    pyramidvolume = (pyrw * pyrh * pyrl) / 3
    return pyramidvolume

def voloct(oedge):
    octahedronvolume = (math.sqrt(2) * oedge * oedge * oedge) / 3
    return octahedronvolume

def volcone(coneradius):
    conevolume = math.pi * coneradius * coneradius
    return conevolume

choice = (input('Welcome to the Figure Calculator! Pick from a list of geometric figures provided to calculate the area or volume, if the calculation is possible possible! What would you like to calculate? Enter either 2D for 2D shapes or anything else for 3D figures. '))

if choice == '2D' or choice == '2d' :
    tshape = (input('What kind of shape would you like to calculate? Choose from triangle, trapezoid, quadrilateral: (square or rectange), or circle: '))
    print('You selected ' + tshape)
    if tshape == 'triangle' or tshape == 'Triangle':
        height = float(input('Height of the triangle? '))
        base = float(input('Length of base of the triangle? '))
        print(artriangle(height, base))
    elif tshape == 'trapezoid' or tshape == 'Trapezoid':
        base1 = float(input('Length of the first base of the trapezoid? '))
        base2 = float(input('Length of the second base of the trapezoid? '))
        heighttrap = float(input('Height of the trapezoid? '))
        print(artrapezoid(base1, base2, heighttrap))
    elif tshape == 'Quadrilateral' or tshape =='quadrilateral':
        baseq = float(input('Width of the quadrilateral? '))
        heightq = float(input('Height of the quadrilateral? '))
        print(arquad(heightq, baseq))                       
    else:
        radius = float(input('Radius of the circle? '))
        print(artcircle(radius))
else:
    thshape = (input('What kind of 3D figure would you like to calculate? Choose from cube, cone, sphere, pyramid, octahedron, or cylinder, '))
    print('You selected ' + thshape)
    if thshape == 'cube' or thshape == 'Cube':
        edgelength = float(input('Length of the edge of the cube? '))
        print(volcube(edgelength))
    elif thshape == 'sphere' or thshape == 'Sphere':
        sphereradius = float(input('Radius of the sphere? '))
        print(volsphere(sphereradius))
    elif thshape == 'Cylinder' or thshape == 'cylinder':
        cylinderradius = float(input('Radius of the cylinder? '))
        cylinderheight = float(input('Height of the cylinder? '))
        print(volcyl(cylinderradius, cylinderheight))
    elif thshape == 'Pyramid' or thshape == 'pyramid':
        pyrw = float(input('Width of the pyramid? '))
        pyrh = float(input('Height of the pyramid? '))
        pyrl = float(input('Length of the pyramid? '))
        print(volpyr(pyrw, pyrh, pyrl))
    elif thshape == 'Octahedron' or thshape == 'octahedron':
        oedge = float(input('Edge length of the octahedron? '))        
        print(voloct(oedge))
    else:
        coneradius = float(input('Radius of the cone? '))
        print(volcone(coneradius))

