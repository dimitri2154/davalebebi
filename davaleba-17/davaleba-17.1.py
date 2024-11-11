#########################
# linked list
#########################
# Node კლასი გამოიყენება დაკავშირებული სიის ელემენტების შესაქმნელად. თითოეული კვანძი შეიცავს ორ ატრიბუტს
# data: ინახავს კვანძის მნიშვნელობას.
# next: მიუთითებს სიის შემდეგ კვანძზე (ან არცერთზე, თუ ის ბოლო კვანძია).
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# LinkedList კლასი წარმოადგენს დაკავშირებულ სიას.
# head ატრიბუტი მიუთითებს სიის პირველ კვანძზე (თუ სია ცარიელი არ არის).
# თუ სია ცარიელია, head არის None.
class LinkedList:
    def __init__(self):
        self.head = None

# append მეთოდი ამატებს ახალ კვანძს მითითებული მონაცემებით დაკავშირებული სიის ბოლოს.
# თუ სია ცარიელია (self.head არის None), ახალი კვანძი ხდება სიის head-ი.
# წინააღმდეგ შემთხვევაში, ის იწყებს ბოლო კვანძის მოძებნას და აკავშირებს მას ახალ კვანძთან.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node # თუ სია ცარიელია, ახალი კვანძს მიანიჭებს head-ს
            return

        last_node = self.head # დაიწყებს სიის სათავიდან
        while last_node.next: # გაყვება სიის ბოლოს
            last_node = last_node.next

        last_node.next = new_node # ბოლო კვანძს დააკავშირებს ახალთან

# #remove_at მეთოდი შლის კვანძს მითითებულ ინდექსზე.
# თუ ინდექსი 0-ზე ნაკლებია ან სია ცარიელია, მეთოდი ბრუნდება არაფრის გაკეთების გარეშე.
# თუ ინდექსი არის 0, ის განაახლებს თავს შემდეგ კვანძს.
# წინააღმდეგ შემთხვევაში, ის გაყვება სიას, რომ იპოვოს კვანძი, რომელიც უნდა წაიშალოს და განაახლებს შემდეგ ,
    # რომ გამოტოვოს წასაშლელი კვანძი.
    def remove_at(self, index):
        if index < 0 or self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_position = 0

        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next: # თუ შემდეგი კვანძი არსებობს, ამოიღებს
            current_node.next = current_node.next.next

# display  მეთოდი ბეჭდავს დაკავშირებულ სიას კონსოლში და აჩვენებს თითოეული კვანძის მონაცემებს.
# იწყებს თავიდან, გადის მთელ სიას და ბეჭდავს თითოეული კვანძის მონაცემებს.
# -> იბეჭდება თითოეული კვანძის მონაცემებს შორის, რათა მიუთითოს კავშირი კვანძებს შორის.
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print()


#########################
# stack
#########################
# Stack კლასი წარმოადგენს სტეკის მონაცემთა სტრუქტურას, რომელიც მიჰყვება Last In, First Out პრინციპს.
# top_node მიუთითებს სტეკის ზედა კვანძზე (თუ ცარიელი არ არის).
# სიგრძე სტეკში ინახავს ელემენტების რაოდენობას.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None
        self.length = 0

    def empty(self):
        return self.length == 0 #თუ სიგრძე არის 0, დააბრუნებს True-ს, რაც მიუთითებს იმაზე რომ სტექი ცარიელია# .

    def size(self):
        return self.length # აბრუნებს სტეკის ახლანდელ ზომა

    def push(self, data):
        new_node = Node(data) # შექმინის ახალი კვანძს მოცემული მონაცემებით
        new_node.next = self.top_node # დააკავშირებს ახალი კვანძს სტეკის მიმდინარე ზედა ნაწილთან
        self.top_node = new_node # განაახლებს კვანძს
        self.length += 1 # გაიზრდება სტეკის ზომა

    def pop(self): # პოპ მეთოდი შლის და აბრუნებს სტეკის ზედა ელემენტს
        if not self.empty():
            popped_item = self.top_node.data # ინახავს ზედა კვანძის მონაცემებს
            self.top_node = self.top_node.next
            self.length -= 1 # შეამცირების სტეკის ზომას
            return popped_item # დააბრუნებს ამოღებულ  ელემენტს
        else:
            raise IndexError("Stack is empty")


