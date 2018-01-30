#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int number_needed(string a, string b) {
    int freq[26];
    
    for(int i = 0; i < 26; i ++)
        freq[i] = 0;
    for (auto c : a)
        freq[c-'a'] +=1;
    for (auto c : b)
        freq[c-'a'] -=1;
    
    int result = 0;
    for(int i = 0; i < 26; i ++)
        result += abs(freq[i]) ;
   
    return result;
   
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed(a, b) << endl;
    return 0;
}
