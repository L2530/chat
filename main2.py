import streamlit as st

st.title('chatbot')
st.markdown("# >>>>>>>")
prompt = st.chat_input("Enter something:")


if "messages" not in st.session_state:
	st.session_state.messages = []


for message in st.session_state.messages:
	user_input = st.chat_message(message['role'])
	user_input.write(message['content'])


if prompt and prompt != '':
	st.chat_message("user").write(prompt)
	st.session_state.messages.append({'role:': 'user', 'content': prompt})

if prompt == 'hi':
	st.session_state.messages.append({'role': 'assistant', "content": "Hello"})
	st.chat_message("assistant").write('Hello')
elif prompt == 'good':
	st.session_state.messages.append({'role': 'assistant', "content": "Good to hear! "})
	st.chat_message("assistant").write('Good to hear!')
elif prompt == 'bad':
	st.chat_message("assistant").write('WHY!?!?')
	st.session_state.messages.append({'role': 'assistant', "content": "WHY!?!?"})
elif prompt == 'tae':
	st.chat_message("assistant").write('Delicious yum yum!')
	st.session_state.messages.append({'role': 'assistant', "content": "Delicious yum yum!"})
elif prompt == 'hello':
	st.chat_message("assistant").write('Hi!')
	st.session_state.messages.append({'role': 'assistant', "content": "Hi!"})
elif prompt == 'bye':
	st.chat_message("assistant").write('Bye!!')
	st.session_state.messages.append({'role': 'assistant', "content": "Bye!!"})
elif prompt == 'limuel':
	st.chat_message("assistant").write("May flowers for Therese")
	st.session_state.messages.append({'role': 'assistant', "content": "May flowers for Therese"})
elif prompt == 'do you know limuel':
	st.chat_message("assistant").write("Yes he loves Therese")
	st.session_state.messages.append({'role': 'assistant', "content": "Yes he loves Therese"})
else:
	st.chat_message("assistant").write('I do not understand')
	st.session_state.messages.append({'role': 'assistant', "content": "I do not understand"})

