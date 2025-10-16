# 🧠 InsightBrain - AI Research Summarizer

An intelligent research assistant that performs web searches, generates multi-step reasoning summaries, performs fact-consistency checks, and exports comprehensive research reports as PDFs.

## ✨ Features

- **Quick Research Mode**: Fetches top 3 sources for rapid insights
- **Deep Research Mode**: Analyzes 20+ sources for comprehensive analysis
- **Multi-Step Reasoning**: AI-powered logical analysis of research topics
- **Fact Consistency Check**: Cross-validates information across multiple sources
- **Follow-up Questions**: Generates relevant questions for deeper exploration
- **PDF Export**: Download professional research reports
- **Interactive UI**: Clean Streamlit interface with source citations

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI Model**: Groq (OpenAI GPT-OSS-20B)
- **Web Search**: Tavily Search API
- **PDF Generation**: ReportLab
- **Language Chain**: LangChain

## 📋 Prerequisites

- Python 3.8+
- Tavily API Key
- Groq API Key

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd insightbrain
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit fastapi uvicorn requests python-dotenv
pip install langchain-community langchain-groq tavily-python
pip install reportlab pydantic
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

**Getting API Keys:**
- **Tavily API**: Sign up at [https://tavily.com](https://tavily.com)
- **Groq API**: Get your key at [https://console.groq.com](https://console.groq.com)

## 📁 Project Structure

```
insightbrain/
│
├── app.py              # Streamlit frontend
├── main.py             # FastAPI backend
├── .env                # Environment variables (create this)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🎯 Usage

### Start the Backend Server

Open a terminal and run:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The backend will be available at `http://127.0.0.1:8000`

### Start the Frontend

Open a **new terminal** and run:

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Using the Application

1. **Select Research Mode**: Choose between Quick Research (3 sources) or Deep Research (20 sources)
2. **Enter Query**: Type your research topic in the search bar
3. **Generate Summary**: Click the "🔍 Generate Summary" button
4. **Review Results**: 
   - View cited sources
   - Read the reasoning summary
   - Check fact consistency analysis
   - Explore follow-up questions
5. **Download Report**: Click the download link to get your PDF report

## 📊 API Endpoints

### POST `/research`
Quick research with 3 sources

**Request Body:**
```json
{
  "query": "Impact of AI on healthcare",
  "history": []
}
```

### POST `/deep_research`
Deep research with 20 sources

**Request Body:**
```json
{
  "query": "Impact of AI on healthcare",
  "history": []
}
```

### POST `/generate_pdf`
Generate PDF report

**Request Body:**
```json
{
  "query": "Impact of AI on healthcare",
  "report_md": "# Research Report..."
}
```

### GET `/health`
Health check endpoint

## 🔧 Configuration

### Change Backend URL

If deploying backend remotely, update `FASTAPI_URL` in `app.py`:

```python
FASTAPI_URL = "https://your-backend-url.com"
```

### Adjust Number of Sources

In `main.py`, modify the `k` parameter in endpoints:

```python
# Quick research
sources = fetch_top_sources(req.query, 3)  # Change 3 to desired number

# Deep research
sources = fetch_top_sources(req.query, 20)  # Change 20 to desired number
```

## 🐛 Troubleshooting

### Backend Connection Error
- Ensure backend is running on `http://127.0.0.1:8000`
- Check firewall settings
- Verify CORS configuration

### API Key Errors
- Confirm `.env` file exists in project root
- Verify API keys are valid and active
- Check API key quotas/limits

### PDF Generation Issues
- Ensure ReportLab is installed correctly
- Check file permissions for PDF creation

## 📝 Example Queries

- "Impact of AI on healthcare"
- "Climate change effects on agriculture"
- "Latest developments in quantum computing"
- "Renewable energy adoption trends"
- "Machine learning in financial markets"

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Tavily for web search capabilities
- Groq for AI inference
- LangChain for AI orchestration
- Streamlit for the frontend framework

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: your-email@example.com

---

**Made with ❤️ using AI and open-source tools**
