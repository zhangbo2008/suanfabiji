#股票
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

prices=[7,1,5,3,6,4]
# dp[i][j] 表示第i天时候 j=0 没有股票时候的收益, j=1表示拥有股票的收益.
dp=[[0,0] for i in prices]

dp[0][0]=0
dp[0][1]=-prices[0]

for i in range(1,len(prices)):
     # 买
     dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])
     #mai
     dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
print(dp[len(prices)-1][0])



# https://leetcode.cn/problems/house-robber/

nums=[1,2,3,1]
dp=[0 for i in nums] #一共i个房子,最后一个房子必偷时候的利润.
dp[0]=nums[0]
dp[1]=nums[1]

for i in range(2,len(nums)):
     dp[i]=dp[i-2]+nums[i]

print(max(dp))














# class Solution {
#     public int superEggDrop(int K, int N) {
#         return Solution.recursive(K, N);
#     }
    
#     public static int recursive(int K, int N) {
#         if (N == 0 || N == 1 || K == 1) {
#             return N;
#         }

#         int minimun = N;
#         for (int i = 1; i <= N; i++) {
#             int tMin = Math.max(Solution.recursive(K - 1, i - 1), Solution.recursive(K, N - i));
#             minimun = Math.min(minimun, 1 + tMin);
#         }
#         return minimun;
#     }
# }

# 作者：byMax
# 链接：https://leetcode.cn/problems/super-egg-drop/solutions/7459/ji-dan-diao-luo-xiang-jie-by-shellbye/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



print('==================')

nums = [5,7,7,8,8,10]
# nums = [5,8,8,8,8,10,11,12,13]
target = 8

left=0
right=len(nums)-1

while (left<=right):
     if right-left<=1:
          break
     mid=left+right>>1
     if nums[mid]<target:
          left=mid
     if nums[mid]>=target:
          
          right=mid
print(mid)


'''快速排序'''
'''我最新理解是,给数组头和尾两个指针,
然后分别向中间跑,如果发现逆序就交换,一直交换到指针相碰就停止就写好了fenge函数'''
#关键就是这个分割函数的写法
def fenge(a):
      left=0
      right=len(a)-1
      tmp=a[0]#tmp就是分割的点的值
      for i in range(len(a)):
            if left==right: #主体思想是2重循环来写,然后每一个循环都先加入break条件.
                  break
            while 1:
                  if left==right:
                   break
                  if a[right]<tmp:  #如果有反序就交换过来
                        
                        a[right],a[left]=a[left],a[right]
                        break
                  else:
                        right-=1
            while 1:           #更上面完全类似了.
                  if left==right:
                   break
                  if a[left]>tmp:
                        
                        a[right],a[left]=a[left],a[right]
                        break
                  else:
                        left+=1
      
      return a,left    
def sort(a):
      if len(a)==0:
            return []
      if len(a)==2:
            if  a[0]>a[1]:
                  return [a[1],a[0]]
            else:
                  return a
      if len(a)==1:
            return a
      a,left=fenge(a)
      #[a[left]]把一个数变成数组
      return sort(a[:left])+[a[left]]+sort(a[left+1:])
a=[34,57,4,101,5,97,99,234,3423423]
import random
a=range(1,10000)
a=list(a)
random.shuffle(a)

print (sort(a)[:100])#百万级别还是有点慢大概10s不到的样子












#线段树:线段树的基本定义:线段树是解决数列维护问题的一种常用手段.基本能保证每一个操作
#的复杂度都是O(logn)的级别.而我们知道正常一个数组的查询是需要O(n)的也就是遍历.
'''所以当n的级别很大到10亿以上,如果我们还需要1s内解决问题就需要用线段树来查询和修改'''
'''对于二叉树而言:n0表示叶子节点的数目,n1为度为1的节点数目,n2为度为2的节点数目,
边的数目S=n1+2*n2'''
'''度为0的节点数比度为2的节点数多1:证明:首先二叉树中子树的节点有n1+2n2个,所以二叉树的
总共节点数是1+n1+2n2,另外一种是n0+n1+2n2,所以证毕,并且也知道一个结论是二叉树的
节点数比边数多1'''
'''利用上面2个结论我们知道线段树这个2叉树的节点数目是2n-1'''


'''线段树处理这样的问题:
把问题简化一下：

在自然数，且所有的数不大于30000的范围内讨论一个问题：现在已知n条线段，把端点依次输入告诉你，然后有m个询问，每个询问输入一个点，要求这个点在多少条线段上出现过；

最基本的解法当然就是读一个点，就把所有线段比一下，看看在不在线段中；

每次询问都要把n条线段查一次，那么m次询问，就要运算m*n次，复杂度就是O(m*n)

这道题m和n都是30000，那么计算量达到了10^9；而计算机1秒的计算量大约是10^8的数量级，所以这种方法无论怎么优化都是超时

—–

因为n条线段是固定的，所以某种程度上说每次都把n条线段查一遍有大量的重复和浪费；

线段树就是可以解决这类问题的数据结构

举例说明：已知线段[2,5] [4,6] [0,7]；求点2,4,7分别出现了多少次'''

'''http://hzwer.com/670.html
下面我写的不清楚就继续看上面这个url,又是一个不懂感觉很神秘,懂了感觉很平凡的东西.发明的
人还是吊.
这个网址上面的题目和代码,从他的分析可以看出
用线段树把原来O(mn) 的算法变成了O(mlog30000+nlog30000)   的算法,m和n也都取成3万,
那么我们有左边是10亿右边是几十万,这就是线段树的快捷地方,他快捷的本质是其实不用每一次都
重新问一个数字是否在一个线段里面,而只需要把线段的信息都一次储存好,然后直接询问每一个
要找的数字即可'''

#下面开始实现这个问题
#每一个节点
class jiedian:
      def __init__(self,start,end):
            self.start,self.end=start,end
            self.left,self.right=None,None
            self.count=0#在这个题目里面作为计数的工具使用
#创立这个二叉树,我们问题里面start就是0,end就是30000,因为是线段
#所以需要包含端点,0是自然数.
def build(start,end):
      if start>end:
            return None
      root=jiedian(start,end)
      if start==end:
            return root
      root.left=build(start,(start+end)//2)
      root.right=build((start+end)//2+1,end)
      return root
#下面我们就开始创立我们的简单例子里面[0,7]这个线段树.
a=build(0,7)

#下面我们写一个把一个区间插入到线段树里面的函数,然后把对应的拆分的count+1
#对于插入的区间要分类讨论,比如我插入一个[-99,0]的这种不合逻辑的也需要加强程序鲁邦性.
def charu(root,start,end):#用函数的封装root来实现迭代
            if start<root.start:
              start=root.start
            if end >root.end:
              end=root.end
            if root.start==start and root.end==end:
                  root.count+=1
                  return 
            if root.start>end:
                  return 
            if root.end<start:
                  return 
            if end<=root.left.end:
                  charu(root.left,start,end)
            if start>=root.left.end+1:
                  charu(root.right,start,end)
##charu(a,-99,99)
##print (a.count)#经过实验这里面成功输出1这个数字.基本上讨论了所有情况.
#下面写查询代码即可,相类似.因为这个题目只是每一次找一个数字不是区间所以比上面更容易一点.
def chaxun(root,obj):
      if obj>root.end:
            return 0
      if obj<root.start:
            return 0
      if obj==root.start==root.end:
            return root.count
      if obj<=(root.start+root.end)//2:
            return chaxun(root.left,obj)+root.count
      if obj>=(root.start+root.end)//2+1:
            return chaxun(root.right,obj)+root.count
#下面开始重头插入和查询
charu(a,-99,0)
charu(a,-99,0)
charu(a,-99,0)
charu(a,-99,0)
charu(a,-99,1)
answer=chaxun(a,1)
print (answer)
print(chaxun(a,0))






##http://www.cnblogs.com/mycapple/archive/2012/08/09/2630430.html
'''下面我们继续搞树状数组,也就是数组树'''
'''传统数组(共n个元素)的元素修改和连续元素求和的复杂度分别为O(1)和O(n)。树状数组通过将线性结构转换成伪树状结构（线性结构只能逐个扫描元素，而树状结构可以实现跳跃
式扫描），使得修改和求和复杂度均为O(lgn)，大大提高了整体效率。'''
'''这个东西很神秘,数学上很深.
比如一个数组有8个元素记作a1,....a8
那么做一个新数组c,要求这个数组能加出a1到an的任何一个sum n从1到8
并且这个数组的生成最快,做的运算最少来得到这个数组c'''
'''这个数组是
c1=a1
c2=a1+a2
c3=a3
c4=a1+a2+a3+a4
c5=a5
c6=a5+a6
c7=a7
c8=a1+a2+a3+a4+a5+a6+a7+a8'''
'''对于这个c数组如何找到很神秘'''
'''https://www.cnblogs.com/hsd-/p/6139376.html'''
'''上面这个微博里面的图形很形象表现出来了,
我保存到了2.png'''#ps:从这里面说明我想做的ide带图片的多重要,不然神他妈能说清楚.
'''也就是上面这个链接从上往下数的第五个picture,说的很明白了,图里面你从上往下看,
看这个树,他的第一个元素就是c数组里面需要的元素.真心形象.也保证了这个树的每一个列都取
一个,因为 我们只取最北的那一个就行了'''
'''那么问题来了,改如何证明?感觉还是一个图论的问题,还是从树上入手
1.首先这种取法能保证任何a1加到an都能分解成c里面的和,这很显然,因为
从树这个图能看出来任何的求和,也就是最下面一排的取一个a1到am,都可以分解c里面的和'''
'''2.还需要证明这种c的算法最节约时间的,首先2分是显然的思路,3分或者更高显然速度慢,
所以我们只需要讨论图里面为什么c不选其他的点就行了.那么只需要讨论一个,比如c4就可以了
,我们假设c4不取到最北的点,比如c4取为他下面一个点也就是c4=a3+a4,
这样显然我们如果其他点都不变的话,a1,a1+a2,a1+a2+a3的计算次数
都没变化,但是a1+a2+a3+a4的计算次数多一次.
再看后面a1+a2+a3+a4+a5也是要多一次,归纳法显然后面的嘉禾都多一次,
所以时间复杂度加了O(N),所以变差了,再用归纳法对c4,c5...做归纳,就得到这种算法是最快
的结论,证毕.当然这只是一个初步证明,话说我就喜欢骗自己,当不会证明时候也非要写一种伪证明
来骗自己,否则不敢用.总怕有反例,然而骗自己证明了就随便用...总感觉不证明的东西,用起来
总保证不了是最好的算法,不够完美.'''
'''代码实现都是很多数学推导利用二进制来进行拆分,写了也记不住,只写到理解算法的层面了.'''


'''没什么人用的排序算法,都是一些特俗东西,设计还算巧妙'''
'''计数排序:
比如有4455676,那么就开一个长度为8的数组a,
a[0]表示0出现的次数,所以这个数组结果是00002221,
然后显然再O(N)把数据生成出来即可'''
def count_sort(data,max):#需要实现知道上界才好用
      a=[0]*(max+1)
      b=[]
      for i in range(len(data)):
            a[data[i]]+=1
      for i in range(len(a)):
            for j in range(a[i]):
                  b.append(i)
      return b
print (count_sort([1,5,5,7,8,9,0],9))#太简单了.












'''桶排序:针对大数据的排序,非常重要!!!!!!'''
'''思路就是先把数据进行切分,假设数据在一个区间上是均匀分布的,那么比如先弄10个桶代表这些小区间,
然后每一个桶内部都分好了,之后再拼起来即可'''
def bucket_sort(data,max,min):
    num_of_bucket=3
    interval=(max-min)/num_of_bucket
    a=[]
    #建立桶:
    c=[]
    for i in range((num_of_bucket)):
        c.append([])
    for i in range((num_of_bucket)+1):
             a.append(min+i*interval)
    print (a)
    for i in range(len(data)):
        for j in range(1,len(a)):
            if data[i]==a[0]:
                c[0].append(data[i])
                break
            if data[i]<=a[j]:
                c[j-1].append(data[i])
                break

    for i in range(len(c)):
        c[i]=sorted(c[i])
    return c
import numpy as np
a=np.random.rand(30)



d=bucket_sort(a,1,0)
print (d)#搞定桶排序



'''一个利用1.5N的时间同时找到数组里面最大值和最小值的算法'''
'''思想就是做一个对(ai,ai+1),把他里面大的跟tmpbig比,小的跟tmpsmall比,所以用3次比了2个元素.'''
def max_and_min(a):
      if len(a)==1:
            return a[0],a[0]
      else:
            tmpbig=max(a[0],a[1])
            tmpsmall=min(a[0],a[1])
            for i in range(2,len(a)-1,2):
                  if a[i]<=a[i+1]:
                        tmpbig=max(tmpbig,a[i+1])
                        tmpsmall=min(tmpsmall,a[i])
                  if a[i]>a[i+1]:
                        tmpbig=max(tmpbig,a[i])
                        tmpsmall=min(tmpsmall,a[i+1])
      return tmpbig,tmpsmall
print (max_and_min([1,4,65,87,45,4,54,5,45,45]))