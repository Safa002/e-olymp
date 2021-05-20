#include <stdio.h>
int main() {
    int a,n;
    long long result=1;
    scanf("%d", &a);
    scanf("%d", &n);
    while (n != 0) {
        result *= a;
        --n;
    }
    printf("%lld", result);
    return 0;
}
