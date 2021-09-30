from typing import List 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def split_concat_string(email: str) -> str:
            temp_list: List[str]= list()
            temp_list = email.split("@")
            str_left = temp_list[0]
            str_right = temp_list[-1]
            temp_list_local_name: List[str] = list()
            temp_list_local_name = str_left.split("+")
            str_left = temp_list_local_name[0]
            temp_list_local_name = str_left.split(".")
            str_left = "".join(temp_list_local_name)

            return str_left +"@"+ str_right

        answer_list: List[str] = list()

        for email in emails: 
            answer_list.append(split_concat_string(email))

        
        return len(set(answer_list))

solution = Solution()

print(solution.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

print(solution.numUniqueEmails(emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))





