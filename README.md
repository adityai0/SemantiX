# SemantiX - Multilingual Toxicity Detection

SemantiX is an advanced multilingual toxicity detection system designed to identify harmful and toxic language across multiple languages, specifically fine-tuned for Hindi and English. It provides a highly accurate binary classification, allowing moderators and systems to flag toxic content in real time via a clean, interactive user interface.

## Features

- **Multilingual Support:** Seamlessly detects toxicity in both Hindi and English.
- **Real-Time Prediction:** Interactive Web UI powered by Streamlit for instant text analysis.
- **Transformer-based Architecture:** Utilizes a fine-tuned XLM-RoBERTa (XLM-R) model for state-of-the-art NLP performance.
- **Binary Classification:** Outputs strict `0` (non-toxic) or `1` (toxic) labels, ideal for automated moderation pipelines.

## Project Structure

```text
SemantiX/
├── streamlit_app.py               # Streamlit web application & inference logic
├── model.ipynb                    # Jupyter Notebook for model training & evaluation
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore file
├── toxic_labeled.xlsx             # Training dataset with binary labels
├── toxic_no_label_evaluation.xlsx # Evaluation dataset without labels
└── model/                         # Trained model weights & tokenizer (download separately)
```

## Generating the Model

Due to its large size (~1GB), the trained XLM-RoBERTa model is not included directly in this repository. 
You will need to generate the model files yourself by running the `model.ipynb` notebook before starting the Streamlit application. This will train the model and save the required artifacts into the `model/` directory.

## Setup & Run

Choose one of the following methods to run SemantiX:

### Option 1: Run on Google Colab (Recommended for Training)
1. Upload `model.ipynb` to Google Colab.
2. Install the necessary dependencies:
   ```bash
   !pip install -r requirements.txt
   ```
3. Upload your dataset (`toxic_labeled.xlsx` / `toxic_no_label_evaluation.xlsx`) to the Colab environment.
4. Run the notebook cells sequentially to train the model.
5. Download the final model files from the generated `model/` folder.
6. (Optional) Run the inference cells at the bottom of the notebook to test on sample text.

### Option 2: Run Locally (Recommended for Inference/UI)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/SemantiX.git
   cd SemantiX
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Generate the model** by running `model.ipynb` (locally or on Colab) and ensure the outputs are in the `model/` directory.
5. **Run the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

1. Open the local Streamlit URL provided in your terminal (usually `http://localhost:8501`).
2. Type or paste any English or Hindi sentence into the text box.
3. Click the **"Analyze"** button.
4. The system will process the text and display:
   - A strict **binary label** (`0` or `1`).
   - A **confidence score** representing the probability of the text being toxic.

## Tech Stack

- **Python** (Core language)
- **HuggingFace Transformers** (Base models and tokenization)
- **PyTorch** (Deep learning framework)
- **Streamlit** (Web application frontend)
- **Scikit-learn** (Metrics and evaluation)

## Example Output

**Input text:** *"I love this project, it's amazing!"*

**UI Output:**
- **Status:** Non-Toxic Content
- **Probability:** `0.0215`
- **Label:** `0`

**Input text:** *"तुम एक बेवकूफ इंसान हो"* *(You are a stupid person)*

**UI Output:**
- **Status:** Toxic Content Detected
- **Probability:** `0.9542`
- **Label:** `1`

## Notes

- **Submission Format:** The system is explicitly configured to output binary labels (`0` or `1` only) to comply with standard hackathon submission formats.
- **Thresholding:** The model uses a standard sigmoid activation function with a default threshold of `0.5` to separate toxic from non-toxic content.

## System Architecture and Pipeline

The end-to-end pipeline for SemantiX is structured as follows:

- **Dataset Ingestion:** Loading multilingual text data from structured files such as CSV and XLSX
- **Preprocessing:** Removal of null values, text normalization, and standardization of label columns
- **Data Splitting:** Stratified train-validation split to maintain class balance
- **Tokenization:** XLM-RoBERTa SentencePiece tokenizer with a maximum sequence length of 256 tokens
- **Model Fine-Tuning:** Fine-tuning XLM-RoBERTa using the Hugging Face framework with AdamW optimizer and optimized hyperparameters
- **Inference:** Generating probability scores for input text using the trained model
- **Decision Layer:** Applying a threshold to classify text as toxic or non-toxic
- **Evaluation:** Performance analysis using ROC-AUC, accuracy, confusion matrix, and classification metrics
- **Deployment:** Streamlit-based interface enabling real-time multilingual toxicity prediction

### Pipeline Flow

```text
User Input
↓
Preprocessing
↓
Tokenization (XLM-R)
↓
XLM-RoBERTa Model
↓
Sigmoid Probability
↓
Threshold Decision
↓
Final Prediction (Toxic / Non-Toxic)
↓
Streamlit Interface
```

## How we built it

We fine-tuned XLM-RoBERTa on a multilingual dataset and designed a robust pipeline for preprocessing and evaluation. The system leverages cross-lingual representations and supports efficient inference through a lightweight Streamlit interface.

Each input is:
- Tokenized using multilingual subword encoding
- Passed through the trained model
- Converted into a probability score
- Thresholded into a binary label

## Approach

The system is built on:
- XLM-RoBERTa for multilingual representation learning
- Cross-lingual embeddings for language-agnostic understanding

**Pipeline flow:**
- **Input:** Multilingual text in Hindi, English, or mixed form
- **Encoding:** SentencePiece tokenizer processes text
- **Inference:** Model outputs probability score
- **Output:** Toxic or Non-Toxic label, Confidence score

## Challenges we ran into

- Training instability and memory constraints with large transformer models
- Environment compatibility issues across local systems and cloud environments
- Handling label formatting and tensor shape mismatches during training
- Managing large model size for deployment

## Accomplishments that we're proud of

- Built a fully functional multilingual NLP system within limited time
- Achieved strong performance across Hindi, English, and code-mixed text
- Delivered a clean and interactive real-time demo using Streamlit
- Designed a scalable pipeline suitable for real-world moderation

## Performance Snapshot

- **ROC-AUC:** approximately 0.98 or higher
- **Accuracy:** approximately 94 to 95 percent
- Strong recall for toxic class indicating effective detection of harmful content

| Metric | Value |
| --- | --- |
| Accuracy | 94.55% |
| ROC-AUC | 0.99 |
| Precision | 0.9418 |
| Recall | 0.9544 |
| F1-Score | 0.9481 |

### Score Images

<img width="575" height="593" alt="Image" src="https://github.com/user-attachments/assets/ba37fb81-5d36-4556-b411-1a68f90c15eb" />
<img width="525" height="437" alt="Image" src="https://github.com/user-attachments/assets/438fadcf-0999-4af4-bbcc-030ab051e635" />

### What the Model Gets Right
- Detects implicit toxicity beyond explicit keywords
- Handles code-mixed inputs such as "tum stupid ho"
- Maintains consistent performance across language variations

### Observed Behavior
- Slight bias toward flagging borderline cases as toxic
- This trade-off improves safety but may introduce minor false positives

## Evaluation Strategy

We evaluated performance using multiple metrics:
- **ROC-AUC** for ranking capability
- **Precision and Recall** for class-wise balance
- **Confusion Matrix** for error distribution

## Interface

A lightweight Streamlit interface was built to:
- Accept real-time user input
- Display predictions instantly
- Show confidence scores

This makes the system usable beyond experimentation.

## What we learned

- Practical understanding of transformer fine-tuning
- Debugging and stabilizing machine learning pipelines
- Handling multilingual NLP challenges
- Balancing performance with deployment constraints

## What's next for SemantiX

- Extend beyond binary classification to multi-label toxicity detection
- Optimize inference speed for production deployment
- Add explainability using token importance and attention visualization
- Support additional Indian and global languages
- Deploy as a scalable API for real-world applications
