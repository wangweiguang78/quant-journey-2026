import pandas as pd
import yfinance as yf

print("=" * 50)
print("Phase 1 Environment Check · 2026-04-21")
print("=" * 50)

print("\n正在下载 SPY 数据...")
data = yf.download("SPY", period="5d", progress=False)

print("\nSPY 最近 5 天收盘价：")
print(data['Close'].tail())

print("\n环境完全正常！可以开始 Project 1 了。")