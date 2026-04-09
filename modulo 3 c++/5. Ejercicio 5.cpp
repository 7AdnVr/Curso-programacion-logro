#include <iostream>
using namespace std;

int main() {
    int numerosecreto = 42;
    int intento;
    cin >> intento;
    while(intento != numerosecreto) {
        if(intento < numerosecreto) {
            cout << "mas alto" << endl;
        } else {
            cout << "mas bajo" << endl;
        }
        cin >> intento;
    }
    return 0;
}