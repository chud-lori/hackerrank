#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
	int n;
	cin >> n;
	int a[n];
	//for(int i=0; i <= n-1; i++){
	//	cin >> a[i];
	//}
	n -= 1;
	cout << n;
	do {
		cin >> a[n];
		n--;
	}while(n=0);
	cout << a[0];
    return 0;
}

