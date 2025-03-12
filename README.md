# QnA Web App with Web and Video Crawling

This is a Streamlit-based web application that allows users to ask questions based on the content extracted from web pages or YouTube videos. The app uses the `langchain_groq` library to generate answers using a language model.

## Features

- Extract text from a given web URL.
- Extract text from YouTube video transcripts.
- Generate answers to user questions based on the extracted text.
- Maintain a conversation history.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/akshay7521/QnAWithWebAndVideoCrawling.git
    cd QnAWithWebAndVideoCrawling
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Select the input type ("Web URL" or "YouTube Video").

4. Enter your question and the URL or YouTube video URL.

5. Click the "Get Answer" button to generate an answer based on the extracted text.

## Dependencies

- `streamlit`
- `requests`
- `beautifulsoup4`
- `youtube_transcript_api`
- `langchain_groq`
- `asyncio`
- `aiohttp`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Langchain Groq](https://github.com/langchain/langchain_groq)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact [akshaykshirsagar2514@gmail.com](mailto:akshaykshirsagar2514@gmail.com).
