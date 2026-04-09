#include <iostream>
using namespace std;

const double PI = 3.14159;

void calcularPerimetro(double r) {
    cout << 2 * PI * r << endl;
}

int main() {
    double radio;
    cin >> radio;
    calcularPerimetro(radio);
    return 0;
}