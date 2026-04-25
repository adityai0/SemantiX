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

## Model Download Instructions

Due to its large size (~1GB), the trained XLM-RoBERTa model is not included directly in this repository.

1. Download the pre-trained model files from this link:
   [**Download SemantiX Model (Google Drive)**](#) *(Replace with actual link)*
2. Extract the downloaded archive.
3. Place the extracted contents into the `model/` directory at the root of the project.

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
4. **Download the model** (see instructions above) and place it in the `model/` directory.
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

## Future Improvements

- **Multi-label Classification:** Expand from binary classification to granular categories (e.g., threat, insult, identity hate).
- **More Languages:** Fine-tune on additional diverse regional languages to increase accessibility.
- **API Deployment:** Wrap the inference script in a FastAPI backend for easy integration into mobile apps or third-party platforms.
