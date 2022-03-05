function deleteAndEarn(nums: number[]): number {
    let map: {[key: number]: number} = {};
    let distNums: number[] = [];
    for(let num of nums) {
        if(!map[num]) {
            distNums.push(num);
            map[num] = 0;
        }
        map[num]++;
    }
    if(distNums.length == 1) return map[distNums[0]]*distNums[0];
    distNums = distNums.sort((a,b) => a-b);
    let n1 = map[distNums[0]]*distNums[0];
    let n2 = distNums[1]-distNums[0] !== 1 ? n1 + map[distNums[1]]*distNums[1] : Math.max(n1,map[distNums[1]]*distNums[1]);
    for(let i = 2; i < distNums.length; i++) {
        let num = distNums[i];
        let temp = distNums[i]-distNums[i-1] !== 1 ? n2 + map[num]*num : Math.max(n2,n1 + map[num]*num);
        [n1,n2] = [n2,temp];
    }
    return n2;
};