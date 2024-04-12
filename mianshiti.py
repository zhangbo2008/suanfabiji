'''

1. 详细介绍一下各种排序算法，以及对应的时间复杂度。

  冒泡排序（Bubble Sort）

基本思想：通过相邻元素之间的比较和交换，使每一趟最大的元素能像气泡一样“浮”到数列的一端。
时间复杂度：
最优情况：O(n)
平均情况：O(n^2)
最坏情况：O(n^2)
空间复杂度：O(1)


选择排序（Selection Sort）

基本思想：首先在未排序序列中找到最小（或最大）元素，存放到排序序列的起始位置，然后再从剩余未排序元素中继续寻找最小（或最大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
时间复杂度：
最优情况：O(n^2)
平均情况：O(n^2)
最坏情况：O(n^2)
空间复杂度：O(1)


插入排序（Insertion Sort）

基本思想：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
时间复杂度：
最优情况：O(n)
平均情况：O(n^2)
最坏情况：O(n^2)
空间复杂度：O(1)


希尔排序（Shell Sort）

基本思想：先将整个待排序的记录序列分割成为若干子序列（由相隔某个“增量”的记录组成）分别进行直接插入排序，然后依次缩减增量再进行排序，待整个序列中的记录“基本有序”时，再对全体记录进行一次直接插入排序。
时间复杂度：依赖于增量序列的选择，但通常介于O(n)和O(n^2)之间。
空间复杂度：O(1)


归并排序（Merge Sort）

基本思想：采用分治法的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
时间复杂度：
最优情况：O(n log n)
平均情况：O(n log n)
最坏情况：O(n log n)
空间复杂度：O(n)（非原地排序）


快速排序（Quick Sort）

基本思想：通过一次排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
时间复杂度：
最优情况：O(n log n)
平均情况：O(n log n)
最坏情况：O(n^2)（当输入的数据已经有序时）
空间复杂度：O(log n)（递归栈空间）


堆排序（Heap Sort）

基本思想：将待排序的序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个序列重新构造成一个堆，这样会得到n个元素中的次大值。如此反复执行，便能得到一个有序序列了。
时间复杂度：
最优情况：O(n log n)
平均情况：O(n log n)
最坏情况：O(n log n)
空间复杂度：O(1)


计数排序（Counting Sort）

基本思想：对于待排序的数组，如果最大值和最小值的差值不是太大，那么可以通过申请一个计数数组，将输入数据值转化为键存储在计数数组中，然后输出计数数组。
时间复杂度：
最优情况：O(n+k)（k是整数的范围）
平均情况：O(n+k)
最坏情况：O(n+k)
空间复杂度：O(n+k)

2. 在RNA序列中，例如ACAGU，我们可以通过标记每个核苷酸为 (、. 或 ) 来预测其二级结构。每对匹配的 () 必须是AU、GC或GU（或它们的镜像对称：UA、CG、UG）。我们还假设配对不能交叉。以下是ACAGU的有效结构：

   ACAGU
   .....
   ...()
   ..(.)
   .(.).
   (...)
   ((.))    

   在上面的例子中，最后一个结构是最优的（2对）。

   >>> best("ACAGU")
   (2, '((.))')

   在RNA序列的二级结构预测中，如果存在多个最佳结构，可以任意选择其中一个作为结果，只要这个结构是正确的。这里列出了一些其他的案例以及最佳结构的示例：

   GCACG
   (2, '().()')
   UUCAGGA
   (3, '(((.)))')
   GUUAGAGUCU
   (4, '(.()((.)))')
   AUAACCUUAUAGGGCUCUG
   (8, '.(((..)()()((()))))')
   AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU
   (11, '(((.(..(.((.)((...().))()))))))')
   GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG
   (14, '.()()(()(()())(((.((.)(.))()))))')
   CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU
   (18, '(()())(((((.)))()(((())(.(.().()()))))))')
   ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC
   (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
   AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA
   (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')

   请写出一个算法，语言不限。

'''





# acagu 中找:au, gc, gu,  ua, cg, ug
#    从开始a找到匹配之后, 动态规划, 组合等于现在的再加上 内部找, 或者右边找.拼上.


def one(shuru):
    #全部的单次匹配.
    out=[]
    for i in range(len(shuru)):
        for j in range(i+1,len(shuru)):
            if [shuru[i],shuru[j]] in [['A','U'], ['G','C'],['G','U'],['U','A'],['C','G'],['U','G']]:
                out.append([i,j])
    return out



    

#=======计算两个线段的关系是否重叠
def panding(a,b):
    # 完全覆盖另一个
    if a[0]<b[0] and a[1]>b[1]:
        return True
    if b[0]<a[0] and b[1]>a[1]:
        return True
    if a[1]<b[0] or b[1]<a[0]:
        return True
    return False
def panding2(j,b): #b是否能加入j里面
    for i1 in j:
        if panding(i1,b)==False:
            return False
    return True


print(one('acagu'))
shuru='AGGCAUCAAACCCUGC'
all_combine=one(shuru)


tmp=[[i] for i in all_combine]
for i in all_combine:
    #=====至多进行这么多次组合
    next_step=[]
    for j in tmp:
        for test_add in all_combine:
            #判断test_add是否能加入j里面.
            if panding2(j,test_add):
              next_step.append(j+[test_add])  
    if next_step==[]:
        print(tmp[0]) #=======加到最后会有加不到的.
        break
    tmp=next_step
    # print(1)



























