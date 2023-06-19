# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:14:40 2023

@author: sayth
"""

#17년도 남녀합계

import pandas as pd
import numpy as np

colnames = ['STDR_YMD_CD', 'TMZON', 'ADSTRD_CD', 'MGU_CD', 'SPOP', 'M0009', 'M1014', 'M1519', 'M2024', 'M2529', 'M3034', 'M3539', 'M4044', 'M4549', 'M5054', 'M5559', 'M6064', 'M6569', 'M7074', 'M7579', 'M8000', 'W0009', 'W1014', 'W1519', 'W2024', 'W2529', 'W3034', 'W3539', 'W4044', 'W4549', 'W5054', 'W5559', 'W6064', 'W6569', 'W7074', 'W7579', 'W8000']

# CSV 파일 경로
csv_path = r"C:/Users/sayth/OneDrive/바탕 화면/기말 프로젝트/TBDW_SPOP_LOCAL_RESD_201707.csv"

# CSV 파일 읽기
df = pd.read_csv(csv_path, names=colnames, sep='|')
print(df)

#2029 연령대
#삼성1동
samsung1_values = df.loc[(df["ADSTRD_CD"] == 11680580) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if samsung1_values.size > 0:
    samsung1_sum = np.nansum(np.nan_to_num(samsung1_values, nan=0), axis=1)
    samsung1_total = np.sum(samsung1_sum)
else:
    samsung1_sum = []
    samsung1_total = 0

#여의동
yeouido_values = df.loc[(df["ADSTRD_CD"] == 11560540) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if yeouido_values.size > 0:
    yeouido_sum = np.nansum(np.nan_to_num(yeouido_values, nan=0), axis=1)
    yeouido_total = np.sum(yeouido_sum)
else:
    yeouido_sum = []
    yeouido_total = 0

#잠실6동
jamsil6_values = df.loc[(df["ADSTRD_CD"] == 11710710) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if jamsil6_values.size > 0:
    jamsil6_sum = np.nansum(np.nan_to_num(jamsil6_values, nan=0), axis=1)
    jamsil6_total = np.sum(jamsil6_sum)
else:
        jamsil6_sum = []
        jamsil6_total = 0

#잠실3동
jamsil3_values = df.loc[(df["ADSTRD_CD"] == 11710680) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if jamsil3_values.size > 0:
    jamsil3_sum = np.nansum(np.nan_to_num(jamsil3_values, nan=0), axis=1)
    jamsil3_total = np.sum(jamsil3_sum)
else:
        jamsil3_sum = []
        jamsil3_total = 0
        
#잠실2동
jamsil2_values = df.loc[(df["ADSTRD_CD"] == 11710670) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if jamsil2_values.size > 0:
    jamsil2_sum = np.nansum(np.nan_to_num(jamsil2_values, nan=0), axis=1)
    jamsil2_total = np.sum(jamsil2_sum)
else:
        jamsil2_sum = []
        jamsil2_total = 0
        
#한강로동
hangangro_values = df.loc[(df["ADSTRD_CD"] == 11170625) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if hangangro_values.size > 0:
    hangangro_sum = np.nansum(np.nan_to_num(hangangro_values, nan=0), axis=1)
    hangangro_total = np.sum(hangangro_sum)
else:
        hangangro_sum = []
        hangangro_total = 0

#가락1동
garack1_values = df.loc[(df["ADSTRD_CD"] == 11710631) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if garack1_values.size > 0:
    garack1_sum = np.nansum(np.nan_to_num(garack1_values, nan=0), axis=1)
    garack1_total = np.sum(garack1_sum)
else:
        garack1_sum = []
        garack1_total = 0

#문정2동
moonjeong2_values = df.loc[(df["ADSTRD_CD"] == 11710642) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if moonjeong2_values.size > 0:
    moonjeong2_sum = np.nansum(np.nan_to_num(moonjeong2_values, nan=0), axis=1)
    moonjeong2_total = np.sum(moonjeong2_sum)
else:
        moonjeong2_sum = []
        moonjeong2_total = 0

#목1동
mock1_values = df.loc[(df["ADSTRD_CD"] == 11470510) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M1014", "M1519", "W1014", "W1519"]].values
if mock1_values.size > 0:
    mock1_sum = np.nansum(np.nan_to_num(mock1_values, nan=0), axis=1)
    mock1_total = np.sum(mock1_sum)
else:
        mock1_sum = []
        mock1_total = 0
        
#2029 합계와 총합들
print("삼성1동 합계:")
print(samsung1_sum)
print("삼성1동 1019 총합:")
print(samsung1_total)

print("여의동 합계:")
print(yeouido_sum)
print("여의동 1019 총합:")
print(yeouido_total)

print("잠실6동 합계:")
print(jamsil6_sum)
print("잠실6동 1019 총합:")
print(jamsil6_total)

print("잠실3동 합계:")
print(jamsil3_sum)
print("잠실3동 1019 총합:")
print(jamsil3_total)

print("잠실2동 합계:")
print(jamsil2_sum)
print("잠실2동 1019 총합:")
print(jamsil2_total)

print("한강로동 합계:")
print(hangangro_sum)
print("한강로동 1019 총합:")
print(hangangro_total)

print("가락1동 합계:")
print(garack1_sum)
print("가락1동 1019 총합:")
print(garack1_total)

print("문정2동 합계:")
print(moonjeong2_sum)
print("문정2동 1019 총합:")
print(moonjeong2_total)

print("목1동 합계:")
print(mock1_sum)
print("목1동 1019 총합:")
print(mock1_total)