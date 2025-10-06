# LLM Feedback Model

This repository contains components to investigate the performance of LLMs and transformer models at sentiment analysis and feedback understanding using both **OpenAI GPT-5** and **BERT** models.

---

## `openai/` — GPT-5 Integration

- Contains code to connect to the **OpenAI GPT-5 API**.  
- Runs **prompt-based summarization** and **sentiment analysis** tasks on textual feedback.  
- Saves the generated outputs and metadata into an **Excel sheet** for downstream analysis or validation.

---

## `bert_absa/` — BERT Aspect-Based Sentiment Analysis (ABSA)

- Contains a full **pipeline to extract, transform, and manipulate** data from the **EduRABSA dataset**.  
- Trains and evaluates a **BERT model** for **Aspect-Based Sentiment Analysis (ABSA)** using **pairwise classification**.  
  - Each input pair consists of a `(sentence, aspect)` combination.  
  - The model predicts a corresponding sentiment label:  
    - `2` → Positive  
    - `1` → Neutral  
    - `0` → Negative  
- Includes preprocessing steps, training, evaluation, and model export components.

---


