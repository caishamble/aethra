// WRITE YOUR CODE HERE
#include <iostream>
#include <iomanip>

int main(){

  // input the day
  int day;
  std::cin >> day;

  // convert initial_distance into km & mi
  const double initial_distance_au = 37.33;
  double initial_distance_km = initial_distance_au * 149598000;
  double initial_distance_mi = initial_distance_au * 92955800;

  // calculate the travel distance into km & mi
  int sec = day * 24 * 3600;
  double travel_distance_km = 14.33 * sec;
  double travel_distance_mi = 8.90 * sec;

  // get the total distance in km & mi
  double total_distance_km = initial_distance_km + travel_distance_km;
  double total_distance_mi = initial_distance_mi + travel_distance_mi;

  // find the time wave travel, for round trip, we have to times two
  double times_hour = total_distance_km * 1000 * 2 / 299792458 / 3600;

  // output the value
  std::cout << std::fixed << std::setprecision(2) 
            << total_distance_km << std::endl
            << total_distance_mi << std::endl
            << times_hour << std::endl;

  return 0;
}