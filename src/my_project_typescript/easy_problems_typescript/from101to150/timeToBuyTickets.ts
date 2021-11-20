function timeRequiredToBuy(tickets: number[], k: number): number {

    let selected: number = tickets[k]
    let count: number = 0

    tickets.map((currentElement, index)=>{
        if (index < k){
            count += Math.min(currentElement,selected)
        }
        else if( index === k){
            count += selected
        }
        else {
            if (currentElement < selected){
                count += currentElement
            }
            else{
                count += selected - 1
            }
        }
        
    })

    return count 
};


console.log(timeRequiredToBuy([2,3,2],  2))

console.log(timeRequiredToBuy([5,1,1,1], 0))