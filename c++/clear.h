#include <iostream>
using namespace std;

int cscreen(){
    #ifdef _WIN32
    system("cls");
    return 0;
    #else
    system("clear");
    return 0;
    #endif
}
int EXITW(){
    system("cls");
    return 0;
}
int EXITMAL(){
    system("clear");
    return 0;
}