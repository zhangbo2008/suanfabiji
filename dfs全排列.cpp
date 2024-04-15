#include<iostream>
using namespace std;
const int n = 3;
int a[n];
bool visit[n];
void dfs(int step){
	if(step >= n){
		for(int i = 0; i < n; i++){
			 cout << a[i] << " ";
		}
		cout << endl;
		return;
	}
	for(int i = 0; i < n; i++){
		if(!visit[i]){
			visit[i] = true;
			a[step] = i + 1;
			dfs(step + 1);
			visit[i] = false;
		}
	}
	return;
}
int main() {
    dfs(3);
}
