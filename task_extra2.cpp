
#include <iostream>
using namespace std; 
int main () 
{ 
    int x = 0;
    int y = 0;
    cout<<"insert something: ";
    cin>>x;
    cin>>y;
    
    if(x>0 and y>0){
        cout<<"1 square";
    }
    else if(x>0 and y<0){
        cout<<"2 square";
    }
    else if(x<0 and y< 0){
        cout<<"3 square";
    }
    else if(x<0 and y>0){
        cout<<"4 square";
    }
    else if(x>0 and y ==0){
        cout<<"12 line ";
    }
    else if(x == 0 and y<0){
        cout<<"23 line";
    }
    else if(x<0 and y == 0){
        cout<<"34 line";
    }
    else if(x == 0 and y >0){
        cout<<"41 line";
    }
    else{
        cout<<"middle";
    }
    
} 
