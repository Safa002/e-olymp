#include <iostream>

using namespace std;
int main()
{
	int n,r,cem=0;
	cin>>n;
	if(n<0) {
		n=(-1)*n;
	}
	aa:
		r=n%10;
		cem= cem+r;
		n/=10;
		if(n!=0)goto aa;
		cout<<cem<<endl;
		return 0;
}
