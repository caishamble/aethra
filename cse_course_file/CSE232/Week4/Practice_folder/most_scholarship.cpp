#include <bits/stdc++.h>

using namespace std;

class score {
    int chinese;
    int math;
    int english;
    int index;

public:

    // Constructor
    // in consturctor, create new variable c , m, e, i, and in the following, you can reuse the private variable
    score(int c, int m, int e, int i) : chinese{c}, math{m}, english{e}, index{i} {}

    int get_total(){
        return chinese + math + english;
    }

    int get_index(){
        return index;
    }
    int get_chinese(){
        return chinese;
    }
};

bool cmp(score a, score b) {
    if (a.get_total() == b.get_total()) {
        if (a.get_chinese() == b.get_chinese()) {
            return a.get_index() < b.get_index();
        } else {
            return a.get_chinese() > b.get_chinese();
        }
    } else {
        return a.get_total() > b.get_total();
    }
}


int main() {
    int n;
    vector<score> all_score;

    // Input the number of students
    cin >> n;
    
    // Input the scores for each student
    for (int i = 0; i < n; i++) {
        int c, m, e;
        cin >> c >> m >> e;
        all_score.push_back(score(c, m, e, i + 1)); // Store score and index
    }

    // Sort the scores based on the comparator
    sort(all_score.begin(), all_score.end(), cmp);

    // Output the sorted result
    for (int i = 0; i < 5; i++) {
        cout << all_score[i].get_index() << " " << all_score[i].get_total() << endl;
    }

    return 0;
}
