#include <iostream>
#include <string>
#include <sstream>
#include <time.h>
#include <unistd.h>
#include <stdio.h>
#include "clear.h"
using namespace std;
int cal()
{
    for (;;){ 
    int Num1; 
    int Num2;
    char op;
    cout << "What do you want to be calculated?\n";
    cin >> Num1 >> op >> Num2;
    if (op == '+'){
        double result = Num1 + Num2;
        cout << "Your anwswer  is: " << result << "\n";
    }
    if (op == '-'){
        double result = Num1 - Num2;
        cout << "Your anwswer  is: " << result<< "\n";
    }
    if (op == '*'){
        double result = Num1 * Num2;
        cout << "Your anwswer  is: " << result<< "\n";
    }
    if (op == '/'){
        double result = Num1 / Num2;
        cout << "\nYour anwswer  is: " << result<< "\n";
    }
    if (op == 'e'){
        break;
    }
}
return 0;
}
int main(){
    cout << "Welcome to the calculator!\n";
    sleep(1);
    cout << "You get as many calculations as you want. Just remember to type 1e1 when you want to exit.\n";
    sleep(1);
    cal();
}