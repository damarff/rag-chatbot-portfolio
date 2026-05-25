import os
import chromadb
import pdfplumber
from google import genai
from dotenv import load_dotenv

load_dotenv()

class RAGSystem:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")
        
        # Initialize Google GenAI client
        self.client = genai.Client(api_key=self.api_key)
        
        # Initialize ChromaDB locally in the 'chroma_db' folder
        self.chroma_client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.chroma_client.get_or_create_collection(name="documents")
        
    def generate_embedding(self, text: str) -> list[float]:
        """Converts text into a vector of numbers (embeddings) using Gemini."""
        response = self.client.models.embed_content(
            model='gemini-embedding-001',
            contents=text,
        )
        return response.embeddings[0].values
        
    def process_pdf(self, pdf_path: str, doc_id: str):
        """Reads PDF, chunks the text, and saves embeddings into ChromaDB."""
        full_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    full_text += extracted + "\n"
                    
        # Simple chunking: split by double newlines (paragraphs)
        chunks = [c.strip() for c in full_text.split('\n\n') if len(c.strip()) > 50]
        
        if not chunks:
            raise ValueError("No readable text found in PDF.")
            
        print(f"[*] Processing {len(chunks)} chunks into ChromaDB...")
        for i, chunk in enumerate(chunks):
            embedding = self.generate_embedding(chunk)
            chunk_id = f"{doc_id}_chunk_{i}"
            
            # Upsert into ChromaDB
            self.collection.add(
                ids=[chunk_id],
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"source": doc_id}]
            )
        print("[+] Document successfully embedded!")

    def query(self, user_question: str) -> str:
        """Retrieves relevant context from DB and asks Gemini to answer."""
        # 1. Embed the user's query
        query_embedding = self.generate_embedding(user_question)
        
        # 2. Retrieve top 3 most relevant text chunks from the DB
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )
        
        retrieved_docs = results['documents'][0] if results['documents'] else []
        context = "\n\n---\n\n".join(retrieved_docs)
        
        if not context:
            return "Maaf, saya tidak menemukan informasi terkait di dalam dokumen yang telah diunggah."
            
        # 3. Prompt the LLM strictly based on context
        prompt = f"""
        You are an intelligent internal company assistant. 
        Answer the user's question ONLY based on the provided CONTEXT. 
        If the answer is not in the context, strictly say "Saya tidak tahu berdasarkan dokumen yang ada."
        Do not use external knowledge. Answer in Indonesian language.

        CONTEXT:
        {context}

        QUESTION:
        {user_question}
        """
        
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        return response.text
