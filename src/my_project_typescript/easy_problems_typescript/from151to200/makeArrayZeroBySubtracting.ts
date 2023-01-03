function minimumOperations(nums: number[]): number {

        let objectSolution: {[key:number]:number} = {}

        let answer: number = 0

        for (let num of nums){
            objectSolution[num] = 1
        }

        for (let num in objectSolution){
            if (Number(num) > 0){
                answer += objectSolution[num]
            }
            
        }

        return answer


};