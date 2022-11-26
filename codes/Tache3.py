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

def dist_2(x:str,y:str):
    """
    Calculer la distance en dessinant la table de la distance.
    """
    n=len(x)
    m=len(y)
    T=[[0]*(len(y)+1) for i in range(len(x)+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 and j==0:
                T[i][j]=0
                continue
            if i==0:
                T[i][j]=j*2
                continue
            if j==0:
                T[i][j]=i*2
                continue
            T[i][j]=min_3(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+cost_sub(x,y,i,j))
    return T[n][m]

x="ATCCG"
y="AACGT"
print(dist_2(x,y))