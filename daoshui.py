# 抖音上面又来了一个倒水游戏


# 例子: 3个杯子, 容量12, 9, 5 上来12是满的. 然后都没有刻度只能倒到一个满这种倒法, 然后最后希望倒出2个6ml的.


# 这种很类似华容道. 暴力搜一下

#===============这部分需要每次题目给出!!!!!!!!!!!!!
# 维护一下rongliang和开始状态
rongliang=[12,9,5,5,3]
kaishi=[10,0,0,5,2]
end =[6,6,5,0,0] # 




# 显然这是一个马尔科夫过程, 对于kaishi数组进行维护即可.
# 还是使用bfs, 因为这种不会stackoverflow

history=[kaishi]
par=[0] # 指向父指针的索引
lastdex=0
def one_step():
   # 进行一次倒水,遍历所有倒水情况.
   for i in range(lastdex,len(history)):
      tmp=history[i]
      # 尝试新的方式倒水
      for src in range(len(rongliang)):
          for to in range(len(rongliang)):
             src_bottle=tmp[src]
             to_bottle=tmp[to]
             src_cap=rongliang[src]
             to_cap=rongliang[to]
             #=判断是否可以倒水
             if src_bottle!=0 and to_bottle!=to_cap:
                #==========这时候可以倒水.
                daoshuliang=to_cap-to_bottle
                have_shuiliang=src_bottle
                daoshuliang=min(daoshuliang,have_shuiliang)
                # 拼接新的状态
                new_state=tmp.copy()
                new_state[src]-=daoshuliang
                new_state[to]+=daoshuliang
                if new_state not in history:
                  history.append(new_state) # 不用担心死循环. len(history) 到这行时候就赢锁定这个长度了. 用常数替代了.
                  par.append(i)
for i in range(100):
  one_step()
  if end in history:
     dex=history.index(end)
     #========通过par来反解
     lujing=[dex]
     while 0 not in lujing:
        dex=par[dex]
        lujing .append(dex)
     print(f'第{i}次bfs找到了你要的答案,并且算法bfs保证了这个是最少倒水次数')
     print([history[jj] for jj in   lujing[::-1] ])
     break
else:
  print('遍历了100次都找不到你要的答案,可能问题过于复杂或者无解!')

             

# PS C:\Users\admin\Desktop\fucking-algorithm-master> & d:/Users/admin/miniconda3/python.exe c:/Users/admin/Desktop/fucking-algorithm-master/daoshui.py
# 第7次bfs找到了你要的答案,并且算法bfs保证了这个是最少倒水次数
# [[12, 0, 0], [7, 0, 5], [7, 5, 0], [2, 5, 5], [2, 9, 1], [11, 0, 1], [11, 1, 0], [6, 1, 5], [6, 6, 0]]
# PS C:\Users\admin\Desktop\fucking-algorithm-master> 


















       
   














