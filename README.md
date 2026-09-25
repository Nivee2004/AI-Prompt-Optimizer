# 🤖 AI Prompt Optimizer

A simple Generative AI application that transforms a raw user prompt into a clearer, more structured, and effective prompt using an LLM.

## 🚀 What Does It Do?

Users can enter a simple prompt such as:

> Tell me about RAG

The application analyzes the prompt and generates an improved version by organizing it around:

* **Role**
* **Task**
* **Context**
* **Audience**
* **Output Format**
* **Constraints**

### Example

**Input:**

```text
Tell me about RAG
```

**Output:**

```text
ROLE:
You are an AI educator.

TASK:
Explain Retrieval-Augmented Generation.

CONTEXT:
The learner has basic knowledge of AI.

AUDIENCE:
College students and beginners.

OUTPUT FORMAT:
Explain the concept with examples and a simple workflow.

CONSTRAINTS:
Use simple English and avoid unnecessary jargon.
```

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* Large Language Model (LLM)
* python-dotenv

## 🧠 Prompt Engineering Concepts

This project applies several Prompt Engineering concepts:

* Role prompting
* Task definition
* Context setting
* Audience specification
* Output formatting
* Constraints
* Zero-shot prompting
* Prompt iteration
* Prompt optimization

## 🔄 How It Works

```text
User Input
    ↓
Raw Prompt
    ↓
Groq API
    ↓
LLM
    ↓
Prompt Optimization
    ↓
Structured Improved Prompt
    ↓
Display Result
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Prompt-Optimizer.git
cd AI-Prompt-Optimizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

**Never commit your API key to GitHub.**

### 4. Run the application

```bash
streamlit run app.py
```

## 📌 Current Features

* Accepts a raw user prompt
* Uses an LLM to analyze the prompt
* Improves prompt clarity and structure
* Identifies key prompt components
* Displays the improved prompt through a Streamlit interface

## 🔮 Future Improvements

* Generate an AI response using the improved prompt
* Compare original and improved prompts
* Compare responses generated from both prompts
* Add reusable prompt templates
* Add prompt quality evaluation
* Improve the user interface

## 📚 Key Learning

Prompt Engineering is not about finding a "magic prompt."

It is about providing an AI model with **clear instructions, relevant context, a defined output format, and appropriate constraints**, then testing and iterating based on the results.
