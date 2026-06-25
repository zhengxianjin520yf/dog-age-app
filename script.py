import streamlit as st

st.title("🐶 狗狗年龄换算器")

age = st.number_input("请输入你家狗狗的年龄（岁）", min_value=0, step=1, format="%d")

if age <= 0:
    st.warning("你是在逗我吧! 请输入一个正数。")
elif age == 1:
    st.success("相当于 14 岁的羿芬。")
elif age == 2:
    st.success("相当于 22 岁的羿芬。")
else:
    human = 22 + (age - 2) * 5
    st.success(f"对应羿芬年龄: {human} 岁")