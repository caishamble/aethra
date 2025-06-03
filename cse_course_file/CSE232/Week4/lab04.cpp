#include <bits/stdc++.h>

using namespace std;

int64_t LocToDec(string const & loc) {
  int cnt_a = 0, cnt_b = 0, cnt_c = 0, cnt_d = 0, cnt_e = 0;
  int cnt_f = 0, cnt_g = 0, cnt_h = 0, cnt_i = 0, cnt_j = 0;
  int cnt_k = 0, cnt_l = 0, cnt_m = 0, cnt_n = 0, cnt_o = 0;
  int cnt_p = 0, cnt_q = 0, cnt_r = 0, cnt_s = 0, cnt_t1 = 0;
  int cnt_u = 0, cnt_v = 0, cnt_w = 0, cnt_x = 0, cnt_y = 0, cnt_z = 0;

  // Count occurrences of each letter
  for (size_t i = 0; i < loc.size(); ++i) {
    switch (loc[i]) {
      case 'a': cnt_a += 1; break;
      case 'b': cnt_b += 1; break;
      case 'c': cnt_c += 1; break;
      case 'd': cnt_d += 1; break;
      case 'e': cnt_e += 1; break;
      case 'f': cnt_f += 1; break;
      case 'g': cnt_g += 1; break;
      case 'h': cnt_h += 1; break;
      case 'i': cnt_i += 1; break;
      case 'j': cnt_j += 1; break;
      case 'k': cnt_k += 1; break;
      case 'l': cnt_l += 1; break;
      case 'm': cnt_m += 1; break;
      case 'n': cnt_n += 1; break;
      case 'o': cnt_o += 1; break;
      case 'p': cnt_p += 1; break;
      case 'q': cnt_q += 1; break;
      case 'r': cnt_r += 1; break;
      case 's': cnt_s += 1; break;
      case 't': cnt_t1 += 1; break;
      case 'u': cnt_u += 1; break;
      case 'v': cnt_v += 1; break;
      case 'w': cnt_w += 1; break;
      case 'x': cnt_x += 1; break;
      case 'y': cnt_y += 1; break;
      case 'z': cnt_z += 1; break;
    }
  }

  // Calculate decimal equivalent
  int64_t ans = 0;
  ans = cnt_a * 1 + cnt_b * 2 + cnt_c * 4 + cnt_d * 8 + cnt_e * 16 +
        cnt_f * 32 + cnt_g * 64 + cnt_h * 128 + cnt_i * 256 + cnt_j * 512 +
        cnt_k * 1024 + cnt_l * 2048 + cnt_m * 4096 + cnt_n * 8192 +
        cnt_o * 16384 + cnt_p * 32768 + cnt_q * 65536 + cnt_r * 131072 +
        cnt_s * 262144 + cnt_t1 * 524288 + cnt_u * 1048576 + cnt_v * 2097152 +
        cnt_w * 4194304 + cnt_x * 8388608 + cnt_y * 16777216 + cnt_z * 33554432;

  return ans;
}


string Abbreviate(const string &loc){
    int ans = LocToDec(loc); // Convert loc to an integer
    string new_str = "";
    vector<char> arr = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                    'w', 'x', 'y', 'z'};


    int i = 0;
    while(true){
      if(pow(2, i) > ans){
        ans -= pow(2, i - 1);
        new_str += arr[i - 1];
        if(ans == 0){
          break;
        }
        i = 0;
        }else{
          i += 1;
        }
    }
    sort(new_str.begin(), new_str.end());
    if(loc == ""){
      return "";
    }else{
      return new_str; 
    }
}

string DecToLoc(int64_t dec){
    string new_str = "";
    vector<char> arr = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
                    'w', 'x', 'y', 'z'};
    if (dec == 0){
      return "";
    }
    else{
      int i = 0;
      while(true){
        if(pow(2, i) > dec){
          dec -= pow(2, i - 1);
          new_str += arr[i - 1];
          if(dec == 0){
            break;
          }
          i = 0;
          }else{
            i += 1;
          }
      }
      string rev_str = "";
      for(int i = new_str.size() - 1; i >=0; --i){
        rev_str += new_str[i];
      }
      return rev_str;
    }
}

int64_t AddLoc(string const & loc1, string const & loc2){
  int dec1 = LocToDec(loc1);
  int dec2 = LocToDec(loc2);
  return dec1 + dec2;
}

int main() {
  string s;
  string p, q;
  int a;
  cout << "Give me a location string:" << endl;
  cin >> s;
  cout << "Give me an integer:" << endl;
  cin >> a;
  cout << s << " to dec: " << LocToDec(s) << endl;
  cout << s << " abbreviated: " << Abbreviate(s) << endl;
  cout << a << " to loc: " << DecToLoc(a) << endl;
  cout << "Give me two more location strings: " << endl;
  cin >> p >> q;
  cout << "Sum of "<< p << " and " << q << " is: " << AddLoc(p, q) << endl;

}

