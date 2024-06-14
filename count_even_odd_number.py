# Goal: Nhập chuỗi các số và đếm xem có bao nhiêu số even/ odd

# Bước 1: Nhập 1 list từ bàn phím
  # Xác định số phần tử sẽ có của list cần tạo:
n = int(input("Số phần tử trong list: "))
# khởi tạo một list rỗng:
a = []
# chèn các số nhập từ bàn phím vào bên phải của list:
for i in range(n):
  a.append(input(f"Nhập ký tự thứ {i}: ")
  print("List đã tạo là : ", a)
