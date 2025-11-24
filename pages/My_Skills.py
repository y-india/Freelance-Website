import streamlit as st

st.set_page_config(page_title="My Skills", page_icon="💡", layout="wide")






st.markdown("""
<style>
.block-container {
    padding-top: 0.95rem !important;   
}
</style>
""", unsafe_allow_html=True)









page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_BACKGROUND_FOR_HIRING_WEB.jpg");
    background-size: cover;
}} 
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)






def navbar_full_width():
    st.markdown("""
    <style>

    .full-nav {
        width: 100vw;
        padding: 14px 0;
        margin: 0;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        display: flex;
        justify-content: flex-end;
        padding-right: 30px;
        margin-top: 5px;
        gap: 22px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        position: relative;
        left: 50%;
        transform: translateX(-50%);
        z-index: 999;
    }

    .nav-btn {
        color: #E0E7FF !important;
        font-size: 14px;
        font-weight: 600;
        padding: 6px 16px;
        border-radius: 8px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        transition: 0.22s ease;
        text-decoration: none;
    }

    .nav-btn:hover {
        background: rgba(255,215,0,0.18);
        border-color: rgba(255,215,0,0.45);
        box-shadow: 0 0 10px rgba(255,215,0,0.45);
        transform: translateY(-1px);
    }

    </style>

    <div class="full-nav">
        <a class="nav-btn" href="/" target="_self">Home</a>
        <a class="nav-btn" href="/My_Skills" target="_self">Skills</a>
        <a class="nav-btn" href="/Why_Hire_Me" target="_self">Why Me</a>
        <a class="nav-btn" href="/Services" target="_self">Services</a>
        <a class="nav-btn" href="/Contact_Me" target="_self">Contact</a>
    </div>

    """, unsafe_allow_html=True)

navbar_full_width()










# Title
st.markdown(
    "<h1 style='text-align:center; color:#E0E7FF;'>💡 My Skills 💡</h1>",
    unsafe_allow_html=True
)

# ---------- CSS STYLING ----------
st.markdown("""
<style>
.skill-box {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    padding: 22px;
    border-radius: 14px;
    border: 1px solid rgba(255,0,0,0.25); /* light red tint */
    text-align: center;
    font-size: 18px;
    color: #E0E7FF;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
    transition: 0.25s ease;
    margin-bottom: 25px;
}

/* 🔥 RED GLOW EFFECT */
.skill-box:hover {
    transform: translateY(-4px) scale(1.03);
    background: rgba(255,0,0,0.18);
    border-color: rgba(255,0,0,0.6);
    box-shadow: 
        0 0 18px rgba(255, 0, 0, 0.9),
        0 0 32px rgba(255, 40, 40, 0.55),
        0 0 60px rgba(255, 0, 0, 0.35);
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    color: #E0E7FF;
    text-align: center;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 🔥 1. About Me (Short, Professional Summary)
# ============================================================

st.markdown("<div class='section-title'>👦 About Me</div>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; color:#E0E7FF; font-size:17px;'>
I’m Yuvraj Rana, 
            <br>A self-taught Python and Machine Learning developer who enjoys building practical, data-driven solutions. 
            <br>I work with Python, machine learning, computer vision, data analytics, and Streamlit to create clean, functional projects.
<br>I focus on understanding problems deeply, writing clear code, and turning ideas into real applications through consistent learning and hands-on practice.
</div>
""", unsafe_allow_html=True)


# ============================================================
# 🔥 2. Technical Skills (Grid Layout)
# ============================================================

st.markdown("<div class='section-title'>🧰 Technical Skills</div>", unsafe_allow_html=True)

skills = [
    "🐍 Python Programming",
    "📊 Pandas",
    "🔢 NumPy",
    "📈 Matplotlib",
    "🌈 Seaborn",
    "🧮 SciPy",
    "🤖 Machine Learning (scikit-learn)",
    "🧠 Model Training & Evaluation",
    "🧼 Data Cleaning",
    "🔍 Data Analysis",
    "📊 Data Visualization",
    "👁️ OpenCV (Computer Vision)",
    "⚙️ Automation Tools",
    "🌐 Streamlit Web Apps",
    "📝 Creating ML Notes & Documentation"
]

cols = st.columns(3, gap="large")

for i, skill in enumerate(skills):
    with cols[i % 3]:
        st.markdown(f"<div class='skill-box'>{skill}</div>", unsafe_allow_html=True)


# ============================================================
# 🔥 3. Projects Section
# ============================================================

st.markdown("<div class='section-title'>🚀 Projects I Have Built</div>", unsafe_allow_html=True)

projects = [
    "🌾 AI-Based Crop Predictor (For Haryana Farmers)",
    "📉 Customer Churn Prediction System",
    "😃 Attendance System with Face Recognition",
    "🚗 Road Accident Severity Prediction",
    "🎯 Real-Time Object Tracker (OpenCV)",
    "📘 Machine Learning Notes (self-created)",
    "🌐 Portfolio Website (fully custom-built)",
    "📝 Retail Sales Anaysis ",
    "  Visit GITHUB for DETAILS and MORE PROJECTS"
]




project_cols = st.columns(3, gap="large")

for i, p in enumerate(projects):
    with project_cols[i % 3]:
        st.markdown(f"<div class='skill-box'>{p}</div>", unsafe_allow_html=True)



st.markdown("""
    <br>    """ , unsafe_allow_html=True
        
)
# -----------------------------------------------------------
# GitHub Link
# -----------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <a href="https://github.com/y-india" target="_blank">
            <button style="
                background-color:#00BFFF;
                border:none;
                color:white;
                padding:14px 28px;
                font-size:17px;
                font-weight:600;
                border-radius:12px;
                cursor:pointer;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            ">
            🔗 View GitHub
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)






st.markdown("""
    <br>    """ , unsafe_allow_html=True
        
)




# ============================================================
# 🧰 4. Tools I Use
# ============================================================

st.markdown("<div class='section-title'>🧰 Tools I Use</div>", unsafe_allow_html=True)

tools = [
    "🖥️ VS Code",
    "📓 Jupyter Notebook",
    "🧩 GitHub ",
    "☁️ Google Colab",
    "🌐 Streamlit",
    "🖌️ Canva",
    "🤖 ChatGPT / AI Tools",
    "📊 Kaggle",
]

tool_cols = st.columns(3, gap="large")

for i, tool in enumerate(tools):
    with tool_cols[i % 3]:
        st.markdown(f"<div class='skill-box'>{tool}</div>", unsafe_allow_html=True)
