import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import os
import time
from transformers import pipeline

# Function to load images with error handling
def load_image(image_path):
    if os.path.exists(image_path):
        return Image.open(image_path)
    else:
        st.error(f"Image not found: {image_path}")
        return None

# Load icons
linkedin_icon_path = "app/assets/icons/linkedin.png"
github_icon_path = "app/assets/icons/github.png"
resume_icon_path = "app/assets/icons/approved.png"

linkedin_icon = load_image(linkedin_icon_path)
github_icon = load_image(github_icon_path)
resume_icon = load_image(resume_icon_path)

# Convert images to base64 for inline display
def image_to_base64(image):
    if image:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None

linkedin_icon_base64 = image_to_base64(linkedin_icon)
github_icon_base64 = image_to_base64(github_icon)
resume_icon_base64 = image_to_base64(resume_icon)

# Sidebar information
st.sidebar.markdown("""
    <style>
    .circle-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
        margin: 20px auto;
    }
    .circle-image img {
        width: 100%;
        height: auto;
        object-fit: cover;
    }
    .sidebar-text {
        text-align: left;
        margin-bottom: 10px;
    }
    .sidebar-text-name{
        font-weight: bold;
        margin-bottom: 5px;
        text-align: center;
    }
    .sidebar-link {
        text-align: center;
        margin-bottom: 10px;
    }
    .sidebar-section-title {
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .social-icons img {
        width: 24px;
        height: 24px;
        margin: 0 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load the profile image
image_path = "app/assets/images/86480339.jpeg"
image = Image.open(image_path)
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

st.sidebar.markdown(f'<div class="circle-image"><img src="data:image/jpeg;base64,{img_str}"></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-text-name">Harshal Honde</div>', unsafe_allow_html=True)

# Sidebar contact and social links
st.sidebar.markdown('<div class="sidebar-section-title">Contact Information:</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-text">HarshalHonde50@gmail.com</div>', unsafe_allow_html=True)
if linkedin_icon_base64 and github_icon_base64:
    st.sidebar.markdown(f"""
        <div class="social-icons" style="text-align: center;">
            <a href="https://www.linkedin.com/in/harshal-honde268/">
                <img src="data:image/png;base64,{linkedin_icon_base64}" alt="LinkedIn">
            </a>
            <a href="https://github.com/Harry262000">
                <img src="data:image/png;base64,{github_icon_base64}" alt="GitHub">
            </a>
            <a href="/assets/Resume/Harshal_Honde_Intern.pdf">
                <img src="data:image/png;base64,{resume_icon_base64}" alt="Resume">
            </a>
        </div>
    """, unsafe_allow_html=True)

# Sidebar skills and hobbies
st.sidebar.markdown("""
<style>
.sidebar-list {
    list-style-type: disc; /* Adds bullet points */
    padding-left: 20px; /* Adjust the indentation */
}
.sidebar-text {
    margin-bottom: 5px; /* Space between list items */
}
</style>
<div class="sidebar-section-title">Skills</div>
<ul class="sidebar-list">
    <li class="sidebar-text">Python</li>
    <li class="sidebar-text">Machine Learning</li>
    <li class="sidebar-text">NLP</li>
    <li class="sidebar-text">T5</li>
    <li class="sidebar-text">BERT</li>
    <li class="sidebar-text">Deep Learning</li>
    <li class="sidebar-text">Transformers</li>
</ul>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <a href="https://www.linkedin.com/in/harshal-honde268/" target="_blank">
        <button style="background-color: #FF4B4B; border-radius: 8px; border: none; color: white; padding: 12px 30px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; cursor: pointer;">
            Hire me
        </button>
    </a>
    """, unsafe_allow_html=True)

# Title of the app
st.title("Advanced Automated Text Summarization System")

# Instructions
st.write("""
## Instructions
This application allows you to upload a document or paste text directly, select the type of summarization (extractive, abstractive, or hybrid), and generate summaries.

### Features:
- **Upload a Document or Paste Text:** Choose your preferred input method.
- **Summarization:** Select between extractive, abstractive, and hybrid summarization techniques.
- **Customization:** Adjust summary length and focus as needed.
- **Evaluation Metrics:** View ROUGE, BLEU, and METEOR scores.
- **Multi-Language Support:** Summarization in multiple languages.

### Upload Guidelines:
- **File Format:** Ensure the file is a text format (.txt).
- **Maximum File Size:** The maximum file size allowed is 5 MB.
""")
# Example text
example_text = """
Machine learning is a field of artificial intelligence that uses statistical techniques to give computers the ability to learn from data without being explicitly programmed. It involves algorithms that can identify patterns and make predictions.
"""

# Simulated summaries for each technique (you'll replace these with actual model outputs)
extractive_summary = "Machine learning is a field of artificial intelligence that uses statistical techniques to give computers the ability to learn from data."
abstractive_summary = "Machine learning enables computers to learn from data and make predictions using advanced algorithms, a key aspect of artificial intelligence."
hybrid_summary = "Machine learning, a subset of artificial intelligence, involves statistical methods that allow computers to learn from and predict data patterns, without direct programming."

# Display the example text
st.write("### Example Text")
st.write(example_text)

# Displaying the table with summaries
st.write("""
### Summarization Techniques

| **Technique**   | **Description**                                                                                                           | **Example**                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Extractive**  | Selects important sentences or phrases directly from the original text to create a summary. It essentially "extracts" parts of the original content. | **Extractive Summary:** "Machine learning is a field of artificial intelligence that uses statistical techniques to give computers the ability to learn from data."  |
| **Abstractive** | Generates new sentences that paraphrase the original text. This method creates a summary that might not directly use the original wording but still conveys the same meaning. | **Abstractive Summary:** "Machine learning enables computers to learn from data and make predictions using advanced algorithms, a key aspect of artificial intelligence." |
| **Hybrid**      | Combines both extractive and abstractive methods. It first extracts key sentences or phrases and then uses abstractive techniques to refine and paraphrase the extracted content. | **Hybrid Summary:** "Machine learning, a subset of artificial intelligence, involves statistical methods that allow computers to learn from and predict data patterns, without direct programming."
""")

# Input type selection
input_method = st.radio("Select Input Method:", ("Upload Document", "Paste Text"))

# Lazy-loaded summarization models
def load_models():
    return pipeline("summarization", model="facebook/bart-large-cnn"), pipeline("summarization", model="t5-base")

# Summarization function
def summarize_text(text, summarization_type, max_length):
    extractive_model, abstractive_model = load_models()
    if summarization_type == "Extractive":
        summary = extractive_model(text, max_length=max_length, min_length=30, do_sample=False)
    elif summarization_type == "Abstractive":
        summary = abstractive_model(text, max_length=max_length, min_length=30, do_sample=False)
    else:  # Hybrid (first extractive, then abstractive)
        intermediate_summary = extractive_model(text, max_length=max_length, min_length=30, do_sample=False)
        summary = abstractive_model(intermediate_summary[0]['summary_text'], max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if input_method == "Upload Document":
    uploaded_file = st.file_uploader("Upload a text file", type="txt", help="Select a text file (up to 5 MB)")
    
    if uploaded_file is not None:
        # Check file size
        file_size_mb = uploaded_file.size / (1024 * 1024)
        if file_size_mb > 5:
            st.error("File size exceeds 5 MB. Please upload a smaller file.")
        else:
            text = uploaded_file.read().decode("utf-8")
            st.subheader("Original Text")
            st.text_area("Text from File", value=text, height=300)

            # Summarization options
            st.subheader("Summarization Options")
            summarization_type = st.selectbox("Select Summarization Type", ["Extractive", "Abstractive", "Hybrid"])
            max_length = st.slider("Summary Length", min_value=50, max_value=500, value=150)

            if st.button("Submit and Generate Summary"):
                with st.spinner('Summarizing... This may take 2-3 minutes...'):
                    time.sleep(3)  # Simulate a delay for processing
                    summary = summarize_text(text, summarization_type, max_length)
                    st.subheader("Generated Summary")
                    st.text_area("Summary", value=summary, height=200)

elif input_method == "Paste Text":
    text_input = st.text_area("Paste Your Text Here:", height=200)
    st.markdown("Press 'ctrl + Enter' to submit text...")
    
    if text_input:
        st.subheader("Summarization Options")
        summarization_type = st.selectbox("Select Summarization Type", ["Extractive", "Abstractive", "Hybrid"])
        max_length = st.slider("Summary Length", min_value=50, max_value=500, value=150)

        if st.button("Submit and Generate Summary"):
            with st.spinner('Summarizing... This may take 2-3 minutes...'):
                time.sleep(3)  # Simulate a delay for processing
                summary = summarize_text(text_input, summarization_type, max_length)
                st.subheader("Generated Summary")
                st.text_area("Summary", value=summary, height=200)

# Add future evaluation metrics functionality
st.write("""
## Future Enhancements
- **Interactive Visualization:** Explore key sentences and their importance.
- **Advanced Evaluation Metrics:** Detailed evaluation using ROUGE, BLEU, METEOR scores.
- **Multi-Language Summarization:** Support for additional languages.
""")
