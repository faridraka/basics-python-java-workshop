# TODO: Fungsi untuk memeriksa apakah sebuah bilangan genap
def is_even(num):
    return True if num % 2 == 0 else False

# Tes fungsi
print(is_even(4))   # True
print(is_even(7))   # False

# TODO: Fungsi untuk menghitung faktorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Tes fungsi
print(factorial(5))  # 120
print(factorial(0))  # 1
