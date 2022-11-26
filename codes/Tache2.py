def min_3(a:int,b:int,c:int):
    """
    Trouver le plus petit chiffre entre a,b et c.
    """
    if a>b:
        a=b
    if a>c:
        a=c
    return a

def cost_sub(x:str,y:str,i:int,j:int):
    """
    Calculer le c_sub de x[i] et y[j]
    """
    if x[i-1]==y[j-1]:
        return 0
    elif (x[i-1]=='C' and y[j-1]=='G') or (x[i-1]=='G' and y[j-1]=='C') or (x[i-1]=='A' and y[j-1]=='T') or (x[i-1]=='T' and y[j-1]=='A'):
        return 3
    else:
        return 4

def dist_1(x:str,y:str):
    """
    Calculer la distance en utilisant le psuedo code de Q12
    """
    n=len(x)
    m=len(y)
    return dist_1_rec(x,y,n,m)

def dist_1_rec(x:str,y:str,i:int,j:int):
    """
    Corps de partie recursion de dist_1
    """
    if i==0 and j==0:
        return 0
    if i==0:
        return j*2
    if j==0:
        return i*2
    a=dist_1_rec(x,y,i-1,j)+2
    b=dist_1_rec(x,y,i,j-1)+2
    c=dist_1_rec(x,y,i-1,j-1)+cost_sub(x,y,i,j)
    return min_3(a,b,c)

def create_T(x:str,y:str):
    """
    La creation de la table T indexé par [0..|x|] * [0..|m|] contenant les valeurs de D
    """
    T=[[0]*(len(y)+1) for i in range(len(x)+1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            T[i][j]=dist_1(x[0:i],y[0:j])
    return T

def sol_1(T:list,x:str,y:str):
    """
    Trouver l'alignement avec le plus petite distance en utilisant le psuedo code de Q16
    """
    n=len(x)
    m=len(y)
    return sol_1_rec(T,x,y,n,m)

def sol_1_rec(T:list,x:str,y:str,i:int,j:int):
    if i==0 and j==0:
        return ("","")
    if i==0:
        return ("-"*j,y[0:j])
    if j==0:
        return (x[0:i],"-"*i)
    a=T[i-1][j-1]+cost_sub(x,y,i,j)
    b=T[i-1][j]+2
    c=T[i][j-1]+2
    if a==T[i][j]:
        al_x,al_y=sol_1_rec(T,x,y,i-1,j-1)
        return (al_x+x[i-1],al_y+y[j-1])
    if b==T[i][j]:
        al_x,al_y=sol_1_rec(T,x,y,i-1,j)
        return (al_x+x[i-1],al_y+"-")
    al_x,al_y=sol_1_rec(T,x,y,i,j-1)
    return (al_x+"-",al_y+y[j-1])

x="ATCCG"
y="AACGT"
T=create_T(x,y)
print(dist_1(x,y))
print(sol_1(T,x,y))