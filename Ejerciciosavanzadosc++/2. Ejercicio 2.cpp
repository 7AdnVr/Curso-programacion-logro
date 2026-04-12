#include <iostream>
using namespace std;

class InstalacionIndustrial {
protected:
    string id;
};

class ReactorQuimico : public InstalacionIndustrial {
private:
    double presionInterna;
public:
    ReactorQuimico() {
        presionInterna = 0;
    }

    void inyectar(double cantidad) {
        if(presionInterna + cantidad < 100) {
            presionInterna += cantidad;
        } else {
            cout << "Sobrepresion" << endl;
        }
    }

    double limite(int fase) {
        switch(fase) {
            case 1: return 80;
            case 2: return 120;
            case 3: return 60;
        }
        return 0;
    }
};

int main() {
    ReactorQuimico r;
    int op;
    do {
        cin >> op;
        if(op == 0) break;
        r.inyectar(10);
    } while(true);
    return 0;
}