# 📈 Financial Sentiment Analysis

A full-stack machine learning application that classifies the sentiment of financial text (news headlines, reports, tweets) as **positive**, **negative**, or **neutral** using a deep learning LSTM model — served via a REST API and visualized through an interactive frontend.

---

## 🗂️ Project Structure

```
Financial_sentiment/
├── lstm.ipynb          # Model training notebook (LSTM architecture)
├── export.py           # Exports trained Keras model for TensorFlow Serving
├── api/                # Backend REST API
├── frontend/           # Web-based UI for live sentiment predictions
└── .gitignore
```

---

## 🧠 Model

The core model is a **Long Short-Term Memory (LSTM)** neural network built with TensorFlow/Keras, trained on labeled financial text data. LSTM networks are well-suited for this task due to their ability to capture sequential dependencies in text.

The training workflow is fully documented in [`lstm.ipynb`](lstm.ipynb), covering:

- Data loading and preprocessing
- Text tokenization and padding
- LSTM model definition and training
- Evaluation metrics

After training, [`export.py`](export.py) exports the model in **TensorFlow SavedModel format** for serving:

```bash
python export.py
```
---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- TensorFlow 2.x
- Node.js (for the frontend)

### 1. Clone the repository

```bash
git clone https://github.com/Dapansuu/Financial_sentiment.git
cd Financial_sentiment
```

### 2. Install Python dependencies

```bash
pip install tensorflow numpy pandas scikit-learn jupyter
```

### 3. Train the model

Open and run the Jupyter notebook:

```bash
jupyter notebook lstm.ipynb
```

### 4. Export the model

```bash
python export.py
```

### 5. Start the API

```bash
cd api
# Install dependencies and start server (refer to api/ directory for details)
```

### 6. Start the Frontend

```bash
cd frontend
# Install dependencies and start the dev server (refer to frontend/ directory for details)
```

---

## 🔌 API

The `api/` directory contains a backend server that exposes endpoints for running sentiment inference on input text. Send a POST request with a financial text string and receive a sentiment label and confidence score in response.

Example request:

```json
POST /predict
{
  "text": "Company reports record profits amid market rally"
}
```

Example response:

```json
{
  "sentiment": "positive",
  "confidence": 0.94
}
```

---

## 🖥️ Frontend

The `frontend/` directory contains a web interface (HTML/CSS/JavaScript) that allows users to type or paste financial text and see real-time sentiment predictions powered by the API.

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Model     | TensorFlow / Keras LSTM |
| Notebook  | Jupyter Notebook        |
| Export    | TensorFlow SavedModel   |
| API       | Python (backend server) |
| Frontend  | HTML, CSS, JavaScript   |

---

## 📄 License

This project is open source. Feel free to fork, contribute, or use it as a learning reference.

---

## 🙋 Author

**Dapansuu** — [GitHub Profile](https://github.com/Dapansuu)