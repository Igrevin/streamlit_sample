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

"""
user=st.text_input("帳號")
passwd=st.text_input("密碼",type="password")

if st.button("好怕美夢", type="primary"):
    if not user or not passwd:
        st.warning("請輸入帳號與密碼")
        st.stop()

    try:
        conn = mariadb.connect(
            user=user,
            password=passwd,
            host="localhost",
            port=3306,
            database="aqidb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USERS")
        rows = cursor.fetchall()

        st.write("第一千零一夜", user)
        st.subheader("潺潺")
        st.write(rows)
    except mariadb.Error as e:
        st.error(f"資料庫錯誤: {e}")
    finally:
        if "conn" in locals():
            conn.close()

if st.button("朦朧", type="secondary"):
    st.write("浮生若夢", user)

if st.button("存在與否", type="secondary"):
    if not user or not passwd:
        st.warning("請輸入帳號與密碼")
        st.stop()

    try:
        conn = mariadb.connect(
            user="root",
            password=os.getenv("PASSWORD"),
            host="127.0.0.1",
            port=3306,
            database="aqidb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USERS WHERE name=%s AND email=%s",(user,passwd))
        row = cursor.fetchone()

        if row is not None:
            st.success("帳號與密碼存在於資料庫中")
            st.write("查詢結果：", row)
        else:
            st.warning("帳號或密碼不存在於資料庫中")
    except mariadb.Error as e:
        st.error(f"資料庫錯誤: {e}")
    finally:
        if "conn" in locals():
            conn.close()

#print(os.getenv("PASSWORD"))
"""