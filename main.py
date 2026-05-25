import streamlit as st
from few_shorts import FewShorts
from post_generator import generate_post

def main():
    st.title("LinkedIn Post Generator")
    clo1, clo2, col3 = st.columns(3)
    with clo1:
        length = st.selectbox("Select Length", ["Short", "Medium", "Long"])
    with clo2:
        language = st.selectbox("Select Language", ["English"])
    with col3:
        tag = st.selectbox("Select Tag", ["Book Promotion", "Self Improvement", "Digital Marketing", "Self Improvement","Authors", "Fiction", "Non-Fiction"])

    if st.button("Generate Post"):
        post = generate_post(length, language, tag)
        st.write(post)

if __name__ == "__main__": 
    main()