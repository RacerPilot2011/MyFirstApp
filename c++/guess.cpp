#include <iostream>
#include <time.h>
#include <unistd.h>
#include <stdio.h>
#include "clear.h"
using namespace std;
void again(){
    cout << "Do you want to play again?\n";
    string answer;
    if (answer == "yes" or "Yes"){
        system("./guess");
    }
    if (answer == "no" or "No"){
        cout << "Exiting...";
        sleep(2);
         #ifdef _WIN32
        EXITW();
        #elif __APPLE__ || __unix__
        EXITMAL();
        #endif
    }
}
void game(){
    for (;;){
    cout << ("What is you guess?\n");
    int guess;
    cin >> guess;
    srand(time(0));
    int number = rand()% 100;
    if (guess == number){
        cout << ("You guessed the number!\n");
        break;
    }
    else if (guess < number){
        cout << ("Less than\n");
    }
    else if (guess > number){
        cout << "Greater than\n";
    }
    }
    again();
}
int main(){
    cout << ("Welcome to the guessing game!\n");
    sleep(1);
    game();
}