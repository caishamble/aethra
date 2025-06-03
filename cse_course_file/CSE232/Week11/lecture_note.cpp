#include <bits/stdc++.h>

using namespace std;

int main(){
    // iterator types
    
    // container iterators
    vector<int> v = {1, 2, 3, 4, 5};
    vector<int>::iterator it = v.begin();
    cout << *it << endl;

    // container const iterators
    vector<int>::const_iterator cit = v.cbegin();
    cout << *cit << endl;

    // Forward Iterator

    // deference and equalities    *it, it == it2, it != it2
    // forward iterator            ++it, --it
    
    // Bidirectional Iterator      ++it, --it

    // Random Access Iterator      it += 5, it -= 5, it + 5, it - 5, it[5]

    // pointers are iterators
    int array[3] = {2, 3, 2};
    int *ar_begin = array;
    int *ar_end = array + 3;
    ar_begin++;
    *ar_begin = 4;
    bool b = ar_begin != ar_end;


    // iterator invalidation    
    string const original = 
        "My dog is named Mal.";
    string copy{original};
    sort(copy.begin(), copy.end());
    cout << copy << endl;

    // prints: "    .MMaadddegilmnosy"
    

    // iterator invalidation
    copy = original;
    std::string::iterator start = 
        copy.begin() + 5;
    sort(start, copy.end());
    cout << copy << endl;

    // prints: "My do    .Maadegilmns"

    // function used in sort
    bool CaseInsensitiveLess(char left, char right) {
        return tolower(left) < tolower(right);
    }

    // ...
    copy = original;
    sort(copy.begin(), copy.end(),CaseInsensitiveLess);
    cout << copy << endl;
    // prints: ".aaddegilMmNnosy"


    // lambda function used in sort
    copy = original;
    sort(copy.begin(), copy.end(),
        [](char left, char right){
            return tolower(left) < tolower(right);
        });
    cout << copy << endl;
    // prints: ".aaddegilMmNnosy"

    // std::ranges::sort
    // sort is a function that sorts a range of elements


    // Important ALgorithms
    

    return 0;
}