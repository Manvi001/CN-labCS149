#include<bits/stdc++.h>
using namespace std;

string xorOp(string dividend , string divisor){
    string res = "";
    for(int i = 1; i < divisor.length(); i++){
        res += (dividend[i] == divisor[i] ? '0' : '1');
    }
    return res;
}

string divideData(string data , string divi){
    string temp = data.substr(0, divi.length());
    for(int i = divi.length(); i <= data.length(); i++){
        if(temp[0] == '1'){
            temp = xorOp(temp , divi);
        } else {
            temp = xorOp(temp , string(divi.length(), '0'));
        }
        if(i < data.length()){
            temp += data[i];
        }
    }
    return temp.substr(1);
}

string sender(string dataword , string divisor){
    string padData = dataword + string(divisor.length() - 1, '0');
    string rem = divideData(padData, divisor);
    return dataword + rem;
}

bool receiver(string recData , string divisor){
    string rem = divideData(recData, divisor);
    return rem.find('1') == string::npos;
}

int main(){
    string dataword, divi;
    cout << "Enter dataword: ";
    cin >> dataword;
    cout << "Enter divisor: ";
    cin >> divi;
    
    string TD = sender(dataword, divi);
    cout << "Transmitted Data (TD): " << TD << endl;

    cout << "Enter received data: ";
    string RD;
    cin >> RD;
    
    if(receiver(RD, divi)){
        cout << "Valid data received." << endl;
    } else {
        cout << "Error in received data." << endl;
    }
    return 0;
}




****************output*********************
  //valid case

enter dataword , divi : 1101 1011
TD: 110101
enter recieved data: 110101
valid
  
  //error case
enter dataword , divi : 1101 1011
TD: 110101
enter recieved data: 110100 
error
