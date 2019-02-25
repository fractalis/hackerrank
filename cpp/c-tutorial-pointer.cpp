#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

void update(int *a,int *b) {
    int a_p = (*a), b_p = (*b);
    *a = a_p + b_p;
    *b = abs(a_p - b_p);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}


