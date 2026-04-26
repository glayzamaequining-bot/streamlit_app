import streamlit as st

st.title("📬 Contact Me")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill in all fields.")

st.markdown("### Social Links")

st.write("- GitHub: https://github.com/glayzamaequining-bot")
st.write("- Facebook: https://facebook.com/Glaiza-Mae-Distura")
