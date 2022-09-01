max1=4
max2=3
def pour(jug1,jug2):
    x=1
    while(True):
        print("{%d\t%d}" % (jug1, jug2))

        if x==1:
            if jug2 < max2:
                jug1=0
                jug2=max2
        elif x==2 :
            if jug1+jug2 <= 4 and jug2 > 0:
                jug1=jug1+jug2
                jug2=0
        elif x==3 :
            if jug2<3 :
                jug2=max2
        elif x==4 :
            if jug1+jug2 <= 6 and jug2>0 :
                jug2 = (jug2 - (4 - jug1))
                jug1=max1

        elif x==5 :
            if jug1>0 :
                jug1=0
        elif x==6 :
            if jug1+jug2 <=4 and jug2>0:
                jug1=jug1+jug2
                jug2=0
        elif x==7 :
            break
        x=x+1
print("JUG1\tJUG2")
pour(0,0)

