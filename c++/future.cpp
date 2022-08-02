#include <iostream>
#include <time.h>
#include <unistd.h>
#include <stdio.h>
#include "clear.h"
using namespace std;
void ask(){
    int i = 0;
    while(i < 3){
    i = i + 1;
    srand(time(0));
    cout << "What future do you want to be fortold?\n";
    string input;
    getline(cin, input);
    cout << "Seeing the future...\n";
    sleep(2);
    int determiner = rand()% 4;
    if (determiner == 1) {
        cout << "My sources say yes.\n";
    }else if (determiner == 2){
        cout << "Sorry, no.\n";
    }else {
        cout << "The future is foggy, please ask again later.\n";
    }
    sleep (1);
    if (i == 1){
        cout << "2 futures left.\n";
        sleep(1);
    }else if (i == 2){
        cout << "1 future left.\n";
        sleep (1);
    }
}

    #ifdef _WIN32
    EXITW();
    #elif __APPLE__ || __unix__
    EXITMAL();
    #endif
}
int main(){
    #ifdef _WIN32
    W();
    #elif __APPLE__ || __unix__
    MAL();
    #endif
    cout << "Welcome to the future-telling program!!\n";
    sleep(2);
    ask();  
}


