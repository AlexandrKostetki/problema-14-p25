m=[[2,4,5,7,33],
[22,11,34,7,2],
[10,21,-1,5,67],
[23,55,68,-2,5],
[11,37,32,4,7]]
print('Suma 1 este',sum(m[0]))
print('Suma 2 este',sum(m[1]))
print('Suma 3 este',sum(m[2]))
print('Suma 4 este',sum(m[3]))
print('Suma 5 este',sum(m[4]))
r1=0
r2=0
r3=0
r4=0
r5=0
for i in m:
    r1+=i[0]
    r2+=i[1]
    r3+=i[2]
    r4+=i[3]
    r5+=i[4]
print('Suma primului rind=',r1)
print('Suma rindului 2=',r2)
print('Suma rindului 3 =',r3)
print('Suma rindului 4=',r4)
print('Suma rindului 5=',r5)
diagp= m[0][0]+m[1][1]+m[2][2]+m[3][3]+m[4][4]
diags= m[0][4]+m[1][3]+m[2][2]+m[3][1]+m[4][0]
print('Suma diagonalei principale=',diagp)
print('Suma diagonalei secundare=',diags)

