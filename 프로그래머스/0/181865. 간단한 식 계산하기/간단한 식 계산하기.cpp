#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string binomial) {
    int a, b;
    char op;

    stringstream ss(binomial);
    ss >> a >> op >> b;
    
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    return a * b;
}