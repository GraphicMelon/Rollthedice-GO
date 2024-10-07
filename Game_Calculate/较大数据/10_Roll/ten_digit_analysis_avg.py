import pandas as pd

# 读取十位数分析结果的 CSV 文件
df = pd.read_csv('ten_digit_numbers_with_calculations.csv')

# 计算 "(8 - x) Mod 8" 列的平均值
average_modulo = df["(8 - x) Mod 8"].mean()

# 输出平均值
print(f"The average of (8 - x) Mod 8 is: {average_modulo}")
