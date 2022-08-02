#include <iostream>
#include "clear.h"
#include <unistd.h>
using namespace std;
#ifdef _WIN32
W());
#else
MAL();
#endif
int main(){
    cout << "Welcome to my c++ programs!\n";
    sleep(1);
    string an;
    cout << "Do you want to use the [C]alculator, play the [G]uessing Game, or ask the [F]uture Teller?(type letter)\n";
    cin >>  an;
    if (an == "F" or "f"){
        system("./future");
    }
    if (an == "C" or "c"){
        system("./calculator");
    }
    if (an == "F" or "f"){
        system("./future");
    }
}