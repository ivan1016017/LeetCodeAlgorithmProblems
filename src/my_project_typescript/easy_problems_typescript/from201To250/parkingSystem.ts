class ParkingSystem {
    private parkingSpace: number[]
    constructor(big: number, medium: number, small: number) {
        this.parkingSpace = [big,medium,small]
    }

    addCar(carType: number): boolean {

        if (this.parkingSpace[carType-1] !== 0){
            this.parkingSpace[carType-1]-=1
            return true 
        }
        return false 

    }
}