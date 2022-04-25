# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from multiprocessing.connection import answer_challenge


S = 'cdeenetpi'
A = [5,2,0,1,6,4,8,3,7]
def solution(S, A):
    # write your code in Python 3.6
    answer = ''
    answer = answer + S[0]
    j = 0
    while A[j]!=0:
        answer = answer + S[A[j]]
        j = A[j]
    return answer

    
solution(S,A)

solution('bytdag',[4,3,0,1,2,5])
