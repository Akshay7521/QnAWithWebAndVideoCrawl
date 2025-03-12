import streamlit as st
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from langchain_groq import ChatGroq
import asyncio
import aiohttp

# Initialize the ChatGroq model
llm = ChatGroq(
    temperature=0,
    api_key='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',
    model_name='llama3-8b-8192'
)

async def invoke_genai_model(prompt):
    response = llm.invoke(prompt)
    return response.content

async def chunk_text(text, max_length=1000):
    words = text.split()
    for i in range(0, len(words), max_length):
        yield ' '.join(words[i:i + max_length])

async def extract_text_from_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                soup = BeautifulSoup(await response.text(), 'html.parser')
                extracted_text = ' '.join([p.text for p in soup.find_all('p')])
                return extracted_text
    except aiohttp.ClientError as e:
        st.error(f"Error fetching the URL: {e}")
        return ""

async def extract_text_from_youtube(video_id):
    try:
        transcript = await asyncio.to_thread(YouTubeTranscriptApi.get_transcript, video_id)
        extracted_text = ' '.join([t['text'] for t in transcript])
        return extracted_text
    except (NoTranscriptFound, TranscriptsDisabled) as e:
        st.error(f"Error fetching the YouTube transcript: {e}")
        return ""

async def main():
    st.title("QnA Web App with Web and Video Crawling")
    
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    option = st.selectbox("Choose input type", ("Web URL", "YouTube Video"))
    question = st.text_input("Enter your question")
    
    if option == "Web URL":
        url = st.text_input("Enter the URL")
        if st.button("Get Answer"):
            if url and question:
                with st.spinner("Extracting text from URL..."):
                    text = await extract_text_from_url(url)
                if text:
                    prompt = ""+{question}+ {text}
                    with st.spinner("Generating answer..."):
                        answer = await invoke_genai_model(prompt)
                        st.write(answer)
                    st.session_state.conversation.append((question, answer))
                    for q, a in st.session_state.conversation:
                        st.write(f"Q: {q}")
                        st.write(f"A: {a}")
    
    elif option == "YouTube Video":
        video_url = st.text_input("Enter the YouTube Video URL")
        if st.button("Get Answer"):
            if video_url and question:
                video_id = video_url.split('v=')[-1]
                with st.spinner("Extracting text from YouTube video..."):
                    text = await extract_text_from_youtube(video_id)
                if text:
                    prompt = f"Human: {question}\nAssistant: {text}"
                    with st.spinner("Generating answer..."):
                        answer = await invoke_genai_model(prompt)
                        st.write(answer)
                    st.session_state.conversation.append((question, answer))
                    for q, a in st.session_state.conversation:
                        st.write(f"Q: {q}")
                        st.write(f"A: {a}")

if __name__ == "__main__":
    asyncio.run(main())
