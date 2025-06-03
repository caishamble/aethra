class Temperature {
    double tempValue;
    char tempUnit;

public:
    Temperature(double value, char unit) {
        tempValue = value;
        tempUnit = unit;
    }

    double AsCelsius(){
        if (tempUnit == 'C'){
            return tempValue;
        }else if (tempUnit == 'F'){
            return (tempValue - 32) * 5 / 9;
        }else if (tempUnit == 'K'){
            return tempValue - 273.15;
        }else if(tempUnit == 'R'){
            return (tempValue - 491.67) * 5 / 9;
        }else{
            return 0;
        }
    }
    double AsFahrenheit(){
        if (tempUnit == 'C'){
            return tempValue * 9 / 5 + 32;
        }else if (tempUnit == 'F'){
            return tempValue;
        }else if (tempUnit == 'K'){
            return tempValue * 9 / 5 - 459.67;
        }else if(tempUnit == 'R'){
            return tempValue - 459.67;
        }else{
            return 0;
        }
    }
    double AsKelvin(){
        if (tempUnit == 'C'){
            return tempValue + 273.15;
        }else if (tempUnit == 'F'){
            return (tempValue + 459.67) * 5 / 9;
        }else if (tempUnit == 'K'){
            return tempValue;
        }else if(tempUnit == 'R'){
            return tempValue * 5 / 9;
        }else{
            return 0;
        }
    }
    double AsRankine(){
        if (tempUnit == 'C'){
            return (tempValue + 273.15) * 9 / 5;
        }else if (tempUnit == 'F'){
            return tempValue + 459.67;
        }else if (tempUnit == 'K'){
            return tempValue * 9 / 5;
        }else if(tempUnit == 'R'){
            return tempValue;
        }else{
            return 0;
        }
    }

};