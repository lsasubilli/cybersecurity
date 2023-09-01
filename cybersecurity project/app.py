import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    st.title("Chat with GPT-3")
    st.write("Enter a prompt to chat with the AI:")

    user_input = st.text_input("You:", value="", max_chars=200)
    
    if st.button("Send"):
        st.text("AI:")
        response = chat_with_gpt(user_input)
        st.write(response)

if __name__ == "__main__":
    main()
