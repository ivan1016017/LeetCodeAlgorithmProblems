class TwoSum {
	private storage = new Map<number, number>();

	constructor() {}

	add(number: number): void {
		const amount: number = this.storage.get(number) || 0;

		this.storage.set(number, amount + 1);
	}

	find(value: number): boolean {
		for (let [numberValue] of this.storage.entries()) {
			const diffValue = value - numberValue;
			const diffAmount = this.storage.get(diffValue);

			if (typeof diffAmount !== "undefined") {
				if (diffValue !== numberValue) {
					return true;
				} else if (diffAmount >= 2) {
					return true;
				}
			}
		}

		return false;
	}
}



class TwoSumTwo {
    private dictNums: {[key:number]:number}
    constructor() {
        this.dictNums = {}

    }

    add(number: number): void {
        if (number in this.dictNums){
            this.dictNums[number]+=1
        }
        else{
            this.dictNums[number]=1
        }

    }

    find(value: number): boolean {

        for (let i in this.dictNums){
            if (value-parseInt(i) in this.dictNums){
                if (value-parseInt(i) !== parseInt(i)){
                    return true  
                }
                else {
                    if (this.dictNums[i] >= 2){
                        return true 
                    }
                }
            }
        }
        return false
    }
}