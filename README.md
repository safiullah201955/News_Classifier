# News_Classifier

## 📌 Project Overview

This project demonstrates how to **fine-tune a transformer-based model** for text classification while using **parameter-efficient training**:
- **Frozen base layers** for faster training.
- **Unfrozen last 2 transformer layers** for domain adaptation.
- **Trainable classification head** for optimal accuracy.

- ## 📂 Dataset

- **Source:** AG News Dataset
- **Classes:**
  1. Politics
  2. Sports
  3. Business
  4. Sci/Tech

## 🧠 Model & Training

- **Base Model:** `distilbert-base-uncased`
- **Fine-tuning Strategy:**
  1. Freeze all DistilBERT parameters.
  2. Unfreeze last **2 transformer layers**.
  3. Keep classifier head trainable.
- **Training Framework:** Hugging Face `Trainer`
- **Epochs:** 1  
- **Batch Size:** 8  
- **Optimizer & Scheduler:** Default in Transformers

- ## 📊 Results

| Metric          | Score  |
|----------------|--------|
| **Accuracy**   | 0.909  |
| **F1 Score**   | 0.909  |
| **Loss**       | 0.322  |

**Evaluation Summary:**
- **Runtime:** ~376s  
- **Samples/sec:** ~5.31  

## 💻 Streamlit App

The model is wrapped in a **Streamlit web interface** for easy interaction.  
Simply input a news headline, and the app predicts the category.
