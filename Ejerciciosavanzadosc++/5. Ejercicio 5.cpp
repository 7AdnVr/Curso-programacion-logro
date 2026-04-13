#include <iostream>
using namespace std;

class MaquinariaPesada {
protected:
    string id;
};

class IncineradorInteligente : public MaquinariaPesada {
private:
    double temperaturaHorno;
public:
    IncineradorInteligente() {
        temperaturaHorno = 0;
    }

    void precalentar() {
        while(temperaturaHorno < 50) {
            temperaturaHorno += 5;
        }
    }

    bool procesar(int material) {
        switch(material) {
            case 1:
                if(temperaturaHorno >= 100) return true;
                else return false;
            case 2:
                if(temperaturaHorno >= 200) return true;
                else return false;
            case 3:
                if(temperaturaHorno >= 80) return true;
                else return false;
        }
        return false;
    }
};

int main() {
    IncineradorInteligente i;
    int m;
    do {
        cin >> m;
        if(m == 0) break;
        i.precalentar();
        i.procesar(m);
    } while(true);
    return 0;
}