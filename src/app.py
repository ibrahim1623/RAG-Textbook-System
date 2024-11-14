import streamlit as st
from openai import OpenAI
import yaml

st.write(" # RAAGGGGG!")

# get API KEY
with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
    API_KEY = config['OPENAI_API_KEY']

# init client
client = OpenAI(api_key=API_KEY)

# set model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

#chat history init
if "messages" not in st.session_state:
    #create a list for messages
    st.session_state.messages = []

# display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# assign input to prompt AND check if its not NONE
if prompt := st.chat_input("Ask a question for STAT 305"):
    # display message
    with st.chat_message("user"):
        st.markdown(prompt)
    # add message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # get the response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Create the stream
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            
            # Process the stream
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
            # Add the full response to message history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")