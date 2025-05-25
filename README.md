# Job Posting Classification

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

## Features

- ✅ Web scraper for real-time job data from Karkidi
- 🧠 TF-IDF + KMeans for job clustering
- 📊 Job grouping based on required skills
- 🌐 Streamlit web app for interactive exploration
- 📁 Saved models and vectorizers for reuse

---

## 💻 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Sreelakshmi-rv/Job_posting_classification.git
cd Job_posting_classification

# Optional: Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

---
