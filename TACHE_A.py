from algo_naive import *
import time



# x,y = readFile("./Instances_genome/Inst_0000010_7.adn")
# # print(DIST_NAIF(x,y)) #2
# start_time = time.time()
# DIST_NAIF(x,y)
# print((time.time() - start_time))

listFiles = ["Inst_0000010_8", "Inst_0000012_56","Inst_0000013_45","Inst_0000014_7","Inst_0000015_2","Inst_0000020_8","Inst_0000050_3"]

for ls in listFiles:
    x,y = readFile("./Instances_genome/"+ls+".adn")
    n=len(x)
    m=len(y)
    start_time = time.time()
    DIST_NAIF(x,y)
    print("{}:{}".format(n, (time.time() - start_time)))