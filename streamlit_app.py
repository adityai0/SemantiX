import streamlit as st
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "model"  

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    
    return tokenizer, model, device

tokenizer, model, device = load_model()

def predict(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )
    
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits.detach().cpu().numpy()
    prob = float(1 / (1 + np.exp(-logits[0][0])))
    label = 1 if prob >= 0.5 else 0
    
    return prob, label

st.set_page_config(page_title="SemantiX", layout="centered")

st.title("SemantiX – Multilingual Toxicity Detection")
st.markdown("Detect whether a sentence is **toxic or non-toxic**.")

text = st.text_area("Enter text here:")

if st.button("Analyze"):
    if text.strip():
        prob, label = predict(text)

        st.subheader("Result")

        if label == 1:
            st.error("⚠️ Toxic Content Detected")
        else:
            st.success("✅ Non-Toxic Content")

        st.subheader("Confidence Score")
        st.progress(prob)

        st.write(f"**Probability:** {prob:.4f}")
        st.write(f"**Label:** {label}")
    else:
        st.warning("Please enter some text.")