// WRITE YOUR CODE HERE
#include <iostream>
#include <string>

using namespace std;

string SharedLetters(const string & s1,const string s2,const string * s3){
  int len_s1 = s1.size();
  int len_s2 = s2.size();
  int len_s3 = (*s3).size();
  int max = 0;
  if(len_s1 > len_s2 && len_s1 > len_s3){
    max = len_s1;
  }
  else if(len_s2 > len_s1 && len_s2 > len_s3){
    max = len_s2;
  }else{
    max = len_s3;
  }
  string str = "";
  for(int i = 0; i <= max - 1; ++i){
    int cnt = 0;
    if(i< len_s1 && i < len_s2 && s1.at(i) == s2.at(i)){
      cnt += 1;
    }
    if(i< len_s2 && i < len_s3 && s2.at(i) == (*s3).at(i)){
      cnt += 1;
    }
    if(i < len_s1 && i < len_s3 && s1.at(i) == (*s3).at(i)){
      cnt += 1;
    }
  }
  return str;
}

int main(){
  string s1;
  string s2;
  string s3;
  cin >> s1 >> s2 >> s3;
  string result = SharedLetters(s1,s2, &s3);
  cout << result << endl;
  return 0;
}


