# Day 2 · 2026-04-22 · pandas 基础

## 今天的目标
- [x] 读 McKinney Ch 5 的 Series / DataFrame / Index
- [x] 完成 `playground/01_pandas_basics.ipynb` 10 道练习
- [x] 理解 loc / iloc / 布尔索引
- [x] 写日志 + commit push

## 今天学到的核心知识

### Series
- Series 是带标签的一维数组，values + index
- 属性（无括号）：`.values`, `.index`, `.name`
- 方法（有括号）：`.isnull()`, `.notnull()`
- 布尔索引：`s[s > 0]`
- 两个 Series 相加会按 index 自动对齐，对不上的变 NaN

### DataFrame
- DataFrame 是多个 Series 按列拼接
- 建议始终用 `df['col']`，不要用 `df.col`（列名可能和方法重名）
- 加列：`df['new'] = value` 或一个 Series（自动对齐）
- 删列：`del df['col']`
- 转置：`df.T`

### loc vs iloc
- `loc` 用标签（label），`iloc` 用整数位置
- 切片关键区别：`loc` 含右端，`iloc` 不含右端 ← 经典坑
- 组合：`df.loc[布尔条件, [列1, 列2]]` 是量化最常用的模式

## 今天踩过的坑
1. **中文引号 vs 英文引号**：用中文输入法打的引号 Python 不认识，报 `unterminated string literal`
2. **`frame.pop` 和内置方法冲突**：列名是 `pop` 时，`df.pop` 访问的是方法而不是列。教训：永远用中括号
3. **`iloc[[0:2],1]` 语法错误**：切片不能放进列表里。列表只能放单个值，切片是独立语法
4. **`[4, 7-5, 3]` 少逗号**：Python 把 `7-5` 当成减法，结果静默变成 `[4, 2, 3]`。**最危险的 bug 是不报错的 bug**

## 今天的决策反思
（今天受消息影响，动了把苹果加入投资组合的念头，说明之前选股的思维模式没有完全改变，不是根据现有组合的投资原则做数据分析后下结论，而是被信息诱惑而动。反映出内心深处放大收益率的欲望仍很强，这个欲望没有错，这也是我现在开始学习量化的动力来源，但应该把预期和执行分开，先问自己如何执行才能实现预期，估计以后还会发生，有Cloude这面镜子，照见本性，慢慢磨练吧）

## 明天的重点
- pandas Ch 6：数据读取（read_csv）
- 用 yfinance 下载 SPY 数据，存成 DataFrame
- 计算移动均线（rolling mean）

## 时间花费
- 上午：Series 练习（约 2.5h）
- 下午：DataFrame + loc/iloc（约 3h）
- 日志：约 20 min