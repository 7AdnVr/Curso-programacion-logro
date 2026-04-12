#include <iostream>
#include <string>
using namespace std;

class CajaFuerte {
private: 
    int pinSecreto;
    bool estadoAbierta;

public:

    bool intentarAbrir(int pin) {
    if (pin == pinSecreto) {
        estadoAbierta = true;
        return true;
    }
    else {
        return false;
    }
    }

    CajaFuerte(int pin) {
        pinSecreto = pin;
        estadoAbierta = false;
    }
};


int main() {
    CajaFuerte Pin(5312);

    int pinIngresado;
    bool abierto;

    do {
    cout << "Intenta adivinar el Pin -> ";
    cin >> pinIngresado;

    abierto = Pin.intentarAbrir(pinIngresado);

    if (!abierto) {
        cout << "PIN incorrecto" << endl;
    }

    } while (!abierto);
    cout << "Caja fuerte abierta" << endl;

}
    

