class RandomizedSet {
    private dataMap: Map<number, number>; // dictionary, aka map, aka hashtable, aka hashmap
    private data: number[]; // list aka array

    constructor() {
        this.dataMap = new Map();
        this.data = [];
    }

    insert(val: number): boolean {
        // the problem indicates we need to return False if the item 
        // is already in the RandomizedSet---checking if it's in the
        // dictionary is on average O(1) where as
        // checking the array is on average O(n)
        if (this.dataMap.has(val)) {
            return false;
        }

        // add the element to the dictionary. Setting the value as the 
        // length of the list will accurately point to the index of the 
        // new element. (len(some_list) is equal to the index of the last item +1)
        this.dataMap.set(val, this.data.length);

        // add to the list
        this.data.push(val);

        return true;
    }

    remove(val: number): boolean {
        // again, if the item is not in the dataMap, return false. 
        // we check the dictionary instead of the list due to lookup complexity
        if (!this.dataMap.has(val)) {
            return false;
        }

        // essentially, we're going to move the last element in the list 
        // into the location of the element we want to remove. 
        // this is a significantly more efficient operation than the obvious 
        // solution of removing the item and shifting the values of every item 
        // in the dictionary to match their new position in the list
        const lastElemInList = this.data[this.data.length - 1];
        const indexOfElemToRemove = this.dataMap.get(val)!;

        this.dataMap.set(lastElemInList, indexOfElemToRemove);
        this.data[indexOfElemToRemove] = lastElemInList;

        // change the last element in the list to now be the value of the element 
        // we want to remove
        this.data[this.data.length - 1] = val;

        // remove the last element in the list
        this.data.pop();

        // remove the element to be removed from the dictionary
        this.dataMap.delete(val);
        return true;
    }

    getRandom(): number {
        // random.choice will randomly select an element from the list of data.
        return this.data[Math.floor(Math.random() * this.data.length)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */