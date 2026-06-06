import streamlit as st
import tempfile

from few_shorts import FewShorts
from post_generator import generate_post
from preprocess import process_posts


def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="✍️"
    )

    st.title("✍️ LinkedIn Post Generator")

    uploaded_file = st.file_uploader(
        "Upload LinkedIn Dataset JSON",
        type=["json"]
    )

    if uploaded_file is None:
        st.info("Please upload a LinkedIn dataset JSON file.")
        return

    # Process dataset only once
    if st.button("Process Dataset"):

        try:
            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".json"
            )

            temp_file.write(uploaded_file.getvalue())
            temp_file.close()

            processed_path = "temp_processed.json"

            with st.spinner("Processing uploaded posts..."):

                process_posts(
                    temp_file.name,
                    processed_path
                )

                st.session_state.few_shorts = FewShorts(
                    processed_path
                )

            st.success("Dataset processed successfully!")

        except Exception as e:
            st.error(f"Error while processing dataset: {str(e)}")
            return

    # Stop here until dataset is processed
    if "few_shorts" not in st.session_state:
        st.warning("Click 'Process Dataset' first.")
        return

    few_shorts = st.session_state.few_shorts

    tags = sorted(
        list(few_shorts.get_unique_tags())
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        length = st.selectbox(
            "Select Length",
            ["Short", "Medium", "Long"]
        )

    with col2:
        language = st.selectbox(
            "Select Language",
            ["English", "Hinglish"]
        )

    with col3:
        tag = st.selectbox(
            "Select Tag",
            tags
        )

    if st.button("Generate Post"):

        try:
            with st.spinner("Generating LinkedIn post..."):

                post = generate_post(
                    length,
                    language,
                    tag,
                    few_shorts
                )

            st.success("Post Generated Successfully!")

            st.text_area(
                "Generated Post",
                value=post,
                height=400
            )

        except Exception as e:
            st.error(f"Error generating post: {str(e)}")


if __name__ == "__main__":
    main()