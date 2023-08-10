A = int(input('Enter the value of Day (Iranian Calendar): '))
#In Iranian calender we have 365 days which each for years it becomes 366 days (Kabiseh year)
#First six months has 31 days and others are (except Esfand on ordinary years that is 29 days) 30 days
if 0<A<=186:
#//:Floor Division , %:Modulus
    M=(A-1)//31+1
    D=(A-1)%31+1
    print(M,D,sep='/')
elif 186<A<=366:
#We shoud take 6 days from A
    l=A-6
    M=(l-1)//30+1
    D=(l-1)%30+1
    print(M,D,sep='/')
else:
    print('The value is Not valid')
#Written by Ali Behrouz id.n:0440868203
