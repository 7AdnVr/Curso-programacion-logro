#include <iostream>
using namespace std;

class NaveExploracion {
protected:
    string modelo;
};

class SondaAutonoma : public NaveExploracion {
private:
    double desviacionTrayectoria;
public:
    SondaAutonoma() {
        desviacionTrayectoria = 0;
    }

    void corregir() {
        if(desviacionTrayectoria > 0) {
            desviacionTrayectoria -= 1;
        } else {
            desviacionTrayectoria += 1;
        }
    }

    double calcular(int tipo) {
        switch(tipo) {
            case 1: return 5;
            case 2: return 10;
            case 3: return 20;
        }
        return 0;
    }

    void aplicar(double d) {
        desviacionTrayectoria += d;
    }
};

int main() {
    SondaAutonoma s;
    for(int i = 0; i < 15; i++) {
        int t;
        cin >> t;
        double d = s.calcular(t);
        s.aplicar(d);
        s.corregir();
    }
    return 0;
}