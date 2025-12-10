import numpy as np
import matplotlib.pyplot as plt
import math

# 1. 描画範囲の設定 (-10から20まで)
x = np.linspace(-10, 20, 400)

# 2. 本物の sin(x)
y_true = np.sin(x)

# 3. マクローリン展開の近似関数を作る (ここがテストです)
def taylor_sin(x_val, n_terms):
    """
    x_val: 入力値 (numpy配列)
    n_terms: 項数 (例: n=1なら x, n=3なら x - x^3/3! ...)
    """
    approx = np.zeros_like(x_val)
    
    for i in range(n_terms):
        # sin(x) = Σ ((-1)^i / (2i+1)!) * x^(2i+1)
        term = ((-1)**i / math.factorial(2*i + 1)) * (x_val ** (2*i + 1))
        approx += term
        
    return approx

# 4. グラフを描画
plt.figure(figsize=(12, 6))
plt.plot(x, y_true, label='True sin(x)', color='black', linewidth=2)

# 次数ごとの近似をプロット
terms_list = [1, 5, 15] # 項数 (1項=1次, 2項=3次, 3項=5次...)
colors = ['red', 'blue', 'green']

for n, color in zip(terms_list, colors):
    y_approx = taylor_sin(x, n)
    plt.plot(x, y_approx, label=f'Taylor (n={n} terms)', color=color, linestyle='--')

# グラフの体裁
plt.ylim(-2, 2) # y軸の範囲を制限 (暴れる君を見やすくするため)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title('Taylor Series Approximation of sin(x): Success and Failure')
plt.grid(True)
plt.show()
