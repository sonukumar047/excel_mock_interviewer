🤖 AI-Powered Excel Mock Interviewer
Overview
This project is an AI-driven mock interviewer designed to assess a candidate's advanced Excel proficiency. The system simulates a multi-turn conversation, intelligently evaluates a user's answers, and generates a detailed performance report.

Key Features
Structured Interview Flow: Manages a coherent, multi-turn interview with dynamic questioning.

Intelligent Answer Evaluation: Evaluates user responses based on correctness, efficiency, and clarity.

Final Feedback Report: Generates a comprehensive summary of performance with actionable feedback.

Modular Architecture: Separates frontend and backend logic for scalability and maintainability.

Containerized Development: Uses Docker and Docker Compose for a consistent, isolated development environment.

Technologies
This project is built using a modern full-stack approach with a focus on containerization and API-driven communication.

Frontend:

HTML, CSS, JavaScript: Standard web technologies for building the user interface.

Tailwind CSS: A utility-first CSS framework for rapid styling.

Backend:

FastAPI: A modern, high-performance web framework for the backend API.

Python: The primary language for all backend logic.

Groq Cloud: Utilized for a high-speed LLM to power the AI interviewer.

Pydantic: Used for data validation and serialization.

Deployment & Environment:

Docker: Used to containerize the application.

Docker Compose: Orchestrates the multi-container application (frontend and backend).

Project Structure
The project is organized into a clean, modular structure to promote separation of concerns.

excel_mock_interviewer/
├── 📝 README.md
├── ⚙️ .env.example
├── 📄 requirements.txt
├── 🐳 Dockerfile
├── ⚙️ docker-compose.yml
│
├── 📁 backend/
│   ├── 🐍 __init__.py
│   ├── 🐍 main.py
│   │
│   ├── 📁 config/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 settings.py
│   │   └── 🐍 database.py
│   │
│   ├── 📁 agents/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 base_agent.py
│   │   ├── 🐍 interview_manager.py
│   │   ├── 🐍 question_generator.py
│   │   ├── 🐍 answer_evaluator.py
│   │   └── 🐍 feedback_generator.py
│   │
│   ├── 📁 models/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 interview_models.py
│   │   └── 🐍 evaluation_models.py
│   │
│   ├── 📁 services/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 groq_service.py
│   │   ├── 🐍 state_manager.py
│   │   └── 🐍 evaluation_service.py
│   │
│   ├── 📁 api/
│   │   ├── 🐍 __init__.py
│   │   └── 📁 routes/
│   │       ├── 🐍 __init__.py
│   │       ├── 🐍 interview.py
│   │       ├── 🐍 evaluation.py
│   │       └── 🐍 session.py
│   │
│   └── 📁 utils/
│       ├── 🐍 __init__.py
│       ├── 🐍 helpers.py
│       ├── 🐍 validators.py
│       └── 🐍 excel_knowledge.py
│
├── 📁 frontend/
│   ├── 🌐 index.html
│   │
│   ├── 📁 styles/
│   │   ├── 🎨 main.css
│   │   ├── 🎨 interview.css
│   │   └── 🎨 components.css
│   │
│   ├── 📁 scripts/
│   │   ├── 🟨 main.js
│   │   ├── 🟨 interview.js
│   │   ├── 🟨 api.js
│   │   └── 🟨 components.js
│   │
│   └── 📁 assets/
│       ├── 📁 images/
│       └── 📁 icons/
│
├── 📁 tests/
│   ├── 🐍 __init__.py
│   ├── 🐍 test_agents.py
│   ├── 🐍 test_api.py
│   └── 🐍 test_evaluation.py
│
└── 📁 docs/
    ├── 📝 api_documentation.md
    ├── 📝 architecture.md
    └── 📝 deployment.md

Getting Started
Follow these steps to get the project up and running locally using Docker Compose.

Prerequisites
Docker

Docker Compose

Step 1: Clone the Repository
git clone [https://github.com/your-username/excel_mock_interviewer.git](https://github.com/your-username/excel_mock_interviewer.git)
cd excel_mock_interviewer

Step 2: Configure Environment Variables
Create a new file named .env in the root of the project.

cp .env.example .env

Open the .env file and add your Groq Cloud API Key.

# Get your API key from [https://console.groq.com/keys](https://console.groq.com/keys)
GROQ_API_KEY="your_groq_api_key_here"

Step 3: Run the Application
Start both the backend and frontend services using Docker Compose.

docker-compose up --build

This command will:

Build the Docker images for the backend and frontend.

Start the FastAPI backend server (accessible at http://localhost:8000).

Start a development server for the frontend (accessible at http://localhost:3000).

Wait for the services to start. You will see INFO: Uvicorn running... in the logs, and the frontend will be served.

Step 4: Access the Application
Open your web browser and navigate to:

http://localhost:3000

You should now see the AI-powered Excel Mock Interviewer, and the frontend will communicate with the backend to start your interview.

API Documentation
For detailed information on the API endpoints, request/response schemas, and example calls, refer to the documentation at http://localhost:8000/docs or view the files in the docs/ directory.

Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
