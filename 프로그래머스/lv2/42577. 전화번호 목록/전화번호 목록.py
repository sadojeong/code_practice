def solution(phone_book):
    answer = True
    phone_book_sorted = sorted(phone_book, key = lambda x: (x))

    for i in range(1, len(phone_book_sorted)):
        if phone_book_sorted[i-1] == phone_book_sorted[i][:len(phone_book_sorted[i-1])]:
            return False
        
    return answer