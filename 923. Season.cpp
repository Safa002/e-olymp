#include <iostream>
using namespace std;
int main(){
	int a;
	cin >> a;
	cout << ((a % 12) < 3 ? "Winter" : (a % 12) < 6 ? "Spring" : (a % 12) < 9 ? "Summer" : "Autumn");
	return 0;
}
