# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 10:00:56 2023

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

#6069 연령대

#소공동
sogong_values = df.loc[(df["ADSTRD_CD"] == 11140520) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if sogong_values.size > 0:
    sogong_sum = np.nansum(np.nan_to_num(sogong_values, nan=0), axis=1)
    sogong_total = np.sum(sogong_sum)
else:
        sogong_sum = []
        sogong_total = 0
        
#반포4동
banpo4_values = df.loc[(df["ADSTRD_CD"] == 11650581) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if banpo4_values.size > 0:
    banpo4_sum = np.nansum(np.nan_to_num(banpo4_values, nan=0), axis=1)
    banpo4_total = np.sum(banpo4_sum)
else:
        banpo4_sum = []
        banpo4_total = 0
        
#가양1동
gayang1_values = df.loc[(df["ADSTRD_CD"] == 11500603) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if gayang1_values.size > 0:
    gayang1_sum = np.nansum(np.nan_to_num(gayang1_values, nan=0), axis=1)
    gayang1_total = np.sum(gayang1_sum)
else:
        gayang1_sum = []
        gayang1_total = 0
        
#서초4동
seocho4_values = df.loc[(df["ADSTRD_CD"] == 11650531) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if seocho4_values.size > 0:
    seocho4_sum = np.nansum(np.nan_to_num(seocho4_values, nan=0), axis=1)
    seocho4_total = np.sum(seocho4_sum)
else:
        seocho4_sum = []
        seocho4_total = 0
        
#회현동
hyeon_values = df.loc[(df["ADSTRD_CD"] == 11140540) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if hyeon_values.size > 0:
    hyeon_sum = np.nansum(np.nan_to_num(hyeon_values, nan=0), axis=1)
    hyeon_total = np.sum(hyeon_sum)
else:
        hyeon_sum = []
        hyeon_total = 0
        
#종로1~4가
jongro1_4_values = df.loc[(df["ADSTRD_CD"] == 11110615) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if jongro1_4_values.size > 0:
    jongro1_4_sum = np.nansum(np.nan_to_num(jongro1_4_values, nan=0), axis=1)
    jongro1_4_total = np.sum(jongro1_4_sum)
else:
        jongro1_4sum = []
        jongro1_4_total = 0

#명동
meongdong_values = df.loc[(df["ADSTRD_CD"] == 11140550) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if meongdong_values.size > 0:
    meongdong_sum = np.nansum(np.nan_to_num(meongdong_values, nan=0), axis=1)
    meongdong_total = np.sum(meongdong_sum)
else:
        meongdong_sum = []
        meongdong_total = 0

#진관동
jinkwandong_values = df.loc[(df["ADSTRD_CD"] == 11380690) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if jinkwandong_values.size > 0:
    jinkwandong_sum = np.nansum(np.nan_to_num(jinkwandong_values, nan=0), axis=1)
    jinkwandong_total = np.sum(jinkwandong_sum)
else:
    jinkwandong_sum = []
    jinkwandong_total = 0
        
#오륜동
fiveryu_values = df.loc[(df["ADSTRD_CD"] == 11710566) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  fiveryu_values.size > 0:
    fiveryu_sum = np.nansum(np.nan_to_num(fiveryu_values, nan=0), axis=1)
    fiveryu_total = np.sum(fiveryu_sum)
else:
    fiveryu_sum = []
    fiveryu_total = 0
        
#사직동
fourjick_values = df.loc[(df["ADSTRD_CD"] == 11110530) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  fourjick_values.size > 0:
    fourjick_sum = np.nansum(np.nan_to_num(fourjick_values, nan=0), axis=1)
    fourjick_total = np.sum(fourjick_sum)
else:
    fourjick_sum = []
    fourjick_total = 0

#서교동
kyo_values = df.loc[(df["ADSTRD_CD"] == 11440660) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  kyo_values.size > 0:
    kyo_sum = np.nansum(np.nan_to_num(kyo_values, nan=0), axis=1)
    kyo_total = np.sum(kyo_sum)
else:
    kyo_sum = []
    kyo_total = 0
        
#상계2동
sanggye2_values = df.loc[(df["ADSTRD_CD"] == 11350640) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  sanggye2_values.size > 0:
    sanggye2_sum = np.nansum(np.nan_to_num(sanggye2_values, nan=0), axis=1)
    sanggye2_total = np.sum(sanggye2_sum)
else:
    sanggye2_sum = []
    sanggye2_total = 0
 
#신촌동
sinchon_values = df.loc[(df["ADSTRD_CD"] == 11410585) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  sinchon_values.size > 0:
    sinchon_sum = np.nansum(np.nan_to_num(sinchon_values, nan=0), axis=1)
    sinchon_total = np.sum(sinchon_sum)
else:
    sinchon_sum = []
    sinchon_total = 0

#영등포동
youngback_values = df.loc[(df["ADSTRD_CD"] == 11560535) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  youngback_values.size > 0:
    youngback_sum = np.nansum(np.nan_to_num(youngback_values, nan=0), axis=1)
    youngback_total = np.sum(youngback_sum)
else:
    youngback_sum = []
    youngback_total = 0

#남영동
manyoung_values = df.loc[(df["ADSTRD_CD"] == 11170530) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  manyoung_values.size > 0:
    manyoung_sum = np.nansum(np.nan_to_num(manyoung_values, nan=0), axis=1)
    manyoung_total = np.sum(manyoung_sum)
else:
    manyoung_sum = []
    manyoung_total = 0

#압구정동
ap9jeong_values = df.loc[(df["ADSTRD_CD"] == 11680545) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  ap9jeong_values.size > 0:
    ap9jeong_sum = np.nansum(np.nan_to_num(ap9jeong_values, nan=0), axis=1)
    ap9jeong_total = np.sum(ap9jeong_sum)
else:
    ap9jeong_sum = []
    ap9jeong_total = 0

#고덕1동
highduck1_values = df.loc[(df["ADSTRD_CD"] == 11740550) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  highduck1_values.size > 0:
    highduck1_sum = np.nansum(np.nan_to_num(highduck1_values, nan=0), axis=1)
    highduck1_total = np.sum(highduck1_sum)
else:
    highduck1_sum = []
    highduck1_total = 0

#상암동
sangarm_values = df.loc[(df["ADSTRD_CD"] == 11440740) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  sangarm_values.size > 0:
    sangarm_sum = np.nansum(np.nan_to_num(sangarm_values, nan=0), axis=1)
    sangarm_total = np.sum(sangarm_sum)
else:
    sangarm_sum = []
    sangarm_total = 0

#대치1동
daechi1_values = df.loc[(df["ADSTRD_CD"] == 11680600) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  daechi1_values.size > 0:
    daechi1_sum = np.nansum(np.nan_to_num(daechi1_values, nan=0), axis=1)
    daechi1_total = np.sum(daechi1_sum)
else:
    daechi1_sum = []
    daechi1_total = 0

#방화2동
fire2_values = df.loc[(df["ADSTRD_CD"] == 11500640) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  fire2_values.size > 0:
    fire2_sum = np.nansum(np.nan_to_num(fire2_values, nan=0), axis=1)
    fire2_total = np.sum(fire2_sum)
else:
    fire2_sum = []
    fire2_total = 0

#풍납2동
poongnap2_values = df.loc[(df["ADSTRD_CD"] == 11710520) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  poongnap2_values.size > 0:
    poongnap2_sum = np.nansum(np.nan_to_num(poongnap2_values, nan=0), axis=1)
    poongnap2_total = np.sum(poongnap2_sum)
else:
    poongnap2_sum = []
    poongnap2_total = 0

#광희동
kwanghee_values = df.loc[(df["ADSTRD_CD"] == 11140590) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  kwanghee_values.size > 0:
    kwanghee_sum = np.nansum(np.nan_to_num(kwanghee_values, nan=0), axis=1)
    kwanghee_total = np.sum(kwanghee_sum)
else:
    kwanghee_sum = []
    kwanghee_total = 0

#등촌3동
backcheon3_values = df.loc[(df["ADSTRD_CD"] == 11500535) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  backcheon3_values.size > 0:
    backcheon3_sum = np.nansum(np.nan_to_num(backcheon3_values, nan=0), axis=1)
    backcheon3_total = np.sum(backcheon3_sum)
else:
    backcheon3_sum = []
    backcheon3_total = 0

#강일동
river1_values = df.loc[(df["ADSTRD_CD"] == 11740515) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  river1_values.size > 0:
    river1_sum = np.nansum(np.nan_to_num(river1_values, nan=0), axis=1)
    river1_total = np.sum(river1_sum)
else:
    river1_sum = []
    river1_total = 0

#역삼1동
yock3_1_values = df.loc[(df["ADSTRD_CD"] == 11680640) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  yock3_1_values.size > 0:
    yock3_1_sum = np.nansum(np.nan_to_num(yock3_1_values, nan=0), axis=1)
    yock3_1_total = np.sum(yock3_1_sum)
else:
    yock3_1_sum = []
    yock3_1_total = 0

#공항동
airport_values = df.loc[(df["ADSTRD_CD"] == 11500620) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  airport_values.size > 0:
    airport_sum = np.nansum(np.nan_to_num(airport_values, nan=0), axis=1)
    airport_total = np.sum(airport_sum)
else:
    airport_sum = []
    airport_total = 0

#구의3동
gu3_values = df.loc[(df["ADSTRD_CD"] == 11215870) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  gu3_values.size > 0:
    gu3_sum = np.nansum(np.nan_to_num(gu3_values, nan=0), axis=1)
    gu3_total = np.sum(gu3_sum)
else:
    gu3_sum = []
    gu3_total = 0

#신사동
gentleman_values = df.loc[(df["ADSTRD_CD"] == 11620685) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  gentleman_values.size > 0:
    gentleman_sum = np.nansum(np.nan_to_num(gentleman_values, nan=0), axis=1)
    gentleman_total = np.sum(gentleman_sum)
else:
    gentleman_sum = []
    gentleman_total = 0

#가산동
gasan_values = df.loc[(df["ADSTRD_CD"] == 11545510) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  gasan_values.size > 0:
    gasan_sum = np.nansum(np.nan_to_num(gasan_values, nan=0), axis=1)
    gasan_total = np.sum(gasan_sum)
else:
    gasan_sum = []
    gasan_total = 0

#신당동
sindang_values = df.loc[(df["ADSTRD_CD"] == 11140615) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  sindang_values.size > 0:
    sindang_sum = np.nansum(np.nan_to_num(sindang_values, nan=0), axis=1)
    sindang_total = np.sum(sindang_sum)
else:
    sindang_sum = []
    sindang_total = 0
    
#수유3동
suyou3_values = df.loc[(df["ADSTRD_CD"] == 11305630) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  suyou3_values.size > 0:
    suyou3_sum = np.nansum(np.nan_to_num(suyou3_values, nan=0), axis=1)
    suyou3_total = np.sum(suyou3_sum)
else:
    suyou3_sum = []
    suyou3_total = 0

#행당1동
hangdang1_values = df.loc[(df["ADSTRD_CD"] == 11200560) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  hangdang1_values.size > 0:
    hangdang1_sum = np.nansum(np.nan_to_num(hangdang1_values, nan=0), axis=1)
    hangdang1_total = np.sum(hangdang1_sum)
else:
    hangdang1_sum = []
    hangdang1_total = 0

#서빙고동
seobingo_values = df.loc[(df["ADSTRD_CD"] == 11170690) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  seobingo_values.size > 0:
    seobingo_sum = np.nansum(np.nan_to_num(seobingo_values, nan=0), axis=1)
    seobingo_total = np.sum(seobingo_sum)
else:
    seobingo_sum = []
    seobingo_total = 0

#청담동
cheongdam_values = df.loc[(df["ADSTRD_CD"] == 11680565) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  cheongdam_values.size > 0:
    cheongdam_sum = np.nansum(np.nan_to_num(cheongdam_values, nan=0), axis=1)
    cheongdam_total = np.sum(cheongdam_sum)
else:
    cheongdam_sum = []
    cheongdam_total = 0

#명일1동
meong1_values = df.loc[(df["ADSTRD_CD"] == 11740530) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  meong1_values.size > 0:
    meong1_sum = np.nansum(np.nan_to_num(meong1_values, nan=0), axis=1)
    meong1_total = np.sum(meong1_sum)
else:
    meong1_sum = []
    meong1_total = 0

#종로5,6가동
jongro5_6_values = df.loc[(df["ADSTRD_CD"] == 11110630) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  jongro5_6_values.size > 0:
    jongro5_6_sum = np.nansum(np.nan_to_num(jongro5_6_values, nan=0), axis=1)
    jongro5_6_total = np.sum(jongro5_6_sum)
else:
    jongro5_6_sum = []
    jongro5_6_total = 0

#상봉2동
sangbong2_values = df.loc[(df["ADSTRD_CD"] == 11260590) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  sangbong2_values.size > 0:
    sangbong2_sum = np.nansum(np.nan_to_num(sangbong2_values, nan=0), axis=1)
    sangbong2_total = np.sum(sangbong2_sum)
else:
    sangbong2_sum = []
    sangbong2_total = 0

#서초3동
seocho3_values = df.loc[(df["ADSTRD_CD"] == 11650530) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  seocho3_values.size > 0:
    seocho3_sum = np.nansum(np.nan_to_num(seocho3_values, nan=0), axis=1)
    seocho3_total = np.sum(seocho3_sum)
else:
    seocho3_sum = []
    seocho3_total = 0

#서초2동
seocho2_values = df.loc[(df["ADSTRD_CD"] == 11650520) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  seocho2_values.size > 0:
    seocho2_sum = np.nansum(np.nan_to_num(seocho2_values, nan=0), axis=1)
    seocho2_total = np.sum(seocho2_sum)
else:
    seocho2_sum = []
    seocho2_total = 0

#천호2동
cheonho2_values = df.loc[(df["ADSTRD_CD"] == 11740610) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  cheonho2_values.size > 0:
    cheonho2_sum = np.nansum(np.nan_to_num(cheonho2_values, nan=0), axis=1)
    cheonho2_total = np.sum(cheonho2_sum)
else:
    cheonho2_sum = []
    cheonho2_total = 0
        
#대학동
university_values = df.loc[(df["ADSTRD_CD"] == 11620735) & (df["STDR_YMD_CD"].isin([20170701, 20170708, 20170715, 20170722, 20170729])), ["STDR_YMD_CD", "M6064", "M6569", "W6064", "W6569"]].values
if  university_values.size > 0:
    university_sum = np.nansum(np.nan_to_num(university_values, nan=0), axis=1)
    university_total = np.sum(university_sum)
else:
    university_sum = []
    university_total = 0

#2029연령대

print("소공동 합계:")
print(sogong_sum)
print("소공동 6069 총합:")
print(sogong_total)

print("반포4동 합계:")
print(banpo4_sum)
print("반포4동 6069 총합:")
print(banpo4_total)

print("가양1동 합계:")
print(gayang1_sum)
print("가양1동 6069 총합:")
print(gayang1_total)

print("서초4동 합계:")
print(seocho4_sum)
print("서초4동 6069 총합:")
print(seocho4_total)

print("회현동 합계:")
print(hyeon_sum)
print("회현동 6069 총합:")
print(hyeon_total)

print("종로1~4가동 합계:")
print(jongro1_4_sum)
print("종로1~4가동 6069 총합:")
print(jongro1_4_total)

print("명동 합계:")
print(meongdong_sum)
print("명동 6069 총합:")
print(meongdong_total)

print("진관동 합계:")
print(jinkwandong_sum)
print("진관동 6069 총합:")
print(jinkwandong_total)

print("오륜동 합계:")
print(fiveryu_sum)
print("오륜동 6069 총합:")
print(fiveryu_total)

print("사직동 합계:")
print(fourjick_sum)
print("사직동 6069 총합:")
print(fourjick_total)

print("서교동 합계:")
print(kyo_sum)
print("서교동 6069 총합:")
print(kyo_total)

print("상계2동 합계:")
print(sanggye2_sum)
print("상계2동 6069 총합:")
print(sanggye2_total)

print("신촌동 합계:")
print(sinchon_sum)
print("신촌동 5059 총합:")
print(sinchon_total)

print("영등포 합계:")
print(youngback_sum)
print("영등포 6069 총합:")
print(youngback_total)

print("남영동 합계:")
print(manyoung_sum)
print("남영동 6069 총합:")
print(manyoung_total)

print("압구정동 합계:")
print(ap9jeong_sum)
print("압구정동 6069 총합:")
print(ap9jeong_total)

print("고덕1동 합계:")
print(highduck1_sum)
print("고덕1동 6069 총합:")
print(highduck1_total)

print("상암동 합계:")
print(sangarm_sum)
print("상암동 6069 총합:")
print(sangarm_total)

print("대치1동 합계:")
print(daechi1_sum)
print("대치1동 6069 총합:")
print(daechi1_total)

print("방화2동 합계:")
print(fire2_sum)
print("방화2동 6069 총합:")
print(fire2_total)

print("풍납2동 합계:")
print(poongnap2_sum)
print("풍납2동 6069 총합:")
print(poongnap2_total)

print("광희동 합계:")
print(kwanghee_sum)
print("광희동 6069 총합:")
print(kwanghee_total)

print("등촌3동 합계:")
print(backcheon3_sum)
print("등촌3동 6069 총합:")
print(backcheon3_total)

print("강일동 합계:")
print(river1_sum)
print("강일동 6069 총합:")
print(river1_total)

print("역삼1동 합계:")
print(yock3_1_sum)
print("역삼1동 6069 총합:")
print(yock3_1_total)

print("공항동 합계:")
print(airport_sum)
print("공항동 6069 총합:")
print(airport_total)

print("구의3동 합계:")
print(gu3_sum)
print("구의3동 6069 총합:")
print(gu3_total)

print("신사동 합계:")
print(gentleman_sum)
print("신사동 6069 총합:")
print(gentleman_total)

print("가산동 합계:")
print(gasan_sum)
print("가산동 6069 총합:")
print(gasan_total)

print("신당동 합계:")
print(sindang_sum)
print("신당동 6069 총합:")
print(sindang_total)

print("수유3동 합계:")
print(suyou3_sum)
print("수유3동 6069 총합:")
print(suyou3_total)

print("행당1동 합계:")
print(hangdang1_sum)
print("행당1동 6069 총합:")
print(hangdang1_total)

print("서빙고동 합계:")
print(seobingo_sum)
print("서빙고동 6069 총합:")
print(seobingo_total)

print("청담동 합계:")
print(cheongdam_sum)
print("청담동 6069 총합:")
print(cheongdam_total)

print("명일1동 합계:")
print(meong1_sum)
print("명일1동 6069 총합:")
print(meong1_total)

print("종로5,6가동 합계:")
print(jongro5_6_sum)
print("종로5,6가동 6069 총합:")
print(jongro5_6_total)

print("상봉2동 합계:")
print(sangbong2_sum)
print("상봉2동 6069 총합:")
print(sangbong2_total)

print("서초3동 합계:")
print(seocho3_sum)
print("서초3동 6069 총합:")
print(seocho3_total)

print("서초2동 합계:")
print(seocho2_sum)
print("서초2동 6069 총합:")
print(seocho2_total)

print("천호2동 합계:")
print(cheonho2_sum)
print("천호2동 6069 총합:")
print(cheonho2_total)

print("대학동 합계:")
print(university_sum)
print("대학동 6069 총합:")
print(university_total)