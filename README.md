# 🤖 AI-Powered Excel Mock Interviewer

An intelligent conversational AI system that conducts mock interviews to assess Excel proficiency using Groq's lightning-fast Language Processing Unit (LPU) Inference Engine.

![Project Demo](https://place-holder.com/800x400) <!-- Replace with an actual GIF or image of your project -->

---

## 🎯 Core Features

-   **Multi-Agent Architecture**: Specialized agents for interview management, question generation, answer evaluation, and feedback generation.
-   **Lightning-Fast Responses**: Powered by Groq, providing a seamless, real-time conversational experience with sub-second latency.
-   **In-Depth Excel Knowledge**: Covers a wide range of Excel topics from basic formulas to advanced VBA and Power Query.
-   **Real-Time Evaluation**: Instantly scores technical accuracy, clarity, and completeness of answers.
-   **Persistent State Management**: Uses Redis to maintain conversation context, allowing interviews to be paused and resumed.
-   **Cost-Effective**: Built to run efficiently on Groq's generous free tier, making it ideal for development and scaling.

---

## 🏗️ System Architecture

The project uses a modern, decoupled architecture for scalability and maintainability.


git clone https://github.com/sonukumar047/excel-mock-interviewer.git
cd excel-mock-interviewer


### 2. Set Up Environment Variables

Create a `.env` file by copying the example file.


Now, open the `.env` file and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here


### 3. Install Dependencies

Install the required Python packages.

pip install -r requirements.txt


### 4. Run the Application with Docker Compose

This is the recommended method as it handles both the FastAPI application and the Redis service.

docker-compose up --build


The application will be available at `http://localhost:8000`.

### 5. (Alternative) Manual Local Run

If you prefer not to use Docker, you can run the services manually.

**Start Redis Server:**

redis-server

**Run the FastAPI App:**

uvicorn backend.main:app --reload


---

## 🛠️ Technology Stack

-   **Backend**: FastAPI, Python
-   **Frontend**: HTML5, CSS3, Vanilla JavaScript
-   **AI Provider**: Groq (Llama 3.1 Models)
-   **State Management**: Redis
-   **Deployment**: Docker, Docker Compose


## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

