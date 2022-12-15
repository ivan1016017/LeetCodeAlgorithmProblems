function numberToWords(num: number): string {

    function helper(num:number):string{
        if (num < 10){
            return dic1[num]
        }
        else if(10<=num && num <20){
            return dic3[num]
        }
        else if (num<100){
            let res:string[] = []
            let q = Math.floor(num/10)
            num = num%10
            res.push(dic2[q*10])
            if (num > 0){
                res.push(" "+dic1[num])
            }
            return res.join("")
        }
        else if(num <1000){
            let q = Math.floor(num/100)
            num = num%100
            if (num == 0){
                return dic1[q]+" "+"Hundred"
            }
            else{
                return dic1[q]+" "+"Hundred"+" "+helper(num)
            }    
        }
        else if(num < 1000000){
            let q = Math.floor(num/1000)
            num = num%1000
            if (num == 0){
                return helper(q)+" "+"Thousand"
            }
            else{
                return helper(q)+" "+"Thousand"+" "+helper(num)
            }               
        }
        else if (num < 1000000000){
            let q = Math.floor(num/1000000)
            num = num%1000000
            if (num == 0){
                return helper(q)+" "+"Million"
            }
            else{
                return helper(q)+" "+"Million"+" "+helper(num)

            }
        }
        else{
            let q = Math.floor(num/1000000000)
            num = num%1000000000
            if (num == 0){
                return helper(q)+" "+"Billion"
            }
            else{
                return helper(q)+" "+"Billion"+" "+helper(num)  
            }           
        }
    }

    if (num ==0){
        return 'Zero'
    }


    let dic1:{[key:number]:any} = {9:"Nine", 8:"Eight", 7:"Seven", 6:"Six", 
            5:"Five", 4:"Four", 3:"Three", 2:"Two", 1:"One"}
    let dic2:{[key:number]:any} = {90:"Ninety", 80:"Eighty", 70:"Seventy", 60:"Sixty", 
            50:"Fifty", 40:"Forty", 30:"Thirty", 20:"Twenty"} 
    let dic3:{[key:number]:any} = {19:"Nineteen", 18:"Eighteen", 17:"Seventeen", 
            16:"Sixteen", 15:"Fifteen", 14:"Fourteen", 13:"Thirteen", 
            12:"Twelve", 11:"Eleven", 10:"Ten"}


    return helper(num)

};