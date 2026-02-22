# Ollama Models Indexer & Summarizer

A sleek, locally-hosted web application that allows you to search the official [Ollama Library](https://ollama.com/library) and generate deep, AI-powered architectural summaries of the models using your local `gpt-oss:20b` deployment.

## ✨ Features
- **Live Library Search**: Scrapes and searches the live Ollama model library directly from `ollama.com`.
- **AI-Powered Insights**: Select any model to generate a comprehensive, highly detailed markdown summary of its use cases, strengths, and architecture using `gpt-oss:20b`.
- **Premium UI**: Built with a gorgeous, responsive, glassmorphic dark-mode interface using pure HTML, CSS, and JS (No heavy frontend frameworks required).

## 🚀 Prerequisites

Before you begin, ensure you have the following installed:
1. [Python 3.8+](https://www.python.org/downloads/)
2. [Ollama](https://ollama.com/)
3. The `gpt-oss:20b` model pulled locally in Ollama:
   ```bash
   ollama pull gpt-oss:20b
   ```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ollama-models-index.git
   cd ollama-models-index
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Start the Flask backend server:**
   ```bash
   python app.py
   ```
   *(Note: The server runs on port 5001 by default to avoid conflicts with common services on port 5000).*

2. **Open the App:**
   Navigate to `http://localhost:5001` in your web browser.

3. **Explore Models:**
   - Type a model name (e.g., `mistral`, `llama3.1`) in the search bar.
   - Click on any model card to trigger the AI summary generation.
   - Wait a few moments as `gpt-oss:20b` processes the request and streams back the markdown evaluation.

## 📁 Project Structure

```
ollama-models-index/
├── app.py                  # Core Flask backend and scraping logic
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Vanilla HTML/CSS/JS frontend
└── .gitignore              # Standard Python gitignore
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/ollama-models-index/issues).

## 📝 License
This project is [MIT](https://opensource.org/licenses/MIT) licensed.
