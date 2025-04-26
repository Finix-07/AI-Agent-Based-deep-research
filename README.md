# AI Agent-Based-deep-research
Exploring Travily

# Deep Research AI Agentic System

## Overview
The **Deep Research AI Agentic System** is an advanced AI-powered framework designed to perform comprehensive online research and generate structured answers. It leverages the **Tavily API** for web crawling and information gathering, and employs a **dual-agent system** to streamline the research and drafting processes. The system is built using the **LangGraph** and **LangChain** frameworks to efficiently organize and process the gathered information.

## Features
- **Dual-Agent Architecture**:
  - **Research Agent**: Focuses on crawling websites and collecting relevant data using the Tavily API.
  - **Drafting Agent**: Processes the collected data and generates structured, markdown-formatted answers.
- **LangGraph Integration**: Orchestrates the flow of tasks between agents using a state graph.
- **LangChain Framework**: Provides tools for prompt engineering and seamless integration with LLMs.
- **Retry Mechanism**: Implements exponential backoff for handling errors during API calls.
- **Customizable Parameters**: Allows configuration of model parameters such as temperature, max length, and retries.

## System Workflow
1. **Input Query**: The user submits a research query through the frontend interface.
2. **Research Agent**: The query is processed by the Research Agent, which uses the Tavily API to gather relevant information from the web.
3. **Drafting Agent**: The collected data is passed to the Drafting Agent, which generates a structured response in markdown format.
4. **Output**: The final answer is displayed in the frontend's "Research Findings" panel.

## Technologies Used
- **Frontend**:
  - React with TypeScript
  - Tailwind CSS for styling
  - Marked.js for rendering markdown
- **Backend**:
  - FastAPI for API endpoints
  - LangGraph for task orchestration
  - LangChain for LLM integration
  - Tavily API for web crawling
- **Other Tools**:
  - dotenv for environment variable management
  - React Query for state management
  - Lucide React for icons

## Installation

### Prerequisites
- Node.js and npm installed
- Python 3.9+ installed
- Tavily API key (add it to a `.env` file)
- [Ollama](https://ollama.ai/) installed for running `llama3.2`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Deep-Research-AI.git
   cd Deep-Research-AI
   ```

2. Run `llama3.2` on Ollama:
   Ensure that Ollama is installed and running. Start the `llama3.2` model:
   ```bash
   ollama serve --model llama3.2
   ```

3. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

5. Add your `.env` file in the `backend` directory:
   ```
   TAVILY_API_KEY=your_tavily_api_key
   ```

6. Start the backend:
   ```bash
   cd backend
   uvicorn api:app --reload
   ```

7. Start the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

## Usage
1. Open the frontend in your browser (default: `http://localhost:3000`).
2. Enter your research query in the "Your Question" panel.
3. View the structured response in the "Research Findings" panel.

## Project Structure
```
Deep-Research-AI/
├── backend/
│   ├── agents/
│   │   ├── research_agent.py
│   │   ├── drafter_agent.py
│   │   └── __init__.py
│   ├── api.py
│   ├── worker_main.py
│   ├── travily.py
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AnswerPanel.tsx
│   │   │   ├── QuestionPanel.tsx
│   │   └── pages/
│   │       ├── Index.tsx
│   ├── index.html
│   ├── tailwind.config.ts
│   └── package.json
└── README.md
```

## License
This project is licensed under the [MIT License](LICENSE).

## Future Enhancements
- Add support for additional models to handle more context and better workflows.
- Enhance the frontend UI for better user experience.
- Integrate more APIs for faster and diverse data sources collection.

## Acknowledgments
- **Tavily API** for enabling efficient web crawling.
- **LangGraph** and **LangChain** for providing robust frameworks for task orchestration and LLM integration.