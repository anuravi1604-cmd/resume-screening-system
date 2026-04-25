import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def compute_match(resume, jd):
    resume = clean_text(resume)
    jd = clean_text(jd)

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume, jd])

    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def extract_keywords(resume, jd):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume, jd])

    feature_names = vectorizer.get_feature_names_out()
    resume_vec = vectors[0].toarray()[0]
    jd_vec = vectors[1].toarray()[0]

    common_indices = [i for i in range(len(feature_names)) if resume_vec[i] > 0 and jd_vec[i] > 0]

    keywords = [(feature_names[i], resume_vec[i] + jd_vec[i]) for i in common_indices]
    keywords = sorted(keywords, key=lambda x: x[1], reverse=True)

    return [k[0] for k in keywords[:10]]

def missing_keywords(resume, jd):
    resume_words = set(clean_text(resume).split())
    jd_words = set(clean_text(jd).split())

    missing = list(jd_words - resume_words)
    return missing[:10]