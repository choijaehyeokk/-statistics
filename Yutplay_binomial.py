import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def binomial_dist(n, k, p):
  if k > n:
        print ('k can not be greater than n')
        sys.exit(1)
  else:
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))*pow(p,n)*pow(1-p,n-k)

def yutNori(step, prob_head=0.5):

  count = 1
  
  do_truth = binomial_dist(4,1,prob_head)
  gae_truth = binomial_dist(4,2,prob_head)
  geol_truth = binomial_dist(4,3,prob_head)
  yut_truth = binomial_dist(4,4,prob_head)
  mo_truth = binomial_dist(4,0,prob_head)
  do =0
  gae =0
  geol =0
  yut =0
  mo =0
  s = np.random.binomial(4,0.5,step)
  for num in s:
          if num == 1:
                  do= do +count
          elif num ==2:
                  gae= gae+count
          elif num==3:
                  geol= geol+count
          elif num==4:
                  yut=yut+count
          else:
                  mo=mo+count

  mo = mo/step
  do =do/step
  geol = geol/step
  yut = yut/step
  gae = gae/step
  xlabel = ['do','gae','geol','yut','mo']
  value = [do,gae,geol,yut,mo]
  value2 = [do_truth,gae_truth,geol_truth,yut_truth,mo_truth]

  sum_of_probability = mo + do + gae + geol + yut
  
  if sum_of_probability != 1:
    print ('Sum of probability is not one')
    sys.exit(1)

  print ('Probability mo: %f, %f' %(mo, mo_truth) + \
        '\nProbability do: %f, %f' %(do, do_truth) + \
        '\nProbability gae: %f, %f' %(gae, gae_truth) + \
        '\nProbability geol: %f, %f' %(geol, geol_truth) + \
        '\nProbability yut: %f, %f' %(yut, yut_truth))
  plt.subplot(2, 1, 1)
  plt.bar(xlabel,value2)
  plt.title('true_value')
  plt.subplot(2, 1, 2)
  plt.bar(xlabel,value)
  plt.title('random_value')
  plt.show()

def main():
  if len(sys.argv) != 2:
    print ('usage: ./yut.py step')
    sys.exit(1)

  step = int(sys.argv[1])

  yutNori(step=step)

if __name__ == '__main__':
  main() 
