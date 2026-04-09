#include <iostream>
using namespace std;

int main() {
    int op;
    do {
        cin >> op;
        switch(op) {
            case 1: cout << "Hola" << endl; break;
            case 2: cout << "Adios" << endl; break;
            case 3: break;
        }
    } while(op != 3);
    return 0;
}