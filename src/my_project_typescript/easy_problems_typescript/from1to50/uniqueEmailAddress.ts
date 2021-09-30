function numUniqueEmails(emails: string[]): number {

    function splitConcatString(email: string) : string{

        let tempList: Array<string> = []
        tempList = email.split("@")
        let strLeft = tempList[0]
        let strRight = tempList[tempList.length-1]
        let tempListLocalName: Array<string> = strLeft.split("+")
        strLeft = tempListLocalName[0]
        tempListLocalName = strLeft.split(".")
        strLeft = tempListLocalName.join("")
        
        return strLeft + "@" + strRight
    }

    let answerList: Array<string> = []

    for (let email of emails){
        answerList.push(splitConcatString(email))
    }

    let answerSet: any = new Set()
    for (let email of answerList){
        answerSet.add(email)
    }


    return answerSet.size

};

console.log(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


console.log(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))





