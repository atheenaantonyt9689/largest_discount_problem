from biggest_discount import *
def runner():
    customer_booklist=["book1","book2","book2","book3","book4","book5","book2","book3"]
    #customer_booklist=[]
   
    unique_booklist=biggest_discount(customer_booklist)
    print("first ",unique_booklist)
    uniques_books_var=uniques_books_fun(unique_booklist)
    print("secondd ",uniques_books_var)



runner()