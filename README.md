# Advanced Automated Text Summarization System

## Overview
This project provides an advanced text summarization system that supports multiple types of documents (news articles, scientific papers, legal documents) and offers both extractive and abstractive summarization techniques. It features a user-friendly web interface, multi-language support, and advanced evaluation metrics.

### Streamlit View
Deploy and interact with the project live using Streamlit, allowing users to experience the summarization capabilities in real-time. [Check the deployed and interactive project here.](https://advanced-automated-text-summarization-harry262000.streamlit.app/)
1. Upload a document through the Streamlit interface.
2. Select the type of summarization (extractive, abstractive, or hybrid).
3. Generate the summary and view the results along with evaluation metrics.
4. Customize the summary length and focus as needed.
5. Use the interactive visualization tools to explore key sentences and their importance.


## Features
- **Multi-Type Document Handling:** Summarize various document types with adaptable preprocessing pipelines.
- **Hybrid Summarization Approach:** Integrates extractive (BERTSUM) and abstractive (T5, BART, Pegasus) techniques.
- **Contextual Understanding:** Incorporates topic modeling for better contextual understanding.
- **User Interface:** Streamlit-based web interface for document upload and summary generation.
- **Evaluation Metrics:** Detailed evaluation using ROUGE, BLEU, and METEOR scores.
- **Multi-Language Support:** Summarization in multiple languages using multilingual models.

## Folder Structure
- `data/`: Contains raw and processed datasets.
  - `raw/`: Original datasets categorized by document type.
  - `processed/`: Preprocessed datasets ready for model training.
- `models/`: Stores pre-trained and fine-tuned models.
  - `extractive/`: Models for extractive summarization.
  - `abstractive/`: Models for abstractive summarization.
  - `hybrid/`: Combined models for hybrid summarization.
- `notebooks/`: Jupyter notebooks for data preprocessing and model training.
- `src/`: Source code for data processing, model training, evaluation, and interface.
  - `data/`: Scripts for data loading, preprocessing, and topic modeling.
  - `models/`: Summarization model scripts.
  - `evaluation/`: Scripts for evaluation metrics.
  - `interface/`: Streamlit app and utility scripts.
  - `visualization/`: Scripts for visualizing summaries and highlighting sentences.
- `tests/`: Unit tests for data processing, models, evaluation, and interface.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Git ignore file.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/advanced_text_summarization.git
   cd advanced_text_summarization
2. Create a virtual enviorment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Data Preprocessing:
- Run the data preprocessing notebook to prepare the datasets:
  ```bash
  jupyter notebook notebooks/data_preprocessing.ipynb
2. Model Training:
- Train the extractive, abstractive and hybrid models using the respective notebooks.
  ```bash
  jupyter notebook notebooks/extractive_model_training.ipynb
  jupyter notebook notebooks/abstractive_model_training.ipynb
  jupyter notebook notebooks/hybrid_model_training.ipynb
3. Running the Interface:
- Start the streamlit app to interact with the summarization system.
  ```bash
  streamlit run src/interface/app.py
## Evalution

- Evaluate the performance of the summarization models using the provided evaluation scripts.
  ```bash
  python src/evaluation/rouge.py
  python src/evaluation/bleu.py

### Thank you for visiting.
