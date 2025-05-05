from urllib.request import urlopen
from bs4 import BeautifulSoup

# 검색 연도별 네이버 블로그 검색 URL 목록
urls = {
    2020: 'https://search.naver.com/search.naver?ssc=tab.blog.all&query=%22%EA%B5%AD%EB%B9%84%22%20%22%EA%B5%90%EC%9C%A1%22%20%22IT%22%20%22%EC%B7%A8%EC%97%85%22&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom20200101to20201231',
    2021: 'https://search.naver.com/search.naver?ssc=tab.blog.all&query=%22%EA%B5%AD%EB%B9%84%22%20%22%EA%B5%90%EC%9C%A1%22%20%22IT%22%20%22%EC%B7%A8%EC%97%85%22&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom20210101to20211231',
    2022: 'https://search.naver.com/search.naver?ssc=tab.blog.all&query=%22%EA%B5%AD%EB%B9%84%22%20%22%EA%B5%90%EC%9C%A1%22%20%22IT%22%20%22%EC%B7%A8%EC%97%85%22&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom20220101to20221231',
    2023: 'https://search.naver.com/search.naver?ssc=tab.blog.all&query=%22%EA%B5%AD%EB%B9%84%22%20%22%EA%B5%90%EC%9C%A1%22%20%22IT%22%20%22%EC%B7%A8%EC%97%85%22&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom20230101to20231231',
    2024: 'https://search.naver.com/search.naver?ssc=tab.blog.all&query=%22%EA%B5%AD%EB%B9%84%22%20%22%EA%B5%90%EC%9C%A1%22%20%22IT%22%20%22%EC%B7%A8%EC%97%85%22&sm=tab_opt&nso=so%3Ar%2Cp%3Afrom20240101to20241231',
}

# 연도별 href 속성 길이 총합 저장할 딕셔너리
yearly_href_lengths = {}

# 연도별 크롤링 수행
for year, url in urls.items():
    try:
        # 웹 페이지 열기
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')

        # href 속성 길이 리스트 생성
        href_lengths = [len(link.attrs['href']) for link in bs.find_all('a') if 'href' in link.attrs]

        # 총합 계산 후 저장
        yearly_href_lengths[year] = sum(href_lengths)

    except Exception as e:
        print(f"{year}년 데이터 수집 실패:", e)
        yearly_href_lengths[year] = None  # 오류 발생 시 None 값 저장

# 연도별 총 href 길이 출력
for year, total_length in yearly_href_lengths.items():
    print(f"{year}: {total_length}")





import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import koreanize_matplotlib

# ✅ 연도별 키워드 개수 데이터 (예제 데이터)
yearly_href_lengths = {
    2020: 18972,
    2021: 18724,
    2022: 17789,
    2023: 17024,
    2024: 18758,
}

# ✅ 데이터 준비
years = list(yearly_href_lengths.keys())   # 연도 리스트
total_lengths = list(yearly_href_lengths.values())  # 총 href 속성 길이 리스트

# ✅ 그래프 생성
fig, ax1 = plt.subplots(figsize=(10, 5))  # 그래프 크기 설정

# ✅ 막대 그래프 (왼쪽 Y축)
ax1.bar(years, total_lengths, color='skyblue', width=0.6, label="키워드 개수")
ax1.set_xlabel("연도", fontsize=12)  # X축 라벨
ax1.set_ylabel("키워드 개수", fontsize=12, color="blue")  # Y축 라벨
ax1.tick_params(axis="y", labelcolor="blue")

# ✅ 데이터 값 표시 (막대 위에 숫자 출력)
for i, txt in enumerate(total_lengths):
    ax1.text(years[i], total_lengths[i] + 500, str(txt), ha='center', fontsize=10, color="blue")

# ✅ 꺾은선 그래프 (막대 위쪽으로만 값 표시)
ax1.plot(years, total_lengths, marker='o', linestyle='-', linewidth=2, color='red', label="추세선")

# ✅ 그래프 제목 및 범례 추가
plt.title("연도별 키워드 변화 추이", fontsize=14)
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()

# ✅ 그래프 출력
plt.show()