A=float(input('Enter the value of a:  '))
B=float(input('Enter the value of b:  '))
C=float(input('Enter the value of c:  '))
#In 2nd degree equations we have:aX^2+bX+c
#In order to solve the Equatin we need Delta=b^2-4ac and from the result of it we'll have 3 type of answers
D=(B**2)-4*(A*C)
if D<0:
    print('No Answere')
elif D==0:
    x=float(-B/(2*A))
    print('The Answere of equation is X= ',x)
#sqrt math library command take after the Root
else:
    import math
    x1=(-B+math.sqrt(D))/(2*A)
    x2=(-B-math.sqrt(D))/(2*A)
    print('The Answers of the equation are X1 =', x1, 'and X2 =', x2)
#Written by Ali Behrouz id.n:0440868203
