function wateringPlants(plants: number[], capacity: number): number {

    let returnCount: number = 0
    let tempCapacity: number = capacity

    let lenPlants: number = plants.length

    for (let i = 0; i < lenPlants; i++){
        if (tempCapacity < plants[i]){
            returnCount += i*2
            tempCapacity = capacity - plants[i]
        }
        else {
            tempCapacity -= plants[i]
        }
    }

    return lenPlants + returnCount

};


function wateringPlantsTwo(plants: number[], capacity: number): number {

    let returnCount: number = 0
    let tempCapacity: number = capacity

    let lenPlants: number = plants.length

    plants.forEach( (element, index) => {
        if (tempCapacity < element){
            returnCount += index*2
            tempCapacity = capacity - element
        }
        else {
            tempCapacity -= element
        }
    })

    return lenPlants + returnCount

};