import itertools
import pandas as pd

# 定义数字范围 1-6
numbers = [1, 2, 3, 4, 5, 6]

# 生成两位数的所有组合
combinations_2_digit = list(itertools.product(numbers, repeat=2))

# 将元组转换为两位数
two_digit_numbers = [''.join(map(str, comb)) for comb in combinations_2_digit]

# 计算每个两位数的数字之和
digit_sums_2 = [sum(int(digit) for digit in num) for num in two_digit_numbers]

# 计算数字之和对8取模的结果
modulo_8_2 = [digit_sum % 8 for digit_sum in digit_sums_2]

# 计算 (8 - x) % 8 的结果
modulo_complement_2 = [(8 - x) % 8 for x in modulo_8_2]

# 创建一个包含两位数、数字之和、模8结果和 (8 - x) % 8 的数据框
df_2_digit = pd.DataFrame({
    "Two-Digit Numbers": two_digit_numbers,
    "Sum of Digits": digit_sums_2,
    "Sum Mod 8": modulo_8_2,
    "(8 - x) Mod 8": modulo_complement_2
})

# 输出结果到 CSV 文件
df_2_digit.to_csv('two_digit_numbers_with_calculations.csv', index=False)

print("两位数的计算完成！结果已保存为 two_digit_numbers_with_calculations.csv")
