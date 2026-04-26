import streamlit as st

st.title("🛠 Skills")

st.subheader("Programming")

python_level = st.slider("Python Skill Level", 0, 100, 70)
html_level = st.slider("HTML Skill Level", 0, 100, 75)
css_level = st.slider("CSS Skill Level", 0, 100, 65)

st.write("Python")
st.progress(python_level)

st.write("HTML")
st.progress(html_level)

st.write("CSS")
st.progress(css_level)

st.subheader("Tools")
st.write("- Visual Studio Code")
st.write("- GitHub")
st.write("- Streamlit")


st.title("📂 My Projects")

project = st.selectbox(
    "Choose a project to view:",
    [
        "Calculator Application",
        "Personal Portfolio"
    ]
)


if project == "Calculator Application":
    st.write("A program that performs basic mathematical calculations.")

elif project == "Personal Portfolio":
    st.write("A website that displays my skills, projects, and profile.")

if st.button("Show Personal Goals"):
    st.success("My goal is to do well in my studies, graduate successfully, and make my family proud.")

