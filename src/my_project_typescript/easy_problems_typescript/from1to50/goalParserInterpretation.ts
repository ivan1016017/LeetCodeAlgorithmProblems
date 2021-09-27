function interpret(command: string): string {
    var valueString1 = /\(al\)/g
    var valueString2 = /\(\)/g

    command = command.replace(valueString1, "al" )
    command = command.replace(valueString2, "o" )



    return command
};


console.log(interpret( "G()(al)(al)"))