import itertools
import pandas as pd

# 定义数字范围 1-6
numbers = [1, 2, 3, 4, 5, 6]

# 生成十位数的所有组合
combinations_10_digit = list(itertools.product(numbers, repeat=10))

# 将元组转换为十位数
ten_digit_numbers = [''.join(map(str, comb)) for comb in combinations_10_digit]

# 计算每个十位数的数字之和
digit_sums_10 = [sum(int(digit) for digit in num) for num in ten_digit_numbers]

# 计算数字之和对8取模的结果
modulo_8_10 = [digit_sum % 8 for digit_sum in digit_sums_10]

# 计算 (8 - x) % 8 的结果
modulo_complement_10 = [(8 - x) % 8 for x in modulo_8_10]

# 创建一个包含十位数、数字之和、模8结果和 (8 - x) % 8 的数据框
df_10_digit = pd.DataFrame({
    "Ten-Digit Numbers": ten_digit_numbers,
    "Sum of Digits": digit_sums_10,
    "Sum Mod 8": modulo_8_10,
    "(8 - x) Mod 8": modulo_complement_10
})

# 输出结果到 CSV 文件
df_10_digit.to_csv('ten_digit_numbers_with_calculations.csv', index=False)

print("计算完成！结果已保存为 ten_digit_numbers_with_calculations.csv")
