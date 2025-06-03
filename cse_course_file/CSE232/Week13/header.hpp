#pragma once

#include <iostream>

class Time {
    private:
        int minute;
        int hour;

    public:
        Time(int h, int m);
        void minuteincrement();
        void hourincrement();

        friend std::ostream& operator<<(std::ostream &out, const Time &t);
        friend std::istream& operator>>(std::istream &in, Time &t);
};
