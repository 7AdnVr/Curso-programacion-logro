#include <iostream>
using namespace std;

class DispositivoRed {
protected:
    string nombre;
};

class RouterCore : public DispositivoRed {
private:
    int paquetesDescartados;
    int total;
public:
    RouterCore() {
        paquetesDescartados = 0;
        total = 0;
    }

    void rutear(int puerto) {
        switch(puerto) {
            case 80: total++; break;
            case 21: total++; break;
            case 25: total++; break;
            default: paquetesDescartados++; total++; break;
        }
    }

    string estado() {
        if(total > 0 && paquetesDescartados > total * 0.1) {
            return "Congestion Severa";
        } else {
            return "Estable";
        }
    }
};

int main() {
    RouterCore r;
    int p;
    while(true) {
        cin >> p;
        r.rutear(p);
        if(r.estado() == "Congestion Severa") {
            break;
        }
    }
    return 0;
}