import os

import streamlit as st

from dotenv import load_dotenv

from openai import OpenAI


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# APPLICATION TITLE
# =========================================================

st.title("🤖 AI Resume Analyzer")

st.write(
    """
    Analyze your resume against a job description
    using Generative AI.
    """
)


# =========================================================
# CHECK API KEY
# =========================================================

if not HF_TOKEN:

    st.error(
        """
        Hugging Face API token not found.

        Please create a .env file containing:

        HF_TOKEN=hf_your_token_here
        """
    )

    st.stop()


# =========================================================
# HUGGING FACE OPENAI-COMPATIBLE CLIENT
# =========================================================

client = OpenAI(

    # Hugging Face OpenAI-compatible API
    base_url="https://router.huggingface.co/v1",

    # Hugging Face token
    api_key=HF_TOKEN
)


# =========================================================
# MODEL CONFIGURATION
# =========================================================

MODEL_NAME = "openai/gpt-oss-120b"


# =========================================================
# RESUME INPUT
# =========================================================

st.subheader("📄 Resume")

resume = st.text_area(

    "Paste your resume",

    height=250,

    placeholder="""
Example:

AI Engineer with 3 years of experience
in Python, Machine Learning and NLP.

Skills:
Python
SQL
Machine Learning
Deep Learning
NLP
FastAPI
Docker
"""
)


# =========================================================
# JOB DESCRIPTION INPUT
# =========================================================

st.subheader("💼 Job Description")

job_description = st.text_area(

    "Paste the job description",

    height=250,

    placeholder="""
Example:

We are looking for an AI Engineer with
experience in Python, Machine Learning,
Deep Learning, NLP, LLMs and RAG.
"""
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(

    "🚀 Analyze Resume",

    use_container_width=True

):

    # =====================================================
    # VALIDATE INPUT
    # =====================================================

    if not resume.strip():

        st.warning(
            "Please paste your resume."
        )

        st.stop()


    if not job_description.strip():

        st.warning(
            "Please paste the job description."
        )

        st.stop()


    # =====================================================
    # PROMPT ENGINEERING
    # =====================================================

    prompt = f"""
You are an expert AI recruitment assistant.

Your task is to analyze a candidate's resume
against a job description.

IMPORTANT RULES:

1. Use only information explicitly present
   in the resume.

2. Do NOT invent skills.

3. Do NOT invent experience.

4. Do NOT invent certifications.

5. Do NOT invent projects.

6. Do NOT assume technologies that are not
   explicitly mentioned.

7. Be concise and practical.

8. Give an estimated match score based only
   on evidence present in the resume.

--------------------------------------------------
RESUME
--------------------------------------------------

{resume}

--------------------------------------------------
JOB DESCRIPTION
--------------------------------------------------

{job_description}

--------------------------------------------------
REQUIRED OUTPUT
--------------------------------------------------

Return the analysis using exactly these sections:

## 1. MATCH SCORE

Give an estimated percentage from 0 to 100.

Briefly explain why.

## 2. MATCHING SKILLS

List important skills that appear in both
the resume and job description.

## 3. MISSING SKILLS

List important job requirements that are
not clearly demonstrated in the resume.

## 4. EXPERIENCE GAP

Explain important differences between
the candidate's experience and the role.

## 5. RESUME IMPROVEMENTS

Give exactly 5 practical improvements.

## 6. TECHNICAL INTERVIEW QUESTIONS

Generate exactly 5 technical interview
questions based on the job description
and candidate background.

## 7. PROFESSIONAL SUMMARY

Write a concise professional summary
tailored to this job.

Do not claim that the candidate has
experience that is not present in the resume.
"""


    # =====================================================
    # CALL LLM
    # =====================================================

    with st.spinner(
        "🤖 AI is analyzing your resume..."
    ):

        try:

            response = client.chat.completions.create(

                model=MODEL_NAME,

                messages=[

                    {
                        "role": "system",

                        "content": (
                            "You are a professional "
                            "AI recruitment assistant."
                        )
                    },

                    {
                        "role": "user",

                        "content": prompt
                    }

                ],

                temperature=0.2,

                max_tokens=1200

            )


            # =================================================
            # EXTRACT RESPONSE
            # =================================================

            result = (
                response
                .choices[0]
                .message
                .content
            )


        # =====================================================
        # ERROR HANDLING
        # =====================================================

        except Exception as e:

            st.error(
                "❌ Unable to generate the analysis."
            )

            st.code(
                str(e)
            )

            st.stop()


    # =========================================================
    # DISPLAY RESULT
    # =========================================================

    st.divider()

    st.subheader(
        "🤖 AI Analysis"
    )

    st.markdown(
        result
    )


    # =========================================================
    # DOWNLOAD RESULT
    # =========================================================

    st.download_button(

        label="📥 Download Analysis",

        data=result,

        file_name="resume_analysis.txt",

        mime="text/plain"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Built with Python • Streamlit • Hugging Face • "
    "Generative AI"
)