#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    // initialize map
    unordered_map<string, string> myMap;
    // add items
    myMap["name"] = "Jack";
    myMap["age"] = "26";
    myMap["address"] = "Downtown";
    // update value
    myMap["age"] = "27";

    // check if key is in map
    if ( myMap.find("age") != myMap.end() )
        cout << myMap["age"] << endl;

    // iterate over map
    for (auto const& pair: myMap) {
        std::cout << "{" << pair.first << ": " << pair.second << "}\n";
    }

}
