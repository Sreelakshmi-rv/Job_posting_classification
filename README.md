# Job Posting Classification

🚀 [Live Demo](https://jobpostingclassification-7augcb2gyc8tkfhq9qzjvw.streamlit.app/)  
🎯 Find jobs, faster — categorized by skills, clustered by AI.

This project scrapes job listings from [Karkidi.com](https://www.karkidi.com/), processes the job descriptions using Natural Language Processing (NLP), and uses unsupervised machine learning (clustering) to classify job postings based on required skills. It helps users identify relevant job groups and discover opportunities that match their expertise.

The classified job data is then served through an interactive **Streamlit** web app.

---

## Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Info](#-model-info)
- [Future Improvements](#-future-improvements)
- [License](#-license)

---

## Overview

This is a **Data Science mini-project** where job data is scraped, vectorized using **TF-IDF**, and clustered using **KMeans** to uncover hidden patterns in job postings. It's particularly useful for automating job categorization without labeled datasets.

---

## 🖼️ App Demo



> ✨ You can explore job clusters and skill groupings directly from your browser.

## Features

- ✅ Web scraper for real-time job data from Karkidi
- 🧠 TF-IDF + KMeans for job clustering
- 📊 Job grouping based on required skills
- 🌐 Streamlit web app for interactive exploration
- 📁 Saved models and vectorizers for reuse

---

## Installation

Clone the repository and install dependencies:

``` bash
git clone https://github.com/Sreelakshmi-rv/Job_posting_classification.git
cd Job_posting_classification

# Optional: Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```
---

## Usage

1. Scrape Job Data
   ``` bash
   python scrapper.py
   ```
2. Launch the Streamlit App
   ``` bash
   streamlit run streamlit_app.py
   ```

---

## Project Structure

├── data_science_all_jobs_*.csv         # Raw job postings
├── data_science_matched_jobs_*.csv     # Cleaned/processed jobs
├── job_cluster_model.pkl               # Trained KMeans clustering model
├── tfidf_vectorizer.pkl                # TF-IDF vectorizer for text processing
├── scrapper.py                         # Web scraping script
├── streamlit_app.py                    # Streamlit web app
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation

---

## Model Info

- Text Preprocessing: Job titles and descriptions are cleaned and vectorized using TfidfVectorizer.
- Model Used: KMeans is used to group similar job postings into clusters based on required skills.
- Goal: Auto-classify new jobs into meaningful, human-readable categories.

---

## Future Improvements

- Add job alert system (email notifications)
- Include visual analytics in the Streamlit app
- Improve clustering with contextual NLP (e.g., BERT embeddings)
- Evaluate cluster coherence and interpretability
- Expand scraping to other job sites (e.g., LinkedIn, Naukri)

---

## 🙌 Acknowledgments

- Karkidi.com for job listings
- Streamlit and Scikit-learn community
- Built as part of a portfolio project @ Digital University Kerala 🎓

