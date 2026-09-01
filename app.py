import streamlit as st

st.title("streamlit web testing")
st.header("header")
st.divider()
st.markdown("----------")
st.text("===============")
st.caption("caption")
st.text("text")
st.code("""code
123
456
""")

st.latex(r"\cfrac{1}{a + \cfrac{7}{b + \cfrac{2}{9}}} =c")
st.latex(r"\oint_{a}^{ir} ")
st.latex(r"\beta \phi \omega \phi ")
st.markdown("""
        :sunglasses:
""")
st.chat_input("Is it over?")
st.number_input("Pain Index",1,10,7)
st.slider("Hopelessness Index",1,100,67)
st.date_input("等待之日")
st.date_input("HBDMDIR")
st.time_input("靜待之時")

with st.sidebar:
    st.header("選單在此")
    st.write("選單內容")
    st.button("躍入過去")
    st.button("重返未來")

with st.bottom:
    st.header("相關資訊")
    st.write("相關資訊內容")

