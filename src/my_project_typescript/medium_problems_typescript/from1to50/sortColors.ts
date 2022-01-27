function sortColors(nums: number[]): void {

    let c0: number = 0
    let c1: number = 0
    let c2: number = 0
    

    for (let i = 0; i < nums.length; i++){
        if (nums[i] === 0){
            c0 += 1
        }
        else if (nums[i] === 1){
            c1 += 1
        }
        else {
            c2 += 1
        }
    }

    for (let i = 0; i < c0; i++ ){
        nums[i] = 0
    }
    for (let i = c0; i < c0+c1; i++ ){
        nums[i] = 1
    }
    for (let i = c0+c1; i < nums.length; i++ ){
        nums[i] = 2
    }




};