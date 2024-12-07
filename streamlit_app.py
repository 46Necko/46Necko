import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# タイトル
st.title('二次関数のグラフ描画アプリ')

# ユーザーからの入力を受け取る
a = st.slider('aの値を選んでください', -10.0, 10.0, 1.0)
b = st.slider('bの値を選んでください', -10.0, 10.0, 0.0)
c = st.slider('cの値を選んでください', -10.0, 10.0, 0.0)

# 二次関数 f(x) = ax^2 + bx + c の計算
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

# グラフを描画
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}', color='blue')
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('二次関数のグラフ')
ax.legend()

# グラフをStreamlitに表示
st.pyplot(fig)
