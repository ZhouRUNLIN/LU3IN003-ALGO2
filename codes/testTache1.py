from projet import *

#test pour Inst_0000010_44.adn
cp=read_file("Instances_genome/Inst_0000010_44.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))

#test pour Inst_0000010_7.adn
cp=read_file("Instances_genome/Inst_0000010_7.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))

#test pour Inst_0000010_8.adn
cp=read_file("Instances_genome/Inst_0000010_8.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' ' + (str)(dist_naif(cp[2],cp[3])))

#les instances fournies en moins d’une minute
cp=read_file("Instances_genome/Inst_0000012_13.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))
cp=read_file("Instances_genome/Inst_0000012_56.adn")
print('distance de ' + cp[2] + ' et ' + cp[3] + ' : ' + (str)(dist_naif(cp[2],cp[3])))      #plus que 1min