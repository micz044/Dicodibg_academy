z = 0
try:
    x=1/z
    print(x)
except ZeroDivisionError:
    print("sayangku, tidak bisa oran bagi dengan nol")

try:
    with open('kode.py') as file:
        print(file.read())
except(FileNotFoundError, ):
    print("tidak ada filenya sayangku")