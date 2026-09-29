x=input("X:")
x=float(x)
y=x/2
while abs(x-(y*y))>0.001:
    y=(y+x/y)/2
    diff=abs(x-(y*y))
    print(diff)
    print(round(y,3))