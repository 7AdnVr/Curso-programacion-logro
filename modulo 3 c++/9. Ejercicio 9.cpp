#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> comidas(3);
    for(int i = 0; i < 3; i++) {
        cin >> comidas[i];
    }
    for(int i = 0; i < 3; i++) {
        cout << comidas[i] << endl;
    }
    return 0;
}