import streamlit as st

# 웹사이트의 대문(제목) 설정
st.set_page_config(page_title="학성여자고등학교 식물도감", page_icon="🌿")

st.title("🌿 학성여자고등학교 식물도감")
st.write("학성여자고등학교 교정에 어떤 식물들이 살고 있을까요?")

# 메뉴 선택 (사이드바)
menu = st.sidebar.selectbox("메뉴를 선택하세요", ["홈", "나무", "꽃", "지도"])
with st.sidebar:
    st.write("---") # 구분선
    st.caption("제작자: [30326 황연우]")
    st.caption("2026 [학성여자고등학교] 식물도감 프로젝트")


if menu == "홈":
    st.header("학성여자고등학교 식물도감에 오신 것을 환영합니다! 🤗")
    st.write("왼쪽 메뉴를 눌러 우리 학교의 식물들을 확인해 보세요.")
    # 학교 사진이 있다면 아래 주석(#)을 지우고 파일 이름을 넣으세요.
    st.image("학성여자고등학교 전경.jpg", caption="학성여자고등학교 전경")

   
elif menu == "나무":
    st.header("📖 나무 목록")
    
    # 탭 기능을 사용해 식물을 나누어 보여줍니다.
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["풍게나무", "사철나무", "단풍나무", "향나무", "배롱나무", "메티세콰이어", "등나무", "야자수", "호랑가시나무"])
    
    with tab1:
        st.subheader("풍게나무")
        st.info("4 ~ 5월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("10월경에 지름 7 ~ 8mm의 열매가 검은색으로 익습니다.")
        
    with tab2:
        st.subheader("사철나무")
        st.success("6 ~ 7월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("사철 내내 늘 푸른 잎을 보여주어 이름이 사철나무가 되었고, 꽃말도 '변함없다'를 뜻합니다.")
        
    with tab3:
        st.subheader("단풍나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.info("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")    

    with tab4:
        st.subheader("향나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.success("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")

    with tab5:
        st.subheader("배롱나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.info("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")

    with tab6:
        st.subheader("메티세콰이어")
        st.write("위치: 운동장 스탠드 뒤")
        st.success("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")  
    
    with tab7:
        st.subheader("등나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.info("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")
    
    with tab8:
        st.subheader("야자수")
        st.write("위치: 운동장 스탠드 뒤")
        st.success("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")
    
    with tab9:
        st.subheader("호랑가시나무")
        st.write("위치: 운동장 스탠드 뒤")
        st.info("가을이 되면 아름다운 단풍이 날리는 인기 만점 장소예요!")
        with st.expander("📖 더 자세한 이야기"):
                st.write("단풍나무는 일교차가 클수록 더욱 붉은색을 띱니다.")

elif menu == "꽃":
    st.header("📖 꽃 목록")
    
    # 탭 기능을 사용해 식물을 나누어 보여줍니다.
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["꽃마리", "붓꽃", "송엽국", "클로버", "고들빼기", "씀바귀"])
    
    with tab1:
        st.subheader("꽃마리")
        st.info("4 ~ 7월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("꽃대가 태엽처럼 펴지면서 자랍니다. 꽃말은 물망초의 꽃말과 동일한 '나를 잊지 말아요' 입니다.")
        
    with tab2:
        st.subheader("붓꽃")
        st.success("6 ~ 8월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("물을 좋아하여 하천, 습지, 연못 주변에 잘 자랍니다.")
        
        
    with tab3:
        st.subheader("송엽국")
        st.info("5 ~ 6월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("이름이 소나무 잎처럼 생긴 국화라 하여 송엽국이며, 여러해살이풀 입니다.")
    
    with tab4:
        st.subheader("클로버")
        st.success("6 ~ 8월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("행운의 상징인 네잎클로버는, 특정 유전자 조합이 존재하며 열성이라고 추정하고 있습니다. 기형이라고 합니다.") 

    with tab5:
        st.subheader("고들빼기")
        #st.write("위치: 운동장 스탠드 뒤")
        st.info("5 ~ 9월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("순천권에서는 김치나 나물로도 담궈먹기도 합니다.")              

    with tab6:
        st.subheader("씀바귀")
        #st.write("위치: 운동장 스탠드 뒤")
        st.info("5 ~ 7월에 개화합니다.")
        with st.expander("📖 더 자세한 이야기"):
                st.write("고들빼기와 혼동되기도 하는데, 씀바귀는 꽃술이 검은빛이고 잎이 줄기를 감싸지 않습니다.") 

elif menu == "지도":
    st.header("📖 지도")
    st.write("아래 지도로 우리 학교의 식물들의 위치를 확인해 보세요.")
    # 학교 사진이 있다면 아래 주석(#)을 지우고 파일 이름을 넣으세요.
    st.image("학성여자고등학교지도.png", caption="학성여자고등학교 지도")
