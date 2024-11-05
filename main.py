import streamlit
from langchain_ollama import OllamaLLM
import time

# App title
streamlit.set_page_config(page_title="Ollama Assistant")
with streamlit.sidebar:streamlit.title("Ollama Assistant")

llm = OllamaLLM(model="pacha")

# Store llm generated messages.
if "messages" not in streamlit.session_state.keys():
  streamlit.session_state.messages = [{"role": "assistant", "content": "How can i help you?"}]

# Display the messages stored in streamlit messages session.
for message in streamlit.session_state.messages:
  with streamlit.chat_message(message["role"]):
    streamlit.write(message["content"])

# Reset the messages session to null.
def clear_chat_history():
  streamlit.session_state.messages = [{"role": "assistant", "content": "How can i help you?"}]

# Add clear button.
streamlit.sidebar.button("Clear chat history", on_click=clear_chat_history)

def generate_llm_response(prompt):
  response = llm.invoke(input=prompt)

  return response

# Check if the user has entered any input and if yes, assign it to prompt.
if prompt := streamlit.chat_input():
    streamlit.session_state.messages.append({"role": "user", "content": prompt})
    with streamlit.chat_message("user"):
        streamlit.write(prompt)

if streamlit.session_state.messages[-1]["role"] != "assistant":
   with streamlit.chat_message("assistant"):
      response = generate_llm_response(prompt)
      # to show generating of response, char by char.
      placeholder = streamlit.empty()
      bot_response = ""
      for char in response:
        bot_response += char
        placeholder.markdown(bot_response)
        time.sleep(0.02) # to give writing feeling. Adjust as needed.
      message = {"role": "user", "content": bot_response}
      streamlit.session_state.messages.append(message)