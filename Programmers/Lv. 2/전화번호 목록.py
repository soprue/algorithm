def solution(phone_book):
    phone_set = set(phone_book)
    
    for phone in phone_book:
        temp = ""
        
        for number in phone[:-1]:
            temp += number
            if temp in phone_set:
                return False
    
    return True
