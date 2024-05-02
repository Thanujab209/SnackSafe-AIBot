import streamlit as st
import google.generativeai as genai

st.title("SnackSafe: Your Kid's Health Guardian")
st.subheader("Empowering Parents with Ingredient Safety Checks 🎉 Welcome to SnackSafe, your ultimate companion in ensuring your child's snack time is both delicious and safe! 🍎🥨. With this app, you can effortlessly input your kid's snack or chocolate ingredients and receive instant analysis on their safety. From allergens to additives, this'll provide clear explanations on why certain snacks are suitable or not for your little ones. 💡 Empower yourself with knowledge about what goes into your child's treats, and make informed choices for their health and happiness. Say goodbye to uncertainty and hello to confident snacking with SnackSafe! 🚀👨‍👩‍👧‍👦")

#Read the API Key

f = open("D:\Innomatics\search_engine\work_0\google_api_key.txt")

key=f.read()

#Configure the API Key

genai.configure(api_key=key)

#Init a gemini model
model = genai.GenerativeModel (model_name="gemini-1.5-pro-latest",
                               system_instruction="""You are a Helpful AI Bot. 
    You take the ingredients/contents list of a food item from the user and check whether
      it is safe for kids or not. Give explanation to users why it is safe or not safe for kids. """)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#Init the chat object

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.balloons()
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history