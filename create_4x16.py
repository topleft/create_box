def box_H_line(x,y,z):
    x = x + " "
    y = y + " "
    z = z
    print x, y*4, x, y*4, z

def box_H_line_add(x,y,z):
    x = x + " "
    y = y + " "
    z = z
    print x, y*4, x, y*4, z, y*4, x, y*4, z
    
def box_V_line(t):
    t = t + (" " * 11) + t + (" " * 11) + t
    print t
    print t
    print t
    print t
    print t
   

def box_V_line_add(t):
    t = t + (" " * 11) + t + (" " * 11) + t + (" " * 10) + t + (" " * 11) + t
    print t
    print t
    print t
    print t
    print t    

def boxes_4(f1,f2, x,y,z,t):
    f1(x,y,z)
    f2(t)
    f1(x,y,z)
    f2(t)
    f1(x,y,z)




    
def boxes_16(f3, f4, x,y,z,t):
    #prints first box (4 columns, 2 rows)
    f3(x,y,z)
    f4(t)
    f3(x,y,z)
    f4(t)
    f3(x,y,z)
    #prints second box under the first, ammended to add on
    f4(t)
    f3(x,y,z)
    f4(t)
    f3(x,y,z)
    
box_H_line("+", "-", "+")
box_V_line("/")
box_H_line("+", "-", "+")
box_V_line("/")
box_H_line("+", "-", "+")

print " "
print " "

boxes_16(box_H_line_add, box_V_line_add,  "8", "0", "8", "0")
boxes_16(box_H_line_add, box_V_line_add,  "+", "-", "+", "/")
boxes_16(box_H_line_add, box_V_line_add,  ">", "<", ">", "<")

