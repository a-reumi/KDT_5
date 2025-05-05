import os
import sys
import urllib.request
import json
import re
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 네이버 API 인증 정보
client_id = "s4I4P4GdHHdKKdkxo52z"
client_secret = "urxpdAXEDh"

# 블로그 검색을 위한 연도별 데이터 수집
search_keyword = "KDT, 국비교육, AI, 빅데이터, IT, 취업" 
years = ["2020", "2021", "2022", "2023", "2024"]  # 2020~2024년 5년치 데이터
text_data = ""

for year in years:
    encText = urllib.parse.quote(f"{search_keyword} {year}")
    url = f"https://openapi.naver.com/v1/search/blog?query={encText}&display=30"
    
    # API 요청 설정
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if rescode == 200:
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        
        # 블로그 제목만 출력 (연도별 크롤링)
        print(f"🔹 {year}년 블로그 제목 🔹")
        for item in result["items"]:
            title = re.sub(r'<.*?>', '', item["title"])  # HTML 태그 제거
            print(title)
            text_data += f"{title} "
    else:
        print(f"Error Code ({year}):", rescode)


# # 1) CSV 불러오기
# #    → "직무" 컬럼이 있다고 가정
# df = pd.read_csv("./blog_data.csv")

# # 2) "직무" 컬럼을 하나의 문자열로 합치기
# text_data = " ".join(df["year"].astype(str))

text=open('./2020.txt', encoding='utf-8').read()

# 3) 마스크 이미지 로드 (흑백 변환)
mask_image = Image.open("./cloud.png").convert("L")
mask_array = np.array(mask_image)

# 4) 워드클라우드 생성 (STOPWORDS 없음)
wordcloud = WordCloud(
    font_path="malgun.ttf",   # Windows 기준, 맑은 고딕 폰트
    background_color="white", # 배경색
    mask=mask_array,          # 마스크 적용
    width=800,
    height=600
).generate(text)

# 5) 시각화
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show() 

