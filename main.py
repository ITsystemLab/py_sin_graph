# Sinグラグの生成

import numpy as np
import matplotlib.pyplot as plt

π= np.pi

# x座標の最小値
x0 = 0

# x座標の最大値
xMax = 2*π

x = np.linspace(x0, xMax, 100);

# Nsin(A)  の Nの値を入力してください。
times = 2 # 例: 1sin(A), 3sin(A)

# sin(ここ！) xが使えます。
s = x - π/4 # 例: 3x, π/4

# タイトル
title = "2sin(x - π/2)"

# ここから先は変更品でください。正しく表示されない場合があります。
plt.figure(0);
plt.plot(x, times*np.sin( s ));
plt.title(title);
plt.legend();
plt.show();
