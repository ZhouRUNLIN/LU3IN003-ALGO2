import time

def read_file(fileName:str):
	"""
	Lire les dossiers de ADN sous la forme:
	lenX
	lenY
	x1 x2 x3...
	y1 y2 y3...
	(lenX <= lenY)
	retourne: (lenX:int,lenY:int,x:str,y:str)
	"""
	f=open(fileName)
	lenX=int(f.readline())
	lenY=int(f.readline())
	x=""
	y=""
	x0=f.readline()
	for c in x0:
		if c in {'A','T','C','G'}:
			x+=c
	y0=f.readline()
	for c in y0:
		if c in {'A','T','C','G'}:
			y+=c
	return (lenX,lenY,x,y)

# exercice 6
def dist_naif(x:str,y:str):
	"""
	Retourne d(X,Y) en utilisant le pseudo code donnee en exercice 6.
	Nous initialisons dist avec 2147483647 au lieu de l'infini positif.
	"""
	t0=time.time()
	dist=dist_naif_rec(x,y,0,0,0,2147483647)
	t1=time.time()
	print('Time taken for execution : ' + (str)(t1-t0))
	return dist

def dist_naif_rec(x:str,y:str,i:int,j:int,c:int,dist:int):
	"""
	Entrée : x et y deux mots,
	i un indice dans [0..|x|], j un indice dans [0..|y|],
	c le coût de l’alignement de (x[1..i],y[1..j])
	dist le coût du meilleur alignement de (x, y) connu avant cet appel
	Sortie : dist le coût du meilleur alignement de (x, y) connu après cet appel
	"""
	n=len(x)
	m=len(y)
	if n==i and m==j:
		if c<dist:
			dist=c
	else:
		if i<n and j<m:
			if x[i]==y[j]:
				cSub=0
			elif (x[i]=='C' and y[j]=='G') or (x[i]=='G' and y[j]=='C') or (x[i]=='A' and y[j]=='T') or (x[i]=='T' and y[j]=='A'):
				cSub=3
			else:
				cSub=4
			dist=dist_naif_rec(x,y,i+1,j+1,c+cSub,dist)
		if i<n:
			dist=dist_naif_rec(x,y,i+1,j,c+2,dist)
		if j<m:
			dist=dist_naif_rec(x,y,i,j+1,c+2,dist)
	return dist
	

cp=read_file("Instances_genome/Inst_0000010_44.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))
cp=read_file("Instances_genome/Inst_0000010_7.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))
cp=read_file("Instances_genome/Inst_0000010_8.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' ' + (str)(dist_naif(cp[2],cp[3])))
cp=read_file("Instances_genome/Inst_0000012_13.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))
cp=read_file("Instances_genome/Inst_0000013_45.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))
#cp=read_file("Instances_genome/Inst_0000014_7.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))