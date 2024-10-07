import pandas as pd

# 定义数字范围 1-6
numbers = [1, 2, 3, 4, 5, 6]

# 生成一位数的所有组合
one_digit_numbers = [str(num) for num in numbers]

# 计算每个一位数的数字之和（其实就是数字本身）
digit_sums_1 = [int(num) for num in one_digit_numbers]

# 计算数字之和对8取模的结果
modulo_8_1 = [digit_sum % 8 for digit_sum in digit_sums_1]

# 计算 (8 - x) % 8 的结果
modulo_complement_1 = [(8 - x) % 8 for x in modulo_8_1]

# 创建一个包含一位数、数字之和、模8结果和 (8 - x) % 8 的数据框
df_1_digit = pd.DataFrame({
    "One-Digit Numbers": one_digit_numbers,
    "Sum of Digits": digit_sums_1,
    "Sum Mod 8": modulo_8_1,
    "(8 - x) Mod 8": modulo_complement_1
})

# 输出结果到 CSV 文件
df_1_digit.to_csv('one_digit_numbers_with_calculations.csv', index=False)

print("一位数的计算完成！结果已保存为 one_digit_numbers_with_calculations.csv")
