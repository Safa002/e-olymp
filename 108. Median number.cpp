#include <iostream>
using namespace std;
int main(){
	int a,b,c,min,max,orta;
	cin>>a>>b>>c;
	min=a;
	if(b<min) {min=b;
	}
	if(c<min) {min=c;
	}
	max=a;
	if(b>max) {max=b;
	}
	if(c>max) {max=c;
	}
	orta =a+b+c - min - max;
	
	cout<<orta<<endl;
	return 0;
}
