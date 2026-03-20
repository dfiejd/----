import streamlit as st

# 웹사이트의 대문(제목) 설정
st.set_page_config(page_title="학성여자고등학교 식물 도감", page_icon="🌿")

st.title("🌿 학성여자고등학교 식물도감")
st.write("학성여자고등학교 교정에 어떤 식물들이 살고 있을까요?")
st.divider() # 구분선
    
# 🌟 제작자 이름 넣는 부분 🌟
st.markdown("### **🛠️ 제작자 정보**")
st.markdown("**학번/이름:** [30326 황연우]")
st.divider() # 구분선

# 메뉴 선택 (사이드바)
menu = st.sidebar.selectbox("메뉴를 선택하세요", ["홈", "식물 도감"])

if menu == "홈":
    st.header("학성여자고등학교 식물도감에 오신 것을 환영합니다! 🤗")
    st.write("왼쪽 메뉴에서 '식물 보기'를 눌러 우리 학교의 식물들을 확인해 보세요.")
    # 학교 사진이 있다면 아래 주석(#)을 지우고 파일 이름을 넣으세요.
    st.image("test_main.jpg", caption="우리 학교 전경")

elif menu == "식물 보기":
    st.header("📖 식물 도감 목록")
    
    # 탭 기능을 사용해 식물을 나누어 보여줍니다.
    tab1, tab2, tab3 = st.tabs(["소나무", "벚나무", "단풍나무"])
    
    with tab1:
        st.subheader("🌲 소나무")
        st.write("위치: 정문 옆")
        st.info("우리 학교의 교목입니다. 일 년 내내 푸른 잎을 자랑하죠.")
        
    with tab2:
        st.subheader("🌸 벚나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.success("봄이 되면 아름다운 꽃잎이 날리는 인기 만점 장소예요!")
        
    with tab3:
        st.subheader("🍁 단풍나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.info("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")       
