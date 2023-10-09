from tkinter import *

history = []

while True:
    # Nhập dữ liệu từ người dùng
    user_input = input("Nhập một từ: ")
    
    # Lưu giá trị vào lịch sử
    history.append(user_input)
    
    # Xuất giá trị vừa nhập
    print("Bạn vừa nhập:", user_input)
    
    # Kiểm tra nếu người dùng muốn thoát
    exit_choice = input("Bạn có muốn thoát (y/n)? ")
    if exit_choice.lower() == 'y':
        break

# In ra lịch sử đã nhập và xuất
print("Lịch sử đã nhập và xuất:")
for item in history:
    print(item)
