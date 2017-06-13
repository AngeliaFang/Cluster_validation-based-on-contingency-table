# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 20:01:07 2017

@author: lab
"""

#import scipy.stats as stats
#from sklearn.metrics.cluster import adjusted_rand_score
import numpy as np
import math

#定义contingency table
contingency1 = np.array([[25, 50, 45, 900, 30, 0, 1050],
                [75, 1000, 40, 20, 45, 20, 1200],
                [20, 25, 550, 30, 25, 700, 1350],
                [900, 20, 10, 20, 40, 10, 1000],
                [50, 25, 25, 30, 1250, 20, 1400],
                [1070, 1120, 670, 1000, 1390, 750, 6000]])

#定义函数用来求组合数（n 2），即从n中任取2个数的组合情况,方便求ARI 
def combination_number(n):
    return n * (n - 1) / 2

#contingency table一共有多少行多少列
ROW = contingency1.shape[0]
COL = contingency1.shape[1]

#一共有多少个操作对象
OBJ_NUM = contingency1[ROW - 1][COL - 1]

#n个对象的组合数
T = combination_number(OBJ_NUM)

#行列的求和保存在序列中
M_I = []
M_J = []

for row in range(ROW - 1):
    #print contingency1[row][COL - 1]
    M_I.append(contingency1[row][COL - 1])

for col in range(COL - 1):
    #print contingency1[ROW - 1][col]
    M_J.append(contingency1[ROW - 1][col])

#计算ARI的函数                  
def ARI1():
    all_sum = 0
    row_sum = 0
    col_sum = 0
    for i in range(ROW - 1):
        for j in range(COL - 1):
            all_sum += combination_number(contingency1[i][j])
            
    
    for i in range(ROW - 1):
        #print M_I[i]
        row_sum += combination_number(M_I[i])
        
    #print row_sum
        
    for j in range(COL - 1):
        col_sum += combination_number(M_J[j])
    
    sum_mul = row_sum * col_sum / T
    
    sum_sum = (row_sum + col_sum) / 2

    ari = float((all_sum - sum_mul)) / (sum_sum - sum_mul)
    
    return ari  

    
#求似然的log函数    
def mul_log(div_num):
    div_num = float(div_num) / OBJ_NUM
    return div_num * (math.log(div_num))

#计算MI(Mutual Information)的函数    
def MI1():
    H_U = 0
    H_V = 0
    H_U_V = 0
    
    for i in range(ROW - 1):
        #print M_I[i]
        H_U -= mul_log(M_I[i])
        
    for j in range(COL - 1):
        H_V -= mul_log(M_J[j])
        
    for i in range(ROW - 1):
        for j in range(COL - 1):
            if contingency1[i][j] != 0:
                H_U_V -= mul_log(contingency1[i][j])
            
    mi = (H_U + H_V - H_U_V) / (math.log(OBJ_NUM))
    
    return mi

    
ari1 = ARI1()
print 'ARI:', ari1

mi1 = MI1()
print 'MI:', mi1
