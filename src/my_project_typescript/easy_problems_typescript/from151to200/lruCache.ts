class LRUCache {
    /*
    Map in typescript is ordered
    Whenever you `get`, delete the key-val and add it back to ensure that it is the latest
    When `put` the value, if it exist, delete. Add it back(Same reason as second point). 
	If size is more than capacity, delete the k-v pair at first index.
    */
    
    capacity: number
    cache: Map<number, any>
    
    constructor(capacity: number) {
        this.cache = new Map()
        this.capacity = capacity
    }

    get(key: number): any {
        if (!this.cache.has(key)) {
            return -1
        }
        
        const val = this.cache.get(key)
        this.cache.delete(key)
        this.cache.set(key, val)
        return this.cache.get(key)
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            this.cache.delete(key)
        }
        
        this.cache.set(key,value)
        if (this.cache.size > this.capacity) {
            this.cache.delete(this.cache.keys().next().value)   
        }
    }
}