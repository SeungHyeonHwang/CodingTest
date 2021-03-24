# In[] : https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록 level 2 


def solution(phone_book):
    answer=''
    sort_book = sorted(phone_book, key=lambda x : len(x))
    for i in range(len(sort_book)):
        phone = sort_book[i]
        for j in range(i+1, len(sort_book)) :
            if phone in sort_book[j][:len(phone)] : 
                return False
        

    return True


	
phone_book = [['119', '97674223', '1195524421'],['123','456','789'],['12','123','1235','567','88'],['12','153','1835','567','15678']]
for i in range(len(phone_book)):
    print(solution(phone_book[i]))