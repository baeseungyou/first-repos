# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 09:03:28 2023

@author: sayth
"""

import pandas as pd

input_excel_file = r"C:\Users\sayth\OneDrive\바탕 화면\기말 프로젝트\남녀유동인구17년도.xlsx"  # 엑셀 파일 경로
output_csv_file = r"C:\Users\sayth\OneDrive\바탕 화면\기말 프로젝트\남녀유동인구17년도.csv"  # 저장될 CSV 파일 경로

data_frame = pd.read_excel(input_excel_file)  # 엑셀 파일 읽기
data_frame.to_csv(output_csv_file, index=False)  # CSV 파일로 저장

import pandas as pd

input_excel_file = r"C:\Users\sayth\OneDrive\바탕 화면\기말 프로젝트\남녀유동인구22년도.xlsx"  # 엑셀 파일 경로
output_csv_file = r"C:\Users\sayth\OneDrive\바탕 화면\기말 프로젝트\남녀유동인구22년도.csv"  # 저장될 CSV 파일 경로

data_frame = pd.read_excel(input_excel_file)  # 엑셀 파일 읽기
data_frame.to_csv(output_csv_file, index=False)  # CSV 파일로 저장