import streamlit as st
import joblib
import pandas as pd
from scrapper import scrape_karkidi_jobs, classify_new_jobs

# Load the trained model and vectorizer
model = joblib.load("job_cluster_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("🧠 Job Classifier - Karkidi Jobs")

keyword = st.text_input("🔍 Search keyword", "data science")
pages = st.slider("📄 Number of pages to scrape", 1, 5, 1)
user_clusters = st.multiselect("🎯 Choose your preferred clusters", [0, 1, 2, 3, 4], default=[1, 3])

if st.button("🚀 Check Jobs"):
    with st.spinner("Scraping job listings..."):
        df = scrape_karkidi_jobs(keyword=keyword, pages=pages)
    with st.spinner("Classifying jobs..."):
        classified = classify_new_jobs(df, model, vectorizer)

    matches = classified[classified["Cluster"].isin(user_clusters)]

    st.success(f"Found {len(matches)} job(s) in your preferred clusters!")
    st.dataframe(matches[["Title", "Company", "Location", "Skills", "Cluster"]])
