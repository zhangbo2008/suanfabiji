#include<bits/stdc++.h>
using namespace std;



// 整数二分算法模板 —— 模板题 AcWing 789. 数的范围
bool check(int x) {/* ... */} // 检查x是否满足某种性质

// 区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：
//也就是每次查找如果我们要把符合的东西, 在他左边继续找.那么mid成功了我们就区间变成[l,mid]
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;//取一半偏左的.因为只有这样才分得均匀. 否则你取中间偏右一点的. 那么 [l,mid] 就明显比 [mid+1,r] 长度大. 分得均匀越不容易出错.
        if (check(mid)) r = mid;    // check()判断mid是否满足性质,我们就在他左边继续找.
        else l = mid + 1;
    }
    return l;
}