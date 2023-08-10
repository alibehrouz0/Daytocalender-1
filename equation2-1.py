A=float(input('Enter the value of a: '))
B=float(input('Enter the value of b: '))
C=float(input('Enter the value of c: '))
#In 2nd degree equations we have:aX^2+bX+c
#In order to solve the Equatin we need Delta=b^2-4ac and from the result of it we'll have 3 type of answers
D=B**2-4*A*C
if D<0:
    print('No Answer')
elif D==0:
    x=-B/(2*A)
    print('The Answer of the equation is X =', x)
#As we know any Root could change to it's Exponentiation, for exp:Root2x=x^(1/2)
else:
    x1=(-B+D**(1/2))/(2*A)
    x2=(-B-D**(1/2))/(2*A)
    print('The Answers of the equation are X1 =', x1, 'and X2 =', x2)
#Written by Ali Behrouz id.n:0440868203
