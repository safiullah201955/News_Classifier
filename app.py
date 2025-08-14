from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import streamlit as st

model = AutoModelForSequenceClassification.from_pretrained(
    "text_classifier",
    device_map=None,
    torch_dtype=torch.float32
).to("cpu")

tokenizer = AutoTokenizer.from_pretrained("text_classifier_tok")

label_names = ["Politics", "Sports", "Business", "Sci/Tech"]

st.title("📰 News Topic Classifier")

text = st.text_area("Enter a news headline:")

if st.button("Predict"):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    pred_id = torch.argmax(outputs.logits, dim=1).item()
    st.write(f"**Predicted Topic:** {label_names[pred_id]}")