# https://github.com/exercism/python/blob/main/exercises/practice/book-store/.docs/instructions.md

def biggest_discount(book_list):
    unique_books=0   
    discount_rate=0

    if 'book1' in book_list:       
        unique_books +=1
        book_list.remove("book1")
        #print(book_list)

    if 'book2' in book_list:       
        unique_books +=1
        book_list.remove("book2")
        #print(book_list)

    if 'book3' in book_list:       
        unique_books +=1
        book_list.remove("book3")
        #print(book_list)

    if 'book4' in book_list:       
        unique_books +=1
        book_list.remove("book4")
        #print(book_list)

    if 'book5' in book_list:       
        unique_books +=1
        book_list.remove("book5") 
    

    # biggest_discount_rate
        #discount_prize=((100-discount%)/100)*single_book_prize))
        #single_book_prize=8
    if unique_books==5:
        discount_rate=6*5
    #print(discount_rate)
    if unique_books==4:
        discount_rate=6.4*4
    #print(discount_rate)
    if unique_books==3:
        discount_rate=7.2*3
    #print(discount_rate)
    if unique_books==2:
        discount_rate=7.6*2
    #print(discount_rate)
    if unique_books==1:
        discount_rate=8 
    if unique_books=='':
        discount_rate=0 
    print("discount ratess  ",discount_rate)
    print("unique   ",unique_books)  
    return book_list 

def uniques_books_fun(unique_booklist):    

    if  len(unique_booklist) >=0:
        return biggest_discount(unique_booklist)
    pass
         

