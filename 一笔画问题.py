#=============一笔画问题.
import matplotlib.pyplot as plt

# 1表示可以走的路, 0表示墙
# [0,1,1,1,1,1]
# [1,1,0,0,1,1]
# [1,0,1,1,1,1]
# [1,1,1,1,0,1]
# [1,0,1,1,1,1]
# [1,1,1,1,1,0]





#


ditu=[
[1,1,0,1,1,1,1,1,1],
[1,1,1,1,0,1,1,1,1],
[1,1,1,1,1,1,0,1,1],
[1,1,1,0,1,1,1,1,1],
[1,0,1,1,1,1,1,0,1],
[1,1,1,1,1,0,1,0,1],
[0,1,1,0,1,1,1,1,1],
[1,1,1,1,1,1,1,1,0],




]


#==========cn2选起始点和终点. 排列组合.
all_point=[]
for i in range(len(ditu)):
  for j in range(len(ditu[0])):
    if ditu[i][j]==1:
      all_point.append([i,j])
print(1)
point_num=len(all_point)
#==========任意取2个点的所有组合:

kaishi_jieshu_zuhe=[]
for i in range(len(all_point)-1):
   for j in range(i+1,len(all_point)):
     kaishi_jieshu_zuhe.append([all_point[i],all_point[j]]) # 406个点.
print(1)








#=============
# 其实我们只需要确定起点就够了. 然后算他的最长路径即可.
#每一个路径我们都要保存, 所以用多叉树结构来存所有路径
# class node:
#    def __init__(self,val):
#       self.val=val  #自己的值
#       self.children=[] # childre是node组成的数组.

# for i in all_point:
#    start=i
#    t=node(start) # 起始点创建的节点就记作根节点.

#    print(1)


#=========还是直接保存路径
start_luxian=all_point.copy()  #所有第一步能走到的点.
#========把点个点变成路径
for i in range(len(start_luxian)):
   start_luxian[i]=[start_luxian[i]]
#==========生成走2步的所有路径

dx=[-1,1,0,0]
dy=[0,0,-1,1] #只能上下左右走.

#==========输入第n步的全部路线, 输出第n+1步的全部路线.
def one_step(start_luxian):
  next_luxian=[]
  for i in start_luxian:
        tmp_luxina=i
        tmp_luxian_zuihouyigedian=i[-1]

        #===最后一个点开始尝试找到下一个点
        candidate=[]
        for j in range(len(dx)):
          nx=[tmp_luxian_zuihouyigedian[0]+dx[j],tmp_luxian_zuihouyigedian[1]+dy[j]]
          if 0<=nx[0]<len(ditu) and  0<=nx[1]<len(ditu[0]) and nx not in tmp_luxina and ditu[nx[0]][nx[1]]==1 :

            # candidate.append([nx])
            # print(1)
        #========路线合并
        # for j in candidate:
           next_luxian.append(tmp_luxina+[nx]) #======这个地方的二维数组确实很饶腾, 以后可以nmpy重写.
        # print(1)
  return next_luxian


#==========根据我们地图我们知道,度为1的点一定是起点!!!!!
start_luxian=[[[7,0]]]
# start_luxian=all_point  #如果我们没有度为1的点, 那么我们就只能设置为所有带你都



for i in range(25):#一共可以走这么多步:
  print('当前推理:',i,'步','组合',len(start_luxian),'个')
  
  next_luxian=one_step(start_luxian)
  if next_luxian==[]:
    print('找到最长的路线了',start_luxian[0],'长度',len(start_luxian[0]),'走法一共有',len(start_luxian))
    break
  start_luxian=next_luxian

print(1)


#===========gui画图

import numpy as np

#======输入左上角
kuan=0.05
print(ditu)
for i in range(len(ditu)):
  for j in range(len(ditu[0])):
    
    zuoxiajiaoy=0.05*(len(ditu[0])-i-1)#======这地方衡中坐标也非常复杂.
    zuoxiajiaox=0.05*(j)

    if ditu[i][j]==1:
      square = plt.Rectangle(xy=(zuoxiajiaox, zuoxiajiaoy), width=kuan, height=kuan, alpha=0.8, angle=0.0,facecolor='blue',fill=True,edgecolor ='black')
    else:
            square = plt.Rectangle(xy=(zuoxiajiaox, zuoxiajiaoy), width=kuan, height=kuan, alpha=0.8, angle=0.0,facecolor='blue',color='white')
    plt.gca().add_patch(square)
# square = plt.Rectangle(xy=(100, 100), width=0.2, height=0.2, alpha=0.8, angle=0.0,color='blue')
# plt.gca().add_patch(square)

#========画上解的路线即可.

jie=start_luxian[0]
x=1
y=1
font={'family':'serif',
     'style':'italic',
    'weight':'normal',
      'color':'red',
      'size':6
}
# plt.text((y+0.5)*kuan,(len(ditu[0])-x-0.5)*kuan,color='red',s='1',fontdict=font)


print('jie',jie)
for i in range(len(jie)-1):
   aaaa=jie[i]
   bbbb=jie[i+1]
   dx=bbbb[1]-aaaa[1]

   dy=bbbb[0]-aaaa[0]
   dy=-dy
   plt.arrow((aaaa[1]+0.5)*kuan,(len(ditu[0])-aaaa[0]-0.5)*kuan,kuan*dx,kuan*dy,color='red',head_width=0.007,length_includes_head=True)
plt.show()





