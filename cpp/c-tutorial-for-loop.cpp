#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

const string number_map[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main() {

    int lb, ub;
    cin >> lb >> ub;

    for(int i = lb; i <= ub; i++) {
        if( i >= 1 && i <= 9 ) {
            cout << number_map[i-1] << endl;
        } else if(i > 9) {
            if(i % 2 == 0) {
                cout << "even" << endl;
            } else {
                cout << "odd" << endl;
            }
        }
    }

    return 0;
}


