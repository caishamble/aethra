#include <bits/stdc++.h>

using namespace std;

int main(){
    // copy operation
    // copy constructor
    // copy assignment operator

    // copy constructor
    class_name(const class_name &obj){
        // copy all the data members
    }

    // copy assignment operator
    class_name& operator=(const class_name &obj){
        // copy all the data members
        return *this;
    }


    // move operation
    // move constructor
    // move assignment operator

    // move constructor
    class_name(class_name &&obj){
        // move all the data members
    }

    // move assignment operator
    class_name& operator=(class_name &&obj){
        // move all the data members
        return *this;
    }



    // rule of 3
    // destructor
    // copy constructor
    // copy assignment operator

    // rule of 5
    // destructor
    // copy constructor
    // copy assignment operator
    // move constructor
    // move assignment operator



    // operator overloading

    // equality operator
    // relational operator
    // I/O operator



    // stream


    // stream operator

    // input stream operator
    // output stream operator

    // input stream operator
    istream & operator>>(istream & is, T & );

    // output stream operator
    ostream & operator<<(ostream & os, const T & );


    // fstream

    // ofstream
    ofstream ofs("file.txt");
    ofs << setw(4); // set width of the output
    ofs << setprecision(2); // set precision of the output
    ofs << "Age: " << 30 << endl;

    // ifstream
    ifstream ifs("file.txt");
    int x;
    ifs >> x;
    ifs >> noskipws; // do not skip white space
    ifs >> x;
    while(ifs >> x){
        cout << x << endl;
    }


    // stringstream

    // ostringstream
    ostringstream oss;
    oss << "Age: " << 30 << endl;
    string str = oss.str();

    // istringstream
    string word;
    char ch;
    istringstream iss{"Hello World"};
    iss >> word;
    iss.get(ch);
    iss.get(ch);


    // git 

    // terminology

    // repository
    // a repo is a directory that is managed by git

    // commit
    // the contents of a repo at a specific moment

    // commit message
    // a message that describes the changes made in a commit

    // local repo   
    // this is the repo on your computer that you can change direclty

    // remote repo
    // this is a repo hosted elsewhere that you can send commits to often hosted on sites GitHub

    // branch
    // a named sequence of commits


    // commands

    // git init
    // initialize a new git repo

    // git clone
    // clone a repo into a new directory


    // git add
    // add file contents to the index

    // git log
    // print the list of commits

    // git commit -m "Commit message"
    // insert a commit into the repo

    // git config --global user.name "Your Name"
    // set the name of the user

    // git config --global user.email "Your Email"
    // set the email of the user

    // git branch -l
    // list all the branches

    // git branch branch_name
    // create a new branch

    // git checkout branch_name
    // check out a branch, commits will be made to this branch

    // git merge branch_name
    // merge the branch into the current branch

    // git branch -d branch_name
    // delete the branch


    // git push
    // push the changes to the remote repo

    // git pull
    // pull the changes from the remote repo

    // git clone
    // clone a repo into a new directory    


    return 0;
}