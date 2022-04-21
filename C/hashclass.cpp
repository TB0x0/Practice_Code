#include <iostream>
#include <vector>

using namespace std;

class MyHashSet {
public:
    vector<int> keys;

    MyHashSet() {
      cout << "hashSet constructor\n";
      keys.push_back(0);
    }

    void add(int key) {
        bool inSet = false;
          for(int i = 0; i < keys.size(); i++){
              if (keys[i] == key){
                  inSet = true;
              }
              else {
                  inSet = false;
              }
          }
          if (!inSet){
              keys.push_back(key);
              cout << "key added: "<< key << "\n";
          }
    }

    void remove(int key) {
        bool inSet = false;
        for(int i = 0; i < keys.size(); i++){
            if (keys[i] == key){
                keys.erase(keys.begin()+i);
            }
        }
    }

    bool contains(int key) {
         bool inSet = true;
        for(int i = 0; i < keys.size(); i++){
            if (keys[i] == key){
                inSet = true;
            }
            else {
                inSet = false;
            }
        }
        cout << "Contains: " << key << "\n";
       return inSet;
    }
};

int main() {
  cout << "Started HashSet\n";
  MyHashSet myHashSet;
  myHashSet.add(1);      // set = [1]
  myHashSet.add(2);      // set = [1, 2]
  myHashSet.contains(1); // return True
  myHashSet.contains(3); // return False, (not found)
  myHashSet.add(2);      // set = [1, 2]
  myHashSet.contains(2); // return True
  myHashSet.remove(2);   // set = [1]
  myHashSet.contains(2); // return False, (already removed)

}
