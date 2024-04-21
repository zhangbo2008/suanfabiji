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






// 区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}

// 作者：yxc
// 链接：https://www.acwing.com/blog/content/277/
// 来源：AcWing
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。









//problem1:


bool check1(int x) {return x>3;} 
int bsearch_11(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        cout<<"=============="<<endl;
        cout<<mid<<endl;     //4
        cout<<l<<endl;       //3
        cout<<r<<endl;      //4
        if (check1(mid)) r = mid;   
        else l = mid + 1;
    }
    return l;
}




bool check2(int x) {return x<3;} 
int bsearch_22(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;
        if (check2(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
}

int main(){
puts("第一个问题我们找区间里面比a大的数里面最小的");
puts("因为我们找到匹配的后,要在他左边继续寻找所以我们用模板1");
cout<<bsearch_11(0,7)<<endl;



puts("第2个问题我们找区间里面比a小的数里面最大的");
puts("因为我们找到匹配的后,要在他左边继续寻找所以我们用模板1");
cout<<bsearch_22(0,7)<<endl;


// 最后我们来理解一半的思想.
//假设我们对1234做二分查找. 那么我们mid=2.5
//假设我们不做[1,2]  [3,4] 的划分. 我们做[1]  [2,3,4] 的划分.
//其实这种不管好坏,首先效率就达不到最优.



}