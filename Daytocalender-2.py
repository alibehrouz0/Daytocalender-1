A=int(input('Enter the value of Day (iranian calender): '))
#In Iranian calender we have 365 days which each for years it becomes 366 days (Kabiseh year)
#First six months has 31 days and others are (except Esfand on ordinary years that is 29 days) 30 days
if 0<A<=31:
    print(1,A,sep='/')
elif 31<A<=62:
    D=A-31
    print(2,D,sep='/')
elif 62<A<=93:
    D=A-62
    print(3,D,sep='/')
elif 93<A<=124:
    D=A-93
    print(4,D,sep='/')
elif 124<A<=155:
    D=A-124
    print(5,D,sep='/')
elif 155<A<=186:
    D=A-155
    print(6,D,sep='/')
elif 186<A<367:
#//:Floor Division , %:Modulus
#We shoud take 6 days from A
    l=A-6
    M=(l-1)//30+1
    D=(l-1)%30+1
    print(M,D,sep='/')
else:
    print('The value is Not Valid')
#Written by Ali Behrouz id.n:0440868203
