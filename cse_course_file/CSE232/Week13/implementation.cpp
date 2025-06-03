#include "header.hpp"

Time::Time(int hour, int minute) : hour(hour), minute(minute) {}

void Time::minuteincrement() {
    minute += 1;
    if (minute == 60) {
        minute = minute % 60;
        hour += 1;
        if (hour == 12) {
            hour = hour % 12;
        }
    }
}

void Time::hourincrement() {
    hour += 1;
    if (hour == 12) {
        hour = hour % 12;
    }
}

std::ostream& operator<<(std::ostream &out, const Time &t) {
    if (t.hour < 10) {
        out << "0";
    }
    out << t.hour << ":";
    if (t.minute < 10) {
        out << "0";
    }
    out << t.minute;
    return out;
}

std::istream& operator>>(std::istream &in, Time &t) {
    char colon;
    in >> t.hour >> colon >> t.minute;
    return in;
}