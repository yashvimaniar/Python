no=1
while no<11:
    cube=no*no*no
    rem=no%2 
    if rem==0: #even
        cube=0-cube
    print(cube,end=' ')  
    no=no+1

