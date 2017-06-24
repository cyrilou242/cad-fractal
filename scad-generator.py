# First draft of an iterative function to generate fractal forms
#Cyril de Catheu
#04072017
#Original idea : generating sphere based fractal much more complicated than that http://www.redditpics.com/-300x218-animated-3d-fractal-openscad-,1644777
#had difficulties in CAO softwares, on openscad, in expressing mathematically the relation between my sphere and its children
#so to begin went with an easy expression based on cubes
#allowed me to write easilly a first function
#complexity of the function is exponential


from solid import *    #import Solidpython
from solid.utils import *  #import Solidpython

SEGMENTS =160  #think it's not considered (useless)

a=cube(0)
def fractal(a,n,p1,p2,p3,p4):  #a forme, n itérations, p1: taille cube, p2 : up, p3,left, p4 foward
    b=cube(p1,center=True)
    b=up(p2)(b)
    b=left(p3)(b)
    b=forward(p4)(b)
    #right p5
    #down  p6
    #back p7
    a+=b
    if n==0:
       return(a)
    else:
      return(fractal(a,n-1,p1/2,p2+p1/2,p3,p4) + fractal(a, n-1,p1/2,p2,p3+p1/2,p4) +fractal(a,n-1,p1/2,p2,p3,p4+p1/2))

a= fractal(a,6,200,0,0,0)
#add to remove not interresting parts
r=cube(400,center=True)
r=down(200)(r)
q=cube(400,center=True)
q=right(200)(q)
p=cube(400,center=True)
p=back(200)(p)
a-=p
a-=q
a-=r
#end add
s=scad_render(a)
print(s)
#scad_render_to_file(a, "/Users/Cyril/CAO3test2") ##pour enregistrer dans un fichier, filepath en 2eme argument ->useless,already exists
text_file = open("/Users/Cyril/generated","w")
text_file.write(s)  #need to add a first line "$fn=x;" docs on $fn first
text_file.close()


#need to rewrite all the code like fractal(n,f) where n : number of iterations (depth) and f : designing function
#with rules on f definition, whould be easy for everyone to write f's and then throw the through the fractal function
