from task01 import caching_fibonacci
from task02 import sum_profit, generator_numbers

fibnum = caching_fibonacci()

print("число Фібоначчі для -1 =", fibnum(-1))
print("число Фібоначчі для 0 =", fibnum(0))
print("число Фібоначчі для 1 =", fibnum(1))
print("число Фібоначчі для 2 =", fibnum(2))
print("число Фібоначчі для 7 =", fibnum(7))
print("число Фібоначчі для 32 =", fibnum(32))
print("число Фібоначчі для 199 =", fibnum(199))
print("число Фібоначчі для 1024 =", fibnum(1024))
print("число Фібоначчі для 1536 =", fibnum(1536))

print("\n")
print("--- TASK 02 ---")
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")
