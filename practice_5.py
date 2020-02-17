import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import random
def xy(step):
#xy 함수는 step번의 횟수를 받아서 처리하는 함수이다.
    ax = [1,2,3,4]
    ay = [1,2,3,4]
    #choice 메서드에서 쓰일 배열을 만들었다.
    x = np.random.choice(ax, step, p=[0.2,0.4,0.3,0.1])
    y = np.random.choice(ay, step, p=[0.25,0.25,0.25,0.25])
    #np.random.choice메서드는 (*a,int 횟수,p*(각 인덱스의 확률로 *a에 맞는 인덱스의 값을 출력하여 x배열에 담아준다.))
    #ex) x = [1,2,2,1,2,3,3,2,2,4,1,...] 개수는 step개수 만큼.
    return x, y
    #python에서는 return값을 꼭 1개가 아니더라도 반환할 수 있게 해준다.

def randomvariable(step):

    x, y = xy(step)
    #xy함수를 호출하고 반환하여 각각을 지역변수 x,y에 담았다.
    matrix = [[0]*4 for i in range(4)]
    matrix_x = [[0]*1 for i in range(step)]
    matrix_y = [[0]*1 for i in range(step)]
    #행렬은 사실 1차원 배열의 묶음으로 표현될 수 있다.
    #a = [[value]*1차원배열의 크기 for i in range(1차원배열 묶음의 개수)]이렇게 표현하면 다차원 배열을 표현할 수 있다.
    #따라서 
    #print(x)
    #print(y) 그냥 한번 잘 찍히나 출력해보았다.
    for i in range(0,step):
        if (x[i] ==1 and y[i] == 1):
            matrix[0][0] += 1
            matrix_x[i]=1
            matrix_y[i]=1
        elif (x[i] ==1 and y[i] == 2):
            matrix[0][1]+=1
            matrix_x[i]=1
            matrix_y[i]=2
        elif (x[i] ==1 and y[i] == 3):
            matrix[0][2] += 1
            matrix_x[i]=1
            matrix_y[i]=3
        elif (x[i] ==1 and y[i] == 4):
            matrix[0][3] += 1
            matrix_x[i]=1
            matrix_y[i]=4
            
        elif (x[i] ==2 and y[i] == 1):
            matrix[1][0] += 1
            matrix_x[i]=2
            matrix_y[i]=1
        elif (x[i] ==2 and y[i] == 2):
            matrix[1][1] += 1
            matrix_x[i]=2
            matrix_y[i]=2
        elif (x[i] ==2 and y[i] == 3):
            matrix[1][2] += 1
            matrix_x[i]=2
            matrix_y[i]=3
        elif (x[i] ==2 and y[i] == 4):
            matrix[1][3] += 1
            matrix_x[i]=2
            matrix_y[i]=4
            
        elif (x[i] ==3 and y[i] == 1):
            matrix[2][0] += 1
            matrix_x[i]=3
            matrix_y[i]=1
        elif (x[i] ==3 and y[i] == 2):
            matrix[2][1] += 1
            matrix_x[i]=3
            matrix_y[i]=2
        elif (x[i] ==3 and y[i] == 3):
            matrix[2][2] += 1
            matrix_x[i]=3
            matrix_y[i]=3
        elif (x[i] ==3 and y[i] == 4):
            matrix[2][3] += 1
            matrix_x[i]=3
            matrix_y[i]=4

        elif (x[i] ==4 and y[i] == 1):
            matrix[3][0] += 1
            matrix_x[i]=4
            matrix_y[i]=1
        elif (x[i] ==4 and y[i] == 2):
            matrix[3][1] += 1
            matrix_x[i]=4
            matrix_y[i]=2
        elif (x[i] ==4 and y[i] == 3):
            matrix[3][2] += 1
            matrix_x[i]=4
            matrix_y[i]=3
        elif (x[i] ==4 and y[i] == 4):
            matrix[3][3] += 1
            matrix_x[i]=4
            matrix_y[i]=4
    #1차원 배열 x와y의 각각의 인덱스 값을 step번 비교하여 X variable 1차원 배열을 만들었고,마찬가지로 Y variable 1차원 배열을 만들었다.
    #2차원 배열 matrix 를 만들었다.

    print("#3")
    p_x4=0
    p_y1=0
    p_x2y3=0
    #각 확률을 구하기 위해서 0으로 초기화 해주었다.
    for i in range(0,4):
        p_x4 = p_x4 + matrix[3][i]
    #p_x4를 구하기 위해서 variable X는 4(index)3)를 구하기 위해서 matrix배열의 3번째 index를 고정시키고 각 y값들의 합을 구했다.
    for i in range(0,4):
        p_y1 = p_y1 + matrix[i][0]
    #p_y1를 구하기 위해서 variable Y는 1(index)0)를 구하기 위해서 matrix배열의 0번째 index를 고정시키고 각 x값들의 합을 구했다.
    for i in range(0,4):
        p_x2y3 = p_x2y3 + matrix[i][2]
    #조건부 확률(Conditioning probability)를 구하기 위해서 일단 조건부인 y=3의 값을 다 더해주었다.

    print("Px(4) = " + str(p_x4) +"/"+str(step))
    print("Py(1) = " + str(p_y1) +"/"+str(step))
    #위의 값들을 각각 출력해주었다.
    print("P2|3(2,3) = " + str(matrix[1][2]) +"/"+str(p_x2y3))
    #y=3의 값을 다 한것이 sample space가 되기 때문에 출력문에서는 위에 구한 값이 분모가 되고,분자에는 조건부 2|3의 값인 matrix[1][2]값이 들어간다.
    print("---------------------------------------")
    
    print("#4")
    E_x=0
    for i in range(1,5):
        for j in range(1,5):
            E_x=E_x+(i*(matrix[i-1][j-1])/step)
    #E[X]의 값을 구하는 방법은 x*p(x)의 총 합이므로, index[0][0]*1 + index[0][1]*1..이런식으로 다 더한다.
    print('E[X]:')
    print(E_x)

    E_y=0
    for i in range(1,5):
        for j in range(1,5):
            E_y=E_y+(i*(matrix[j-1][i-1])/step)
    #E[Y]의 값을 구하는 방법은 y*p(y)의 총 합이므로, index[0][0]*1 + index[1][0]*1..이런식으로 다 더한다.
    print('E[Y]:')
    print(E_y)

    print('np.mean(X):')
    a=np.mean(matrix_x)
    #np.mean메소드를 이용하여 E[X]를 구하기 위해서 variable X의 값들만 담아 놓은 matrix_x를 이용하여 구한다.
    print(a)
    print('np.mean(Y):')
    b=np.mean(matrix_y)
    #np.mean메소드를 이용하여 E[Y]를 구하기 위해서 variable Y의 값들만 담아 놓은 matrix_y를 이용하여 구한다.
    print(b)
    print('----------------------------')

    print("#5")
    E_x2=0
    #E[x^2]를 구하기 위해서 E_x2라는 변수를 만들었다.
    var_x=0
    #V[x]를 구하기 위해서var_x를 만들었다.
    for i in range(1,5):
        for j in range(1,5):
            E_x2=E_x2+(pow(i,2)*(matrix[i-1][j-1])/step)
    #E[x^2]는 x^2*p(x)의 총 합이므로, index[0][0]*1^2 + index[0][1]*1^2..이런식으로 다 더한다.
    var_x=E_x2-pow(E_x,2)
    #V(X) = E[X^2] - (E[X])^2 이므로 위에서 mean메서드로 구했던 E_x를 이용해서 V(X)를 구해준다.
    print('var(x):')
    print(var_x)
    E_y2=0
    #E[y^2]를 구하기 위해서 E_y2라는 변수를 만들었다.
    var_y=0
    #V[y]를 구하기 위해서var_y를 만들었다.
    for i in range(1,5):
        for j in range(1,5):
            E_y2=E_y2+(pow(i,2)*(matrix[j-1][i-1])/step)
    #E[y^2]는 y^2*p(y)의 총 합이므로, index[0][0]*1^2 + index[0][1]*1^2..이런식으로 다 더한다.
    var_y=E_y2-pow(E_y,2)
    #V(Y) = E[Y^2] - (E[Y])^2 이므로 위에서 mean메서드로 구했던 E_y를 이용해서 V(Y)를 구해준다.
    print('var(y):')
    print(var_y)

    print('np_var(x):')
    vx=np.var(matrix_x)
    #np.var메소드를 이용하여 V[X]를 구하기 위해서 variable X의 값들만 담아 놓은 matrix_x를 이용하여 구한다.
    print(vx)
    print('np_var(y):')
    vy=np.var(matrix_y)
    #np.var메소드를 이용하여 V[Y]를 구하기 위해서 variable Y의 값들만 담아 놓은 matrix_y를 이용하여 구한다.
    print(vy)
    print('----------------------------')

    print("#6")
    print('E[2X+4]:')
    #linear원리에 의해서 E[2X+4] =2E[X] +4가 된다.
    print(2*a+4)
    #따라서 위에 구했던 mean에 값만 대입해줘서 구한다.
    print('E[-y^2-1]:')
    #linear원리에 의해서 E[-y^2-1] = -E[Y^2] -1이된다.
    print((-1*E_y2)-1)
    #따라서 위에 구했던 E[Y^2]의 값인 E_y2의 값을 대입하여 구한다.
    print('var[3Y-3]:')
    #linear원리에 의해서 var[3Y-3]은 9var[y]이 된다.
    print(pow(3,2)*var_y)
    #따라서 위에 구했던 var[Y]의 값인 var_y값을 대입하여 구한다.
    print('----------------------------')

    print("#7")
    print("Px,y(x,y) != Px(x)*Py(y)")
    print("If x = 2, y =2일때,")
    print("Px,y(2,2) :" + str(matrix[1][1]/step))
    p_x2 = 0
    p_y2 = 0
    #(2,2)의 좌표에 있는 확률을 구해주었다.
    for i in range(0,4):
        p_x2 = p_x2 + matrix[1][i]
    print("Px(2) :" + str(p_x2/step))
    #Px(2)값을 구해주기 위해서 위에 있는 for문을 이용하여 구하였다.
    for i in range(0,4):
        p_y2 = p_y2 + matrix[i][1]
    print("Py(2) :" + str(p_y2/step))
    #Py(2)값을 구해주기 위해서 위에 있는 for문을 이용하여 구하였다.
    print("Px(2)*Py(2) :" + str((p_x2/step)*(p_y2/step)))
    #두 값을 곱해서 구해주었다.

    print("Px,y(x,y) != Px(x)*Py(y) 이다.")
    #쉽게 말해서 두 x,y는 독립이 아니라는 것을 의미한다.
    #x는 y에게 y는 x에게 서로 영향을 미칠 수 있다는 것을 의미하기도 한다. random probability이기 때문.
    
    plt.figure()
    for i in range(1,5):
        for j in range(1,5):
           plt.text(i+0.1,j,"{}/{}".format(matrix[i-1][j-1], step), fontsize = 7)
    plt.scatter(x, y, s =0.1, c = "blue", marker = "o")

    plt.show()
    #print(matrix)
            
def main():
  if len(sys.argv) != 2:
    print ('usage: python practice_05.py step')
    sys.exit(1)

  step = int(sys.argv[1])

  randomvariable(step=step)

if __name__ == '__main__':
    main()
