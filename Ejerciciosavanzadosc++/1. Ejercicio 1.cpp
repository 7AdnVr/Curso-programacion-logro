#include <iostream>
using namespace std;

class EstacionMonitoreo {
protected:
    string nombre;
};

class NodoCentralSismico : public EstacionMonitoreo {
private:
    double energiaAcumulada;
public:
    NodoCentralSismico() {
        energiaAcumulada = 0;
    }

    void registrarOnda(int tipo) {
        switch(tipo) {
            case 1: energiaAcumulada += 10; break;
            case 2: energiaAcumulada += 20; break;
            case 3: energiaAcumulada += 30; break;
        }
    }

    bool riesgo() {
        if(energiaAcumulada > 100) {
            return true;
        } else {
            return false;
        }
    }
};

int main() {
    NodoCentralSismico nodo;
    for(int i = 0; i < 5; i++) {
        nodo.registrarOnda(1);
    }

    while(true) {
        int t;
        cin >> t;
        nodo.registrarOnda(t);
        if(nodo.riesgo()) {
            break;
        }
    }
    return 0;
}