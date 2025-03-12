# QnA Web App with Web and Video Crawling

This project is a QnA web application that allows users to ask questions based on the content of a web page or a YouTube video. The application extracts text from the provided URL or YouTube video, processes it using an AI model, and generates answers to the user's questions.

## Features

- Extract text from a web page URL
- Extract text from a YouTube video
- Generate answers to user questions based on the extracted text
- Display the conversation history

## Technologies Used

- Streamlit: For building the web application
- BeautifulSoup: For web scraping
- YouTubeTranscriptApi: For extracting transcripts from YouTube videos
- Langchain_groq: For interacting with the AI model
- Azure OpenAI: For processing the text and generating answers
- asyncio and aiohttp: For asynchronous operations

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/qna-web-app.git
    cd qna-web-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add the following variables:
    ```plaintext
    ENDPOINT_URL=your_azure_openai_endpoint
    DEPLOYMENT_NAME=your_azure_openai_deployment_name
    AZURE_OPENAI_API_KEY=your_azure_openai_api_key
    AZURE_OPENAI_VERSION=your_azure_openai_version
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Select the input type ("Web URL" or "YouTube Video").

4. Enter the URL or YouTube video URL and your question.

5. Click the "Get Answer" button to generate an answer based on the extracted text.

## File Structure

- `app.py`: The main application file that contains the Streamlit code and handles user interactions.
- `transcript_analysis.py`: Contains functions for interacting with the Azure OpenAI model and processing the transcript.
- `video_processing.py`: Contains functions for processing video files and extracting transcripts.
- `requirements.txt`: Lists the required Python packages for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [YouTubeTranscriptApi](https://github.com/jdepoix/youtube-transcript-api)
- [Langchain_groq](https://github.com/langchain/langchain)
- [Azure OpenAI](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/)
