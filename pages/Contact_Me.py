import streamlit as st

import base64



st.markdown("""
<style>
.block-container {
    padding-top: 0.95rem !important;   
}
</style>
""", unsafe_allow_html=True)












def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


st.set_page_config(page_title="Contact Me", layout="centered")


import streamlit as st

# Remove top padding so navbar touches the top
st.markdown("""
<style>
.block-container {
    padding-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# JS → Python page switch bridge
st.markdown("""
<script>
function go(page) {
    window.parent.postMessage({type: 'streamlit:setRoute', route: page}, "*");
}
</script>
""", unsafe_allow_html=True)












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













st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_BACKGROUND_FOR_HIRING_WEB.jpg');
        background-size: cover;          /* makes it full screen */
        background-position: center;     /* centers the image */
        background-repeat: no-repeat;    /* prevents tiling */
        background-attachment: fixed;    /* stays in place while scrolling */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Background
page_bg_img = """
<style>
.contact-box, .logo-box {
    background-color: rgba(0,0,0,0.75);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    width: 380px;
    margin: auto;
    color: white;  /* ensures all text inside is white */
}
.contact-box h2 {
    color: #4EC8F4; /* Optional: make heading stand out */
}
.contact-links p {
    font-size: 18px;
    margin: 10px 0;
}
.contact-links a {
    color: #4EC8F4 !important;
    font-weight: bold;
    text-decoration: none;
}
.logo-box img {
    width: 50px;
    margin: 0 15px;
    filter: brightness(0) invert(1);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Contact Info Box
st.markdown("""
<div class="contact-box">
    <h2>📬 Contact Me</h2>
    <div class="contact-links">
        <p><b>Email:</b> <a href="mailto:y.india.main@gmail.com">y.india.main@gmail.com</a></p>
        <p><b>GitHub:</b> <a href="https://github.com/y-india" target="_blank">github.com/y-india</a></p>
        <p><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/yranaind/" target="_blank">linkedin.com/in/yranaind</a></p>
        <p><b>StreamlitCloud:</b> <a href="https://share.streamlit.io/" target="_blank">share.streamlit.io</a></p>
    </div>
</div>

<style>
.contact-box h2 {
    color: white !important;  /* make heading readable */
}
.contact-box a {
    color: #4EC8F4 !important; /* make links consistent */
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)
# Start Platforms box
st.markdown("""
<div class="logo-box">


<img src="https://cdn.simpleicons.org/gmail/ffffff" width="32">
<img src="https://cdn.simpleicons.org/github/ffffff" width="32">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg"
        width="34" style="filter: invert(1);">
<img src="https://cdn.simpleicons.org/streamlit/ffffff" width="32">
""", unsafe_allow_html=True)




