function searchMatrix(matrix: number[][], target: number): boolean {
    
    if (matrix.length == 0 && matrix[0].length == 0){
        return false 
    }

    let h: number = matrix.length

    let w: number = matrix[0].length

    let left: number 
    let right: number 
    let mid: number
    let midValue: number

    for (let row of matrix){
        if (row[0] <= target && target <= row[row.length-1]){

            left = 0
            right = w-1

            while (left <= right){

                mid = Math.floor((left + right)/2)
                midValue = row[mid]

                if ( target > midValue){
                    left = mid + 1
                }
                else if (target < midValue){
                    right = mid -1
                }
                else { 
                    return true
                }
            }



        }
    }

    return false 
};