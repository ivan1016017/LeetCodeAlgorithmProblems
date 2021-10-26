class MyHashSet {
    hashSet: Array<number> = []
    constructor() {
        
    }
    add(key: number): void {
        if (!this.hashSet.includes(key)){
            this.hashSet.push(key)
        }

    }

    remove(key: number): void {
        for (let i = 0; i< this.hashSet.length; i++){
            if (this.hashSet[i] == key){
                this.hashSet = this.hashSet.slice(0,i).concat(this.hashSet.slice(i+1))
                break
            }
        }

    }

    contains(key: number): boolean {
        let tempBoolean: boolean = false
        if (this.hashSet.includes(key)){
            tempBoolean = true 
            return tempBoolean
        }
        return tempBoolean

    }
}