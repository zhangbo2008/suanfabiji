'''

1. 详细介绍一下各种排序算法，以及对应的时间复杂度。

  冒泡排序（Bubble Sort）

基本思想：通过相邻元素之间的比较和交换，使每一趟最大的元素能像气泡一样“浮”到数列的一端。
时间复杂度：
最优情况：O(n)
平均情况：O(n^2)
最坏情况：O(n^2)
空间复杂度：O(1)

nums=[1,2,3,4]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
          nums[i],nums[j]=nums[j],nums[i]


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

def best(rna):
    n = len(rna)
    dp = [[0] * n for _ in range(n)] # str[i,j]中的最长匹配个数. 闭区间
    brackets = [['.'] * n for _ in range(n)] # str[i,j]中最长匹配的解,闭区间.

    for length in range(1, n): # length表示匹配的长度.#========这个必须对length做动态规划.从而让137行的代码, 先把长度为短的部分给算完.
        for i in range(n - length): #i代表匹配的开始位置, j表示匹配的结束位置.
            j = i + length
            if (rna[i] == 'A' and rna[j] == 'U') or (rna[i] == 'U' and rna[j] == 'A') or (rna[i] == 'G' and rna[j] == 'C') or (rna[i] == 'C' and rna[j] == 'G') or (rna[i] == 'G' and rna[j] == 'U') or (rna[i] == 'U' and rna[j] == 'G'):
                dp[i][j] = dp[i + 1][j - 1] + 1
                if j-i==1: #初始情况就直接写()
                    brackets[i][j] ='()'
                else: #进行递归合并.

                    brackets[i][j] = '('+brackets[i+1][j-1]+')' #字符串的i和j匹配成功.
                

            for k in range(i, j): #用k来把i,j分割成2个部分.
                if dp[i][j] < dp[i][k] + dp[k + 1][j]:#如果分割后有更长匹配,那么更新表.
                    dp[i][j] = dp[i][k] + dp[k + 1][j]
                    brackets[i][j] = brackets[i][k] + brackets[k + 1][j]

    return dp[0][n - 1], brackets[0][n - 1]
print(best('GCACG'))
print(best('UUCAGGA'))
print(best('GUUAGAGUCU'))
print(best('AUAACCUUAUAGGGCUCUG'))
print(best('AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU'))
print(best('GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG'))
print(best('CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU'))
print(best('ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC'))
print(best('AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA'))