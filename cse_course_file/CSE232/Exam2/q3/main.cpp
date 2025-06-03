#include "header.h" 
#include <iostream> 
#include <string>

using namespace std;

int main(){

    VoteSystem vs;
    vs.System({"Alice", "Bob", "Charlie"});
    cout << vs.to_string() << endl;
    vs.add_candidate("David");
    cout << vs.to_string() << endl;
    return 0;
}