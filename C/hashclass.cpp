class MyHashSet {
public:
    vector<int> keys;

    MyHashSet() {

    }

    void add(int key) {
        bool inSet = false;
        if(keys.size() == 0){
            keys.push_back(key);
            cout << "Added " + key;
        }
        else {
            for(int i = 0; i < keys.size(); i++){
                if (keys[i] != key){
                    inSet = true;
                }
                else {
                    inSet = false;
                }
            }
            if (!inSet){
                keys.push_back(key);
                cout << "key added";
            }
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
       return inSet;
    }
};

MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
