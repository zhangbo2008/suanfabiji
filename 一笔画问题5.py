# 2024-04-15,12点34  改用 visited矩阵来记录, 还有一个path来记录当前dfs的路径, 空间复杂度下去了, 整个算法不超过一个G内存, 但是速度依然很慢, 如果暴力跑全部路径依然跑不完.
# ps:这个代码也是一个非常好的, 走迷宫代码. 等价于遍历迷宫中尽可能多的点,并且要求不走重复路.

# 2024-04-14,0点26 可能是空间复杂度太高, 改成用树来存储路径.

#=============一笔画问题.
import matplotlib.pyplot as plt

# 1表示可以走的路, 0表示墙






# 配置地图!!!!!!!!!!!


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






# ditu=[
# [1,1,1,1,0,1,1,1],
# [1,1,0,1,1,1,1,1],
# [1,1,1,1,1,0,1,1],
# [1,1,1,1,1,1,0,1],
# [1,0,1,1,1,1,1,1],
# [1,1,1,0,1,1,1,1],
# [1,1,1,1,1,1,0,1],
# # [1,1,1,0,0,1,1,1],
# # [1,1,1,1,1,1,1,0],
# ]


# ditu=[
#    [1,1,1,1],
#    [1,1,0,1]
# ]





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
# 每一个路径我们都要保存, 所以用多叉树结构来存所有路径
class node:
   def __init__(self,val):
      self.val=val  #自己的值=值是一个point
      self.children=[] # childre是node组成的数组.
      # self.par=None #指向父节点, 用于删除时候用.
      # self.visited=0



dx=[-1,1,0,0]
dy=[0,0,-1,1] #只能上下左右走.


#==========根据我们地图我们知道,度为1的点一定是起点!!!!!
#============我们的起点是一个根.
root=node([1,0])
#=====为了测试我们加一层.
# root.children=[node((7,1)),node((6,0))]


# start_luxian=root #使用tuple可以进行哈希.


# start_luxian=all_point  #如果我们没有度为1的点, 那么我们就只能设置为所有点都可能是起点了.

maxlen=0
early_quit=0
save_history=[]
#========2024-04-14,8点12 改成直接用dfs建立树

#=改成visited数组 替代history
visited=[[0]*len(ditu[0]) for i in ditu]
tmp_shendu=1 # 当前便利了多少了节点 #======改成不建立树, 直接走.
path=[]
def dfs(aaa):
    global maxlen
    global early_quit
    global save_history
    global visited
    global tmp_shendu
    global path
    if early_quit:
       return 
    #==========直接走下一步
    #========标记当前为走guo
    visited[aaa[0]][aaa[1]]=1
    path.append(aaa)
    #==跟踪最长路径
    if len(path)>maxlen:
        maxlen=len(path)
        print('当前最长路径长度',maxlen)
        save_history=path
   #============一笔画问题还是搜索空间太大. 无解了. 只能下面加一个提前结束.
    if maxlen==len(all_point):
                     early_quit=1#==让其他的dfs函数提前quit

                     return 
    for j in range(len(dx)):

               nx=[aaa[0]+dx[j],aaa[1]+dy[j]]
               if  0<=nx[0]<len(ditu) and  0<=nx[1]<len(ditu[0]) and visited[nx[0]][nx[1]]==0 and ditu[nx[0]][nx[1]]==1: #如果下一个点可以拓展
                   dfs(nx)
   #=====走到这里说明子路径都遍历玩了,那么去掉这个
    path=path[:-1]
    visited[aaa[0]][aaa[1]]=0









a=dfs([7,0])

print(1)












# for i in range(len(all_point)):#一共可以走这么多步:
#   print('当前推理:',i,'步',)
  
#   next_luxian=one_step(start_luxian)
#   if next_luxian==[]:
#     print('找到最长的路线了',start_luxian[0],'长度',len(start_luxian[0]),'走法一共有',len(start_luxian))
#     break
#   start_luxian=next_luxian

# print(1)


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

jie=save_history
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

plt.savefig('yibihua答案.png')
plt.show()





