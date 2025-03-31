
import streamlit as st
from PIL import Image
import pytesseract
import io

st.title("📦 패키지 표시사항 검수기")

uploaded_file = st.file_uploader("라벨 이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 라벨", use_column_width=True)

    with st.spinner("OCR 텍스트 추출 중..."):
        image_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        extracted_text = pytesseract.image_to_string(image, lang="kor")
        st.success("텍스트 추출 완료!")

        st.subheader("📝 추출된 텍스트")
        st.text_area("OCR 결과", extracted_text, height=300)

    st.markdown("---")
    st.subheader("🧪 검사 항목 분석")

    row1 = st.columns(2)
    row1[0].info("📌 필수 항목 누락 분석\n\n(예: 유통기한, 원재료명 등)")
    row1[1].info("🔍 OCR 텍스트 자동 추출\n\n이미지에서 텍스트를 추출합니다.")

    row2 = st.columns(2)
    row2[0].info("✅ 식약처 필수 문구 자동 점검\n\n효능 주장 금지 문구 등 확인")
    row2[1].info("🌿 식품 필수 항목 분석\n\n건강기능식품 표기 기준 기반")

    row3 = st.columns(2)
    row3[0].info("⚠️ 경고 문구 포함 여부 확인\n\n주의사항/알레르기 문구 등")
    row3[1].info("📜 근거 법령 안내\n\n관련 고시 번호 표시")

    row4 = st.columns(2)
    row4[0].info("🔠 폰트 크기 분석 (예정)")
    row4[1].info("📑 표기 순서/구조 확인 (예정)")

    st.markdown("---")
    st.caption("제작자 : 박민지 ｜ hi.this.is.mine@gmail.com")
