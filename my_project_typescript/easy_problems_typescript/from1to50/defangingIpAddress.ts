function defangIPaddr(address: string): string {
    var valueString = /\./gi
    address = address.replace(valueString, "[.]" )


    return address
};


console.log(defangIPaddr("1.1.1.1"))