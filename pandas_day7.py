# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:20:57 2021

@author: qkrfo
"""

#판다스 내장 그래프 도구 활용
#선그리기
import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl')  # 데이터프레임 변환 

df_ns = df.iloc[[0, 5], 3:]            # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South','North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int) # 열 이름의 자료형을 정수형으로 변경
print(df_ns.head())
print('\n')

# 선 그래프 그리기
df_ns.plot()

# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()
print('\n')

# 행, 열 전치하여 막대 그래프 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot(kind='bar')
print('\n')

# 행, 열 전치하여 히스토그램 그리기
tdf_ns = df_ns.T
tdf_ns.plot(kind='hist')

# read_csv() 함수로 df 생성
df2 = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df2.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 2개의 열을 선택하여 산점도 그리기
df2.plot(x='weight',y='mpg', kind='scatter')

# 열을 선택하여 박스 플롯 그리기
df2[['mpg','cylinders']].plot(kind='box')