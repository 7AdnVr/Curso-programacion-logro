#include <iostream>
using namespace std;

float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura;
    cin >> base >> altura;
    cout << calcularAreaRectangulo(base, altura) << endl;
    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}