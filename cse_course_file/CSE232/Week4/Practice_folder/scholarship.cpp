// 2024-10-06 practice luogo question P1051

#include <bits/stdc++.h>

using namespace std;

class Student{
    string name;
    int final_score;
    int judge_score;
    bool is_leader;
    bool is_west;
    int paper_num;
    int scholarship;

public:
    Student(string n, int f, int j, bool l, bool w, int p){
        name = n;
        final_score = f;
        judge_score = j;
        is_leader = l;
        is_west = w;
        paper_num = p;
        scholarship = 0;
    }

    void CalculateScholarship(){
        if(final_score > 80 && paper_num >= 1){
            scholarship += 8000;
        }
        if(final_score > 85 && judge_score > 80){
            scholarship += 4000;
        }
        if(final_score > 90){
            scholarship += 2000;
        }
        if(final_score > 85 && is_west){
            scholarship += 1000;
        }
        if(judge_score > 80 && is_leader){
            scholarship += 850;
        }
    }

    int GetScholarship(){
        return scholarship;
    }
    string GetName(){
        return name;
    }

};

int main(){

    int n;
    cin >> n;
    vector<Student> students;
    for(int i = 0; i < n; ++i){
        string name;
        int final_score, judge_score, paper_num;
        bool is_leader, is_west;
        cin >> name >> final_score >> judge_score;
        char l, w;
        cin >> l >> w;
        cin >> paper_num;
        students.push_back(Student(name, final_score, judge_score, l == 'Y', w == 'Y', paper_num));
    }

    int max_scholarship = 0;
    string max_name = "";

    for(int i = 0; i < n; ++i){
        students[i].CalculateScholarship();
        if(students[i].GetScholarship() > max_scholarship){
            max_scholarship = students[i].GetScholarship();
            max_name = students[i].GetName();
        }
    }

    int total_scholarship = 0;
    for(int i = 0; i < n; ++i){
        total_scholarship += students[i].GetScholarship();
    }

    cout << max_name << endl;
    cout << max_scholarship << endl;
    cout << total_scholarship << endl;

    return 0;
}