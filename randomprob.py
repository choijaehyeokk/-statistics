import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import random

def geom_randVar(step, prob):
    """
    step: 실험 횟수
    prob: 0이 될 확률

    난수를 생성하여 step 만큼 실험했을때 사용자가 정해놓은 prob이상일 경우 1, 아닐경우 0을 return한다.
    """
    
    b=[]
    for i in range(0,step-1):
        count = 0
        while(1):
            a = np.random.rand()
            if prob <= a:
                count += 1
                b[i] = count
                break
            else:
                count += 1
    return b
        
def geom_dist(step, prob):

    g = geom_randVar(step,prob)
    max_num = np.max(g)

    exp_x = 0
    exp_x2 = 0
    x_bin = []

    for i in range(1,max_num+1):
        x_bin = g[i-1]
        exp_x = exp_x + x_bin*prob
        exp_x2 = exp_x2 + math.pow(x_bin[i])*prob

    exp_v = math.pow(exp_x) - exp_x2

    print('          Experiment   Geometric')
    print('Mean:     %.4f,      %.4f'     %(),exp_x, 1/prob )
    print('Variance: %.4f,      %.4f'     %(),exp_v, (1-prob)/math.pow(p,2))        

def main():
  if len(sys.argv) != 3:
    print ('usage: python randomprob.py step prob')
    sys.exit(1)

  step = int(sys.argv[1])
  prob = float(sys.argv[2])

  geom_dist(step=step, prob=prob)

if __name__ == '__main__':
    main()
