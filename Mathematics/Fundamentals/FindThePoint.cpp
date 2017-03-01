/*
Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.*/


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
   int n;
    cin >> n;
    vector<int> x(2), y(2);
    
    for(int arr_i = 0;arr_i < n;arr_i++){
        int xi = 0, yi = 0;
        for (int j = 0; j < 4; j++)
            
            if (j % 2 == 0)
                cin >> x[xi++];
            else cin >> y[yi++];
        cout << 2*x[1]-x[0] << " " << 2*y[1]-y[0] << "\n";
    }
    
    return 0;
}
