class MyHashMap {
    hashMap: Array<any> = []
    constructor() {

    }

    put(key: number, value: number): void {
        let flag: boolean = false 
        for (let i = 0; i < this.hashMap.length; i++){
            if (this.hashMap[i][0] == key){
                this.hashMap[i][1] = value 
                flag = true 
            }
        }
        if (flag == false){
            this.hashMap.push([key, value])

    }
}

    get(key: number): number {
        for (let i = 0; i < this.hashMap.length; i++){
            if (this.hashMap[i][0] == key){
                return this.hashMap[i][1]
            }
        }
        
        return -1
    }

    remove(key: number): void {
        for (let i = 0; i < this.hashMap.length; i++){
            if (this.hashMap[i][0] == key){
                this.hashMap = this.hashMap.slice(0,i).concat(this.hashMap.slice(i+1))
                break
            }

        }

    }
}
