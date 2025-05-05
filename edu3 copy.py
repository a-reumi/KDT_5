import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

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