# 📄 RAG AI Assistant (Retrieval-Augmented Generation)

An intelligent, interactive company chatbot built with **Streamlit** that allows users to upload confidential PDF documents (like HR Manuals, Standard Operating Procedures, or Technical Specs) and chat directly with them.

## Business Value 💼
Generic AI models (like ChatGPT) hallucinate and do not know your company's proprietary data. This **RAG (Retrieval-Augmented Generation)** system ensures the AI **only** answers based on the uploaded documents. 
- **Zero Hallucination:** Answers are strictly grounded in retrieved semantic context.
- **Privacy First:** Uses a local vector database (`ChromaDB`) to store document embeddings. No sensitive documents are exposed to public training data.
- **Cost Effective:** Built with open-source and free-tier infrastructure.

## Tech Stack 🚀
- **Frontend**: `Streamlit` for a beautiful, instant, and interactive web application.
- **Vector Database**: `ChromaDB` for high-performance, local semantic search and embedding storage.
- **LLM Engine**: `Google Gemini API` (`gemini-2.5-flash` and `text-embedding-004`) for fast inference and semantic vector generation.
- **Data Pipeline**: `pdfplumber` for clean and robust document parsing.

## How to Run 🛠️

1. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/rag-chatbot-portfolio.git
cd rag-chatbot-portfolio
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Set your Gemini API Key in the `.env` file:
```env
GEMINI_API_KEY=your_google_ai_studio_api_key_here
```

4. Launch the Streamlit Web Application:
```bash
streamlit run app.py
```

## Preview
Upload any PDF document via the sidebar, click "Process Document", and instantly start querying the information using natural language!
