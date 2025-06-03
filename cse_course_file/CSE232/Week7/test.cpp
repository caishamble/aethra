#include <iostream>
#include <string>

using namespace std;

// Function to provide feedback for the guessed word
string feedback(string ans_str, string guess_str) {
    string feedback = "";
    
    for (int i = 0; i < 5; ++i) {
        if (guess_str[i] == ans_str[i]) {
            feedback += guess_str[i];  // Correct letter in the right position
        } else if (guess_str[i] == ans_str[0] || guess_str[i] == ans_str[1] ||
                   guess_str[i] == ans_str[2] || guess_str[i] == ans_str[3] ||
                   guess_str[i] == ans_str[4]) {
            feedback += "?";  // Letter exists in the word but in the wrong position
        } else {
            feedback += ".";  // Letter doesn't exist in the word
        }
    }

    return feedback;
}

int main() {
    string ans_str;
    string guess_str;
    int attempt_cnt = 0;
    const int max_attempts = 6;

    cout << "Give me a secret word: " << endl;
    cin >> ans_str;

    while (attempt_cnt < max_attempts) {
        cout << "Give me a guess: " << endl;
        cin >> guess_str;

        if (guess_str == ans_str) {
            cout << feedback(ans_str, guess_str) << endl;
            cout << "You Win!" << endl;
            break;
        } else {
            cout << feedback(ans_str, guess_str) << endl;
            attempt_cnt++;
        }

        if (attempt_cnt >= max_attempts) {
            cout << "You Lose." << endl;
        }
    }

    return 0;
}
