function racecar(target: number): number {
    let q: number[][] = [[0,1,0]]

    while (q.length>0){
        let temp:any = q.shift()
        let pos:  number = temp[0]
        let speed: number = temp[1]
        let n: number = temp[2]
        if (pos===target){
            return n
        }
        q.push([pos+speed,speed*2,n+1])
        if (speed>0){
            if (pos+speed > target){
                q.push([pos,-1,n+1])
            }
        }
        else{
            if (pos+speed<target){
                q.push([pos,1,n+1])
            }
        }
    }
    return 0
};