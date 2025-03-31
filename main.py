import streamlit as st
from PIL import Image, UnidentifiedImageError
import pytesseract

st.set_page_config(page_title="패키지 표시사항 검사기", layout="centered")

st.title("📦 패키지 표시사항 검사기")
st.markdown("라벨 이미지를 업로드해주세요")

uploaded_file = st.file_uploader(
    "Drag and drop file here",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)

extracted_text = ""

if uploaded_file:
    try:
        uploaded_file.seek(0)
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드한 라벨", use_container_width=True)

        with st.spinner("🌀 OCR 텍스트 추출 중..."):
            extracted_text = pytesseract.image_to_string(image, lang="kor")
            st.success("텍스트 추출 완료!")

        st.subheader("📋 추출된 텍스트")
        st.text_area("OCR 결과", extracted_text, height=300)

    except UnidentifiedImageError:
        st.error("❌ 이미지를 열 수 없습니다. PNG, JPG 형식의 이미지 파일만 지원됩니다.")

st.markdown("---")
st.subheader("🧾 검사 항목 분석")

row1 = st.columns(2)
row1[0].info("📌 필수 항목 누락 분석\n\n(예: 유통기한, 원재료명 등)")
row1[1].info("🧠 OCR 텍스트 자동 추출\n\n이미지에서 텍스트를 추출합니다.")

row2 = st.columns(2)
row2[0].info("✅ 식약처 필수 문구 자동 점검\n\n효능 주장 금지 문구 등 확인")
row2[1].info("🍱 식품 필수 항목 분석\n\n건강기능식품 표기 기준 기반")

row3 = st.columns(2)
row3[0].info("⚠️ 경고 문구 포함 여부 확인\n\n주의사항/알레르기 문구 등")
row3[1].info("📖 근거 법령 안내\n\n관련 고시 번호 표시")

row4 = st.columns(2)
row4[0].info("🔠 폰트 크기 분석 (예정)")
row4[1].info("📋 표기 순서/구조 확인 (예정)")

st.markdown("---")
st.caption("제작자 : 박민지 | hi.this.is.mine@gmail.com")

