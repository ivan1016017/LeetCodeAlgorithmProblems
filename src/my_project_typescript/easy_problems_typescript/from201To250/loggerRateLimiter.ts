class Logger {
    private dict_logger: any = {}
    constructor() {
        this.dict_logger = {}
    }

    shouldPrintMessage(timestamp: number, message: string): boolean {

        if (! (message in this.dict_logger)){
            this.dict_logger[message] = timestamp
            return true
        }
        else{
            if (timestamp - this.dict_logger[message] >= 10){
                this.dict_logger[message] = timestamp
                return true 
            }
            else{
                return false 
            }
        }
    }
}