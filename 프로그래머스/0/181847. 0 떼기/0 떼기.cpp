#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string n_str) {
    int i = 0;
    while(true){
        if(n_str[i] == '0') {
            n_str.erase(i, 1);
        } else {
            break;
        }
    }
    return n_str;
}