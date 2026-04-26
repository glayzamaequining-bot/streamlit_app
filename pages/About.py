import streamlit as st

st.title("👩‍💻 About Me")

st.write("""
I am a Computer Science student who enjoys learning programming
and building simple applications.
""")

st.subheader("🎓 Education")

education = st.selectbox(
    "Select information to view:",
    ["Education", "Goals"]
)

if education == "Education":
    st.write("Bachelor of Science in Computer Science 3C")
    st.write("College of Computing and Information Technology at DEBESMSCAT")
    st.write("3rd Year Student")

elif education == "Goals":
    st.write("Improve programming skills")
    st.write("Develop useful systems")
    st.write("Become a professional developer")
