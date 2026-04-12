#include <iostream>
using namespace std;

class TanqueAgua {
private:
    int capacidadMaxima;
    int nivelActual;
public:
    TanqueAgua(int capacidad) {
        capacidadMaxima = capacidad;
        nivelActual = 0;
    }

    int getNivelActual() {
        return nivelActual;
    }

    int getCapacidadMaxima() {
        return capacidadMaxima;
    }

    void llenarTanque(int flujo) {
        if(nivelActual + flujo <= capacidadMaxima) {
            nivelActual += flujo;
        } else {
            nivelActual = capacidadMaxima;
        }
    }
};

int main() {
    TanqueAgua t(100);
    while(t.getNivelActual() < t.getCapacidadMaxima()) {
        t.llenarTanque(10);
        cout << t.getNivelActual() << endl;
    }
    return 0;
}