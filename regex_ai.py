import openai
import streamlit as st

openai.api_key = "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"
starting_messages = [
    {
        "role": "system",
        "content": (
            "You're a kind helpful assistant that writes Python RegEx given a"
            " description of what the user wants."
        ),
    },
    {
        "role": "user",
        "content": (
            "Write a Python RegEx which does what I want. First give the RegEx"
            " string, then explain how it works step by step, in no more than"
            " 5 bullet points. Then provide a short and simple Python example"
            " of using the RegEx. Then show one example input and output. Make"
            " the code simple and efficient. Start your reply with 'Regex:'"
            " and do not repeat yourself in your explanation. Be concise."
            " Reply in markdown."
        ),
    },
]

st.title("ReGex AI")


def converse(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    response = completion.choices[0].message.content
    return {"role": "assistant", "content": response}


starting_messages.append(converse(starting_messages))


message = st.text_input(label="Ask the helpful assistant something...")
if st.button(label="Send"):
    messages = starting_messages
    messages.append({"role": "user", "content": message})
    messages.append(converse(messages))

    st.markdown(messages[-1]["content"])
