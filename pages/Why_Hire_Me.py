import streamlit as st






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

















# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Why Hire Me", layout="wide")

# ================================
# CUSTOM CSS
# ================================
st.markdown("""
<style>
.section-title {
    font-size: 34px;
    font-weight: 800;
    text-align: center;
    color: #E0E7FF;
    margin-top: 10px;
    margin-bottom: 40px;
}

/* Card style */
.hire-card {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    padding: 28px 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.20);
    color: #E0E7FF;
    font-size: 18px;
    line-height: 1.5;
    box-shadow: 0 5px 25px rgba(0,0,0,0.35);
    transition: 0.3s;
}

.hire-card:hover {
    transform: translateY(-6px) scale(1.02);
    background: rgba(255,255,255,0.20);
    border-color: rgba(255,255,255,0.45);
    box-shadow: 0 0 18px rgba(255, 215, 0, 0.85),
            0 0 28px rgba(255, 215, 0, 0.55);
}

/* Bullet points */
.hire-card ul {
    list-style: none;
    padding-left: 8px;
}

.hire-card ul li::before {
    content: "✔ ";
    color: #FF8080;
    font-weight: 700;
    margin-right: 4px;
}
</style>
""", unsafe_allow_html=True)

# ================================
# PAGE TITLE
# ================================
st.markdown("<div class='section-title'>🌟 Why Hire Me? 🌟</div>", unsafe_allow_html=True)








# CSS (card + red glow)
st.markdown("""
<style>
.hire-card {
    background: rgba(255,255,255,0.10);
    padding: 28px;
    border-radius: 12px;
    margin-bottom: 35px;
    border: 1px solid rgba(255,0,0,0.18);
    color: #FFF;
    box-shadow: 0 4px 14px rgba(0,0,0,0.35);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.hire-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 18px rgba(255, 255, 0, 0.8),
            0 0 28px rgba(255, 255, 0, 0.5);
    border-color: rgba(255,0,0,0.6);
}
.hire-title {
    color: #FFCCCC;
    margin-bottom: 8px;
    font-size: 18px;
    font-weight: 700;
}
.hire-desc { font-size: 14px; line-height:1.45; color: #FFECEC; }
</style>
""", unsafe_allow_html=True)

# safe, HTML-wrapped content items (clean)
points = [
    ("🔥 I Build Practical, Real-World Solutions",
     "I focus on solving real problems with clean logic and user-friendly design. My projects are practical, efficient, and built for real use."
    ),
    ("🤖 Strong Skills in AI, Data & Automation",
     "<ul style='margin:6px 0 0 18px'><li>Machine Learning (scikit-learn)</li><li>Data cleaning & analysis</li><li>Computer Vision (OpenCV)</li><li>Streamlit apps</li><li>Python automation</li></ul>"
    ),
    ("⚡ Fast Delivery & Clear Communication",
     "Quick responses, smooth workflow, and transparent updates — no confusion."
    ),
    ("🧠 I Learn Fast & Adapt Quickly",
     "If your project needs something new, I learn and apply it quickly to deliver results."
    ),
    ("🎯 I Care Deeply About Quality",
     "Clean code, structured files, proper documentation, and polished results — your project gets done right."
    ),
    ("🤝 Client Satisfaction First",
     "Revisions, clarifications, and expectations are all handled smoothly."
    ),
    ("💰 Affordable Pricing",
     "Great value for money — suitable for students, startups, and professionals."
    ),
]

# Render rows: two cards per row; center last single if odd count
i = 0
while i < len(points):
    # if last single item -> center it using three columns with middle column for content
    if i == len(points) - 1:
        left, center, right = st.columns([1, 0.9, 1])  # center column narrower so card appears centered
        title, desc = points[i]
        with center:
            st.markdown(
                f"""
                <div class="hire-card">
                    <div class="hire-title">{title}</div>
                    <div class="hire-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        break

    # normal two-card row
    col1, col2 = st.columns(2, gap="large")
    title1, desc1 = points[i]
    title2, desc2 = points[i+1]

    with col1:
        st.markdown(
            f"""
            <div class="hire-card">
                <div class="hire-title">{title1}</div>
                <div class="hire-desc">{desc1}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="hire-card">
                <div class="hire-title">{title2}</div>
                <div class="hire-desc">{desc2}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    i += 2




# ================================
# END NOTE
# ================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center; font-size:22px; color:#FFEAEA; margin-top:25px;'>
✨ If you want someone dedicated, skilled, and focused on real results — I’m ready to work with you.
</div>
""", unsafe_allow_html=True)
