#include <iostream>
#include <cmath>
using namespace std;
int main()
{

int a,b,c,d,hasil;
cin>>a;
if(a>=100 && a<=999){
b=a/100;
c=(a/10)%10;
d=(a%10);
hasil= b*c*d;
cout<<hasil<<endl;
}
}
