from llm_helper import llm
from few_shorts import FewShorts

few_shorts = FewShorts()


def get_length(length):
    if length == "Short":
        return "8 to 9 lines"
    elif length == "Medium":
        return "15 to 16 lines"
    elif length == "Long":
        return "20 to 30 lines"

    return "10 to 15 lines"


def get_prompt(length, language, tag):

    length_str = get_length(length)

    prompt = f"""
Generate a LinkedIn post with the following requirements. No preamble.

1. Language: {language}
2. Length: {length_str}
3. Tag: {tag}
4. The post should be engaging.
5. The post should be LinkedIn-friendly.
6. The post should be original and not copied from anywhere else.
7. The post should be divided into 2 - 3 paragraphs and there should be one-line space before starting each paragraph.
8. There should be one-line space before hashtags.
9. Use 1 to 2 emojis in the post and place them appropriately in the post.
9. 1 emoji can be used in the beginning of the post.
"""

    examples = few_shorts.get_filtered_posts(
        length,
        language,
        tag
    )

    if len(examples) > 0:

        prompt += "\nHere are similar examples:\n"

        for i, post in enumerate(examples[:3]):
            prompt += f"\nExample {i+1}:\n{post['text']}\n"

    return prompt


def generate_post(length, language, tag):

    prompt = get_prompt(length, language, tag)

    print(prompt)   # debugging

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    post = generate_post("Medium", "English", "Fiction")
    print(post)