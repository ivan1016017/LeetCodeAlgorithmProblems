function sortSentence(s: string): string {

    let string_list = s.split(" ")

    

    function index_number(stringValue: string): number{
        return parseInt(stringValue[stringValue.length -1])
    }

    string_list = string_list.sort((a,b) => index_number(a) <= index_number(b)?-1:1)



    string_list = string_list.map(x => x.slice(0,x.length-1))

    let answer: string = string_list.join(" ")


    return answer

};

console.log(sortSentence( "is2 sentence4 This1 a3"))


