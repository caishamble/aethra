/**
 * Question 2 - SeatRanking
 * 
 * Modify the Taylor Swift problem solution from the previous homework:
 * - instead of penalizing seats in every direction, we only want to penalize seats *between* the super fan and the stage
 * 
 * Reminder of the real code instructions from original problem (which they don't give you on exam):
 * THEY ARE NOT THE INSTRUCTIONS FOR THIS PROBLEM, JUST A REMINDER OF THE ORIGINAL PROBLEM
 */
/**
 * Taylor Swift is currently conducting a record breaking world tour, and seats are extremely expensive, especially near the stage. Being closer to the stage is always better than not, but unfortunately some of her more enthusiastic fans scream or cry her lyrics, despite not having nearly the same level of talent as "Mother". Being close to such fans unfortunately makes the experience less pleasant.
Lets imagine that the location of such fans could be known before you needed to purchase tickets (perhaps the super fans were able to buy tickets in a pre-sale event). I want you to write a program that can output the relative value of a grid of seats, which takes into account the distance from the stage and the distance from the loud super fans.
Lets envision a grid of 20 by 10 seats, where the origin (0,0) is on the bottom left. Position (5, 7) would be 5 seats from the left edge, and 7 seats up from the bottom. The stage is located along the bottom edge. Seats adjacent to the stage (x, 0) have a value of 100, those one seat further have a value of 95, those one seat further have a value of 90 and so forth. Seats adjacent to a super fan (in the N, S, E, and W directions) have their value reduced by 40, those one seat further away (and along the diagonals) have their value reduced by 20.
The location of seats purchased by super fans will be provided to standard input in this form:
(5,7)
(13,3)
(14,3)
(14,2)
(13,1)
(8,9)
(0,7)
Your program should output the value of each seat in the grid. Please put asterisks (‘*’) in the seats purchased by super fans.
For the position of the super fans in the input above, the correct output should look like this:
  35,  55,  55,  55,  55,  35,  35,  15,   *,  15,  35,  55,  55,  55,  55,  55,  55,  55,  55,  55,
  20,  40,  60,  60,  40,  20,  40,  40,  20,  40,  60,  60,  60,  60,  60,  60,  60,  60,  60,  60,
   *,  25,  45,  45,  25,   *,  25,  45,  45,  65,  65,  65,  65,  65,  65,  65,  65,  65,  65,  65,
  30,  50,  70,  70,  50,  30,  50,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,
  55,  75,  75,  75,  75,  55,  75,  75,  75,  75,  75,  75,  75,  55,  55,  75,  75,  75,  75,  75,
  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  60,  20,   0,  60,  80,  80,  80,  80,
  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  65,  25,   *,   *,   5,  65,  85,  85,  85,
  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  30, -50,   *,  30,  70,  90,  90,  90,
  95,  95,  95,  95,  95,  95,  95,  95,  95,  95,  95,  75,  55,   *,  -5,  55,  95,  95,  95,  95,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,  80,  60,  60, 100, 100, 100, 100, 100,
 */
/**
 * Example input for this problem:
 * (5,7)
 * (13,3)
 * (14,3)
 * (14,2)
 * (13,1)
 * (8,9)
 * (0,7)
 * 
 * Example output for this problem:
  55,  55,  55,  55,  55,  55,  55,  55,   *,  55,  55,  55,  55,  55,  55,  55,  55,  55,  55,  55,
  60,  60,  60,  60,  60,  60,  60,  40,  20,  40,  60,  60,  60,  60,  60,  60,  60,  60,  60,  60,
   *,  65,  65,  65,  65,   *,  65,  65,  45,  65,  65,  65,  65,  65,  65,  65,  65,  65,  65,  65,
  30,  50,  70,  70,  50,  30,  50,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,  70,
  55,  75,  75,  75,  75,  55,  75,  75,  75,  75,  75,  75,  75,  75,  75,  75,  75,  75,  75,  75,
  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,  80,
  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,  85,   *,   *,  85,  85,  85,  85,  85,
  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  90,  70,  30,   *,  70,  90,  90,  90,  90,
  95,  95,  95,  95,  95,  95,  95,  95,  95,  95,  95,  95,  95,   *,  35,  75,  95,  95,  95,  95,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,  80,  60,  60, 100, 100, 100, 100, 100,
 
 */

// main.cpp
// given to you to modify from previous homework, Nahum version will be different but solution is the same mind
#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cmath>
using namespace std;

void print2DVec(vector<vector<string>> & seats){
    for(size_t i = 0; i < seats.size(); ++i){
        for(size_t j = 0; j < seats.at(i).size(); ++j){
            if(seats.at(i).at(j).size() == 3)
                cout << " " << seats.at(i).at(j) << ",";
            else if(seats.at(i).at(j).size() == 1)
                cout << "   " << seats.at(i).at(j) << ",";
            else
                cout << "  " << seats.at(i).at(j) << ",";
        }
        cout << '\n';
    }
}

void fillSeatValues(vector<vector<string>> & seats){//fill the seat values without superfan locations
    int farthestVal = 55;   //value of the farthest seats from the stage
    for(size_t j = 0; j < 10; ++j){
        vector<string> row;
        string toAdd;
        for(size_t i = 0; i < 20; ++i){
            toAdd = to_string(farthestVal);
            row.push_back(toAdd);
        }
        farthestVal += 5;
        seats.push_back(row);
    }
}

size_t getSuperFanCol(string & str){//from 0 to 19
    int numAsInt;
    numAsInt = str.at(1) - '0';
    if(str.at(2) != ','){
        numAsInt*=10;
        numAsInt += str.at(2) - '0';
    }
    size_t ST = numAsInt;
    return ST;
}

size_t getSuperFanRow(string & str){//from 0 to 9
    int numAsInt;
    numAsInt = str.at(str.size() - 2) - '0';
    size_t ST = numAsInt;
    return ST;
}

void seatSFs(vector<vector<string>> & seats, size_t col, size_t row){//In all honesty I dont understand how I made this work. But I did.
    seats.at(9-row).at(col) = " *";
}

//E W N S reduces by 40, diagonals by 20, next to E W N S by 20

//CHECK IF THE COORDINATE HAS BEEN TURNED INTO A *; IF IT HAS, DONT DO ANYTHING WITH IT

// void adjustOneRight(vector<vector<string>> & seats, size_t col, size_t row){
//     string atPos;
//     atPos = seats.at(9 - row).at(col + 1);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 40;
//         atPos = to_string(num);
//         seats.at(9 - row).at(col + 1) = atPos;
//     }
// }

// void adjustOneUp(vector<vector<string>> & seats, size_t col, size_t row){
//     string atPos;
//     atPos = seats.at(9 - (row + 1)).at(col);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 40;
//         atPos = to_string(num);
//         seats.at(9 - (row + 1)).at(col) = atPos;
//     }
// }

void adjustOneDown(vector<vector<string>> & seats, size_t col, size_t row){
    string atPos;
    atPos = seats.at(9 - (row - 1)).at(col);
    if(atPos != " *"){
        int num = stoi(atPos);
        num -= 40;
        atPos = to_string(num);
        seats.at(9 - (row - 1)).at(col) = atPos;
    }
}

// void adjustOneLeft(vector<vector<string>> & seats, size_t col, size_t row){
//     string atPos;
//     atPos = seats.at(9 - row).at(col - 1);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 40;
//         atPos = to_string(num);
//         seats.at(9 - row).at(col - 1) = atPos;
//     }
// }

// void adjustTwoRight(vector<vector<string>> & seats, size_t col, size_t row){
//     adjustOneRight(seats, col, row);
//     string atPos;
//     atPos = seats.at(9 - row).at(col + 2);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 20;
//         atPos = to_string(num);
//         seats.at(9 - row).at(col + 2) = atPos;
//     }
// }

// void adjustTwoUp(vector<vector<string>> & seats, size_t col, size_t row){
//     adjustOneUp(seats, col, row);
//     string atPos;
//     atPos = seats.at(9 - (row + 2)).at(col);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 20;
//         atPos = to_string(num);
//         seats.at(9 - (row + 2)).at(col) = atPos;
//     }
// }

void adjustTwoDown(vector<vector<string>> & seats, size_t col, size_t row){
    adjustOneDown(seats, col, row);
    string atPos;
    atPos = seats.at(9 - (row - 2)).at(col);
    if(atPos != " *"){
        int num = stoi(atPos);
        num -= 20;
        atPos = to_string(num);
        seats.at(9 - (row - 2)).at(col) = atPos;
    }
}

// void adjustTwoLeft(vector<vector<string>> & seats, size_t col, size_t row){
//     adjustOneLeft(seats, col, row);
//     string atPos;
//     atPos = seats.at(9 - row).at(col - 2);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 20;
//         atPos = to_string(num);
//         seats.at(9 - row).at(col - 2) = atPos;
//     }
// }

// void adjustUpRight(vector<vector<string>> & seats, size_t col, size_t row){
//     ++col;
//     string atPos;
//     atPos = seats.at(9 - (row + 1)).at(col);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 20;
//         atPos = to_string(num);
//         seats.at(9 - (row + 1)).at(col) = atPos;
//     }
// }

// void adjustUpLeft(vector<vector<string>> & seats, size_t col, size_t row){
//     --col;
//     string atPos;
//     atPos = seats.at(9 - (row + 1)).at(col);
//     if(atPos != " *"){
//         int num = stoi(atPos);
//         num -= 20;
//         atPos = to_string(num);
//         seats.at(9 - (row + 1)).at(col) = atPos;
//     }
// }

void adjustDownRight(vector<vector<string>> & seats, size_t col, size_t row){
    ++col;
    string atPos;
    atPos = seats.at(9 - (row - 1)).at(col);
    if(atPos != " *"){
        int num = stoi(atPos);
        num -= 20;
        atPos = to_string(num);
        seats.at(9 - (row - 1)).at(col) = atPos;
    }    
}

void adjustDownLeft(vector<vector<string>> & seats, size_t col, size_t row){
    --col;
    string atPos;
    atPos = seats.at(9 - (row - 1)).at(col);
    if(atPos != " *"){
        int num = stoi(atPos);
        num -= 20;
        atPos = to_string(num);
        seats.at(9 - (row - 1)).at(col) = atPos;
    }
}

void adjustValues(vector<vector<string>> & seats, size_t col, size_t row){
    //side adjustments

    if(row > 1){
        adjustTwoDown(seats, col, row);
    }
    else if(row == 1){
        adjustOneDown(seats, col, row);
    }

    if(col <= 18 && row >= 1)
        adjustDownRight(seats, col, row);
    if(col >= 1 && row >= 1)
        adjustDownLeft(seats, col, row);
}

int main(){
    vector<vector<string>> seats;

    fillSeatValues(seats);

    string input;

    while(cin >> input && input != "q"){   
        size_t row = getSuperFanRow(input); //pass col first row second; rows start counting from below
        size_t col = getSuperFanCol(input);
        seatSFs(seats, col, row);
        adjustValues(seats, col, row);
        input.clear();
    }

    print2DVec(seats);
}
