from algo_naive import *
import time



x,y = readFile("./Inst_0000010_8.adn")
# print(DIST_NAIF(x,y)) #2
start_time = time.time()
DIST_NAIF(x,y)
print((time.time() - start_time))