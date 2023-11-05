

function removeDuplicates(nums:Array<number>): number {

    if (nums.length == 0){
        return 0
    }
    let i: number = 0
    let count: number = 1
    let flag: boolean = false 
    let tempI: number 
    let tempJ: number 
    for (let j = 1; j < nums.length; j++){
        if (nums[j] === nums[i]){
            if (!flag){
                flag = true
                i += 1
                tempI = nums[i]
                tempJ = nums[j]
                nums[i] = tempJ
                nums[j] = tempI 
                count += 1
            }
        }
        else{ 
            flag = false 
            i += 1
            tempI = nums[i]
            tempJ = nums[j]
            nums[i] = tempJ
            nums[j] = tempI
            count += 1
        }
    }

    return count 
}