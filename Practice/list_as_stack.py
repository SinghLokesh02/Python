# Using List as st in Python

# Method - 1 Using OOps

# class stack:
#     # Method for pushing data into stack
#     def push(self, st, data):
#         st.append(data)

#     # Method for pop
#     def pop(self, st):
#         if len(st) > 0:
#             ans = st.pop()
#             print("Removed element from the st : ", ans)
#         else:
#             print("The stack is Empty")

#     # Method to get top of stack
#     def top(self, st):
#         if len(st) > 0:
#             return st[len(st) - 1]

#     # Method to check stack is Empty or not
#     def isEmpty(self, st):
#         if len(st) == 0:
#             return 1
#         else:
#             return 0

#     # Method to get size of stack
#     def size(self, st):
#         return len(st)


# # Creating Object of stack class
# st = stack()


# my_stack = ["Lokesh Singh", "Diwakar Singh", "Aniket Shivhare", "Ritik Srivastav"]

# # Printing the stack
# print(my_stack)

# # Printing the size of stack
# print(st.size(my_stack))

# # Removing the element of stack
# st.pop(my_stack)

# # Printing the top element of stack
# print("Top element in the stack : ",st.top(my_stack))

# # Check stack is Empty or not
# print(st.isEmpty(my_stack))

# # Push element into stack
# st.push(my_stack, "Vimal Kant")
# print("Stack after Push : ",my_stack)


# Direct Method using list methods

# Creating a empty list that represents stack
stack = []

# Pushing elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushing elements:", stack)

# Removing the element from the stack
popped = stack.pop()
print("Popped element from the stack:", popped)


# Printing the stack
print("Stack after popping element:", stack)


# Check stack is Empty or not
if not stack:
    print("Stack is Empty")
else:
    print("Stack is not Empty")
    
    
# Printing the top element of stack
print("Top element in the stack : ",stack[-1])


# Printing the size of stack
print("Size of stack : ",len(stack))

 