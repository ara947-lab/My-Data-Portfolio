import streamlit as st
from PIL import Image

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="TFT 시즌3 메타 분석 대시보드", layout="wide")

st.title("🎮 TFT 시즌3 메타 분석 대시보드")
st.caption("상위 티어 매치 데이터를 기반으로 조합·챔피언·시너지·아이템 메타를 정리한 보드")

# -----------------------------
# KPI 카드 (현황판)
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("전체 플레이 데이터 수", "396,245")
col2.metric("챔피언 개수", "54")
col3.metric("TOP10 평균 승률", "약 18%")
col4.metric("TOP4 기대값 평균", "약 0.56")

st.write("---")

# -----------------------------
# 요약 그래프 5개 한 번에 보여주기
# -----------------------------
st.subheader("📊 KPI 요약")

row1_col1, row1_col2, row1_col3 = st.columns(3)
row2_col1, row2_col2 = st.columns(2)

row1_col1.image("charts/kpi1_top10_combination_winrate.png", caption="KPI1: 조합 승률", use_column_width=True)
row1_col2.image("charts/kpi2_champion_freq.png", caption="KPI2: 챔피언 빈도", use_column_width=True)
row1_col3.image("charts/kpi3_synergy_freq.png", caption="KPI3: 시너지 등장 비율", use_column_width=True)

row2_col1.image("charts/kpi4_top4_vs_winrate.png", caption="KPI4: 기대값 vs 승률", use_column_width=True)
row2_col2.image("charts/kpi5_item_pickrate.png", caption="KPI5: 아이템 픽률", use_column_width=True)

st.write("---")

# -----------------------------
# 상세 분석 탭
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "KPI1: 조합 승률",
    "KPI2: 챔피언 빈도",
    "KPI3: 시너지 비율",
    "KPI4: 기대값 비교",
    "KPI5: 아이템 픽률"
])

# ========== KPI1 ==============
with tab1:
    st.subheader("📌 KPI1: TOP 10 조합 승률")
    st.image("charts/kpi1_top10_combination_winrate.png", use_column_width=True)
    st.markdown("""
    **설명**  
    - 최소 경기수 조건을 충족한 조합 중 **승률 상위 10개**만 정렬한 그래프입니다.  
    - 막대가 높을수록 **1등 비율이 높은 조합**입니다.
    """)

# ========== KPI2 ==============
with tab2:
    st.subheader("📌 KPI2: 챔피언 등장 빈도")
    st.image("charts/kpi2_champion_freq.png", use_column_width=True)
    st.markdown("""
    **설명**  
    - **TOP10 조합**과 **WORST10 조합** 양쪽에서 등장한 챔피언 빈도를 비교합니다.  
    - 차이가 크면 **메타 핵심 챔피언**으로 볼 수 있습니다.
    """)

# ========== KPI3 ==============
with tab3:
    st.subheader("📌 KPI3: 시너지 등장 비율")
    st.image("charts/kpi3_synergy_freq.png", use_column_width=True)
    st.markdown("""
    **설명**  
    - 챔피언을 시너지 단위로 묶어서 TOP10 / WORST10에서의 사용 비율을 비교합니다.  
    - 특정 시너지가 강한 조합에만 등장한다면 **핵심 시너지**,  
      양쪽에서 모두 많이 등장하면 **범용 시너지**입니다.
    """)

# ========== KPI4 ==============
with tab4:
    st.subheader("📌 KPI4: 기대값 vs 실제 승률")
    st.image("charts/kpi4_top4_vs_winrate.png", use_column_width=True)
    st.markdown("""
    **설명**  
    - **TOP4 진입 비율(안정성)** 과 **1등 비율(결승력)** 을 비교합니다.  
    - 기대값 대비 실제 승률이 높으면 **폭발력이 있는 조합**,  
      반대로 낮으면 **안정적이지만 우승력은 약한 조합**입니다.
    """)

# ========== KPI5 ==============
with tab5:
    st.subheader("📌 KPI5: 아이템 픽률")
    st.image("charts/kpi5_item_pickrate.png", use_column_width=True)
    st.markdown("""
    **설명**  
    - TOP10 / WORST10 조합의 아이템 사용 빈도를 비교합니다.  
    - TOP10 조합에서 훨씬 많이 등장하는 아이템은 **핵심 아이템**입니다.
    """)

st.write("---")
st.caption("※ 1차 버전: 계산·전처리·시각화 결과를 정리한 대시보드입니다.")