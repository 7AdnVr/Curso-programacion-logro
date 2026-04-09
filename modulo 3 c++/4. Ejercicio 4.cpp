#include <iostream>
#define LIMITE 10
using namespace std;

int main() {
    int n;
    cin >> n;
    for(int i = 1; i <= LIMITE; i++) {
        cout << n * i << endl;
    }
    return 0;
}