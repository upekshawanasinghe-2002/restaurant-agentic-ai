#  AI Restaurant Recommendation & Dining Planner

An intelligent restaurant recommendation and dining planning system for Sri Lankan tourists using Agentic AI, Retrieval-Augmented Generation (RAG), LangChain, ChromaDB, Groq LLM and Streamlit.


# Project Description

This project helps tourists and local users discover restaurants based on their preferred cuisine, destination, budget and dining preferences.

The system uses multiple AI agents that collaborate to understand user requirements, retrieve restaurant information from a vector database, analyse reviews and generate a personalized dining plan.

# Features

-  Multi-Agent AI Architecture
- Retrieval-Augmented Generation (RAG)
- Personalized Restaurant Recommendations
- Restaurant Review Analysis
- Budget-aware Suggestions
- Location-based Search
- Dining Planning
- Groq LLM Integration
- Streamlit Web Application


# System Architecture
The following sequence diagram illustrates how the AI agents collaborate to process a user's request. The Router Agent delegates tasks to specialized agents, which exchange structured messages. The Restaurant Search Agent retrieves domain knowledge from the RAG knowledge base before the Planner Agent generates the final dining itinerary.

sequenceDiagram
    autonumber
    actor Tourist as User / Streamlit
    participant Router as Router Agent
    participant Pref as Preference Agent
    participant Search as Restaurant Search Agent
    participant VectorDB as ChromaDB / FAISS
    participant Planner as Planner Agent
    participant Review as Review Agent

    Tourist->>Router: Enter dining preferences & trip details
    Router->>Pref: Extract user preferences
    Pref-->>Router: Structured preference profile

    Router->>Search: Search suitable restaurants
    Search->>VectorDB: Retrieve restaurant menus & reviews
    VectorDB-->>Search: Relevant restaurant documents

    Search->>Planner: Recommended restaurant list
    Planner-->>Planner: Create optimized dining itinerary

    Planner->>Review: Summarize customer reviews
    Review-->>Planner: Review summary

    Planner->>Tourist: Final restaurant recommendations & trip dining plan


# Agent Communication Diagram

sequenceDiagram

    participant U as User

    participant UI as Streamlit UI

    participant R as Router Agent

    participant P as Preference Agent

    participant S as Restaurant Agent

    participant V as Vector DB

    participant Rev as Review Agent

    participant Pl as Planner Agent

    participant L as Groq LLM

    U->>UI: Enter dining preferences

    UI->>R: User Query

    R->>P: Extract preferences

    P-->>R: Food, Budget, Location

    R->>S: Search restaurants

    S->>V: Similarity Search

    V-->>S: Restaurant Documents

    S-->>R: Restaurant Results

    R->>Rev: Analyze Reviews

    Rev-->>R: Review Summary

    R->>Pl: Create Dining Plan

    Pl->>L: Generate Recommendation

    L-->>Pl: Final Response

    Pl-->>UI: Personalized Dining Plan

    UI-->>U: Display Recommendation



# RAG Workflow

flowchart LR

    A[Restaurant PDFs / Reviews]

    --> B[Document Loader]

    --> C[Text Splitter]

    --> D[Sentence Embeddings]

    --> E[(ChromaDB)]

    F[User Query]

    --> G[Retriever]

    G --> E

    E --> H[Relevant Chunks]

    H --> I[Groq LLM]

    I --> J[Final Restaurant Recommendation]



# Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- Groq
- Sentence Transformers
- Agentic AI



# Folder Structure

restaurant-agentic-ai
│
├── agents                      # Multi-Agent AI components
│   ├── planner_agent.py
│   ├── preference_agent.py
│   ├── restaurant_agent.py
│   ├── review_agent.py
│   └── router_agent.py
│
├── chroma_db                   # ChromaDB vector database
│
├── data                        # Restaurant datasets and documents
│   ├── cusine
│   ├── menus
│   ├── restaurants
│   ├── reviews
│   └── tourism
│
├── rag                         # RAG pipeline components
│   ├── embeddings.py
│   ├── ingest.py
│   ├── loader.py
│   ├── retriver.py
│   └── splitter.py
│   └── vector_store.py
│
├── streamlit_app
│   └── app.py                   # Streamlit user interface
│
├── tests                       # Unit tests
│
├── utils                      # Utility functions
│
├── .env                         # Environment variables (not committed)
├── .gitignore                   # Git ignore rules
├── app.py                       # Main application entry point
├── config.py                    # Project configuration
├── llm_factory.py               # LLM initialization
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies

# Installation

Clone the repository
git clone https://github.com/upekshawanasinghe-2002/restaurant-agentic-ai.git

cd restaurant-agentic-ai

Install dependencies
pip install -r requirements.txt


Run the application
python -m streamlit run streamlit_app/app.py


# Model Comparison

|         Model               |           Purpose                   |             Reason for Selection                     |
| Groq Llama 3                |    Response Generation              | Fast inference with good reasoning quality           |
| ChromaDB                    |    Vector Database                  | Efficient semantic document retrieval                |
| Sentence Transformers       |    Embedding Model                  | Converts restaurant documents into vector embeddings |
| LangChain                   |    AI Orchestration                 | Connects agents, retrieval, and LLM workflow         |





# GitHub Repository

https://github.com/upekshawanasinghe-2002/restaurant-agentic-ai



# Evaluation

The system was evaluated using several restaurant search queries with different cuisine preferences, locations and budget constraints.

Evaluation focused on:

- Preference extraction accuracy
- Restaurant retrieval relevance
- Response quality
- Recommendation consistency
- End-to-end execution


# Limitations

- Depends on the quality and coverage of the restaurant dataset.
- Recommendations are limited to indexed restaurants.
- User reviews may become outdated over time.
- Budget estimates may not reflect real-time menu prices.
- Does not currently integrate live restaurant APIs or real-time availability.


# Future Improvements

- Google Maps API Integration
- Live Restaurant Booking
- GPS-based Recommendations
- Multilingual Support
- Voice-based Search
- Real-time Restaurant Availability


# Author

Upeksha Sandamali
BSc (Hons) in Information Technology
Horizon Campus

 

# License

This project was developed for academic purposes.