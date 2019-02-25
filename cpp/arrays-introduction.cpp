#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, val;
    cin >> n;

    vector<int> intarr = {};

    for(int i = 0; i < n; i++) {
        cin >> val;
        intarr.push_back(val);
    }

    for(vector<int>::reverse_iterator ri = intarr.rbegin(); ri != intarr.rend(); ri++) {
        cout << *ri << " ";
    }

    return 0;
}
