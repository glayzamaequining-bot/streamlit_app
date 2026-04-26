import streamlit as st

st.title("🏠 Home")

st.header("Hello, I'm Glaiza Mae Q. Distura 👋")

st.write("Computer Science Student | Future Web Developer")

st.image("assets/pic1.jpeg", caption="Portfolio Profile Picture", width=300)

st.info("Explore my portfolio to learn about my skills and projects.")

# INTERACTIVE BUTTON
if st.button("Show a Fun Fact"):
    st.success("I enjoy learning programming and building simple web apps!")
