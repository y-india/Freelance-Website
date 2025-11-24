# app.py
import streamlit as st



st.markdown("""
<style>
/* Navbar container */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(10px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 50px;
    font-family: 'Helvetica', sans-serif;
    border-bottom: 1px solid rgba(80,150,255,0.35);
}

/* Navbar links */
.navbar a {
    color: #BFD7FF;
    text-decoration: none;
    margin-left: 25px;
    font-weight: 600;
    transition: 0.3s;
}

.navbar a:hover {
    color: #E8F1FF;
    transform: scale(1.05);
}

/* Left section */
.navbar .left {
    font-size: 18px;
    font-weight: 700;
    color: #FFD700;
}

/* Right links section */
.navbar .right {
    display: flex;
    align-items: center;
    font-size: 16px;
}
</style>

<div class="navbar">
    <div class="left">
       👀 MUST VISIT 🔥 ➡ 
    </div>
    <div class="right">
        <a href="https://yuvirana.streamlit.app" target="_blank">Portfolio</a>
        <a href="https://github.com/y-india" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/yranaind" target="_blank">LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)




st.markdown(
    """
<style>

.tile {
    background: rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(12px);
    padding: 45px 20px;
    border-radius: 20px;
    border: 1px solid rgba(80,150,255,0.35);
    text-align: center;
    font-size: 26px;
    font-weight: 600;
    color: #BFD7FF;
    text-decoration: none;
    transition: 0.3s ease;
    box-shadow: 0 0 18px rgba(80,150,255,0.35);
}

.tile:hover {
    box-shadow: 0 0 15px rgba(100,170,255,0.7);
    transform: translateY(-6px);
    border-color: #4D8BFF;
    color: #E8F1FF;
}

</style>
""",
    unsafe_allow_html=True,
)









st.markdown("""
<style>
/* Remove default Streamlit top padding */
section.main > div {
    padding-top: 0rem !important;
}

/* Remove padding from the main app container */
[data-testid="stAppViewContainer"] {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

/* Remove padding around blocks */
.block-container {
    padding-top: 0 !important;
    margin-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)




















st.markdown("""
<style>
/* Hide Streamlit top header */
header[data-testid="stHeader"] {
    display: none !important;
}

/* Remove extra space Streamlit leaves behind */
div.block-container {
    padding-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)















st.set_page_config(page_title="Yuvraj — AI/ML & Streamlit Services", layout="wide")
# --- GLOBAL BOX STYLE ---
box_style = """
<style>
.title-box {
    background: rgba(0,0,0,0.25);  /* lighter glass for title */
    backdrop-filter: blur(10px);    /* subtle blur */
    padding: 30px 35px;
    border-radius: 22px;

    /* remove all borders/glow */
    border: none;
    box-shadow: none;

    text-align: center;
    margin-top: -40px !important;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}
</style>
"""


st.markdown(box_style, unsafe_allow_html=True)



page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_BACKGROUND_FOR_HIRING_WEB.jpg");
    background-size: cover;
}} 
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)



# ---- Title Section ----





st.markdown(
    """
<div class="title-box">
<h1 style="
    font-size: 36px;
    color: #E0E7FF;
    margin-bottom: -10px;
    font-weight: 700;
    letter-spacing: -1px;
">
    Yuvraj — AI/ML Engineer & Streamlit App Developer
</h1>

<p style="
    font-size: 15px;
    color: #BFC7D9 ;
    margin-top: 10px;
">
    I build simple, fast and affordable AI tools, ML models, automation scripts and Streamlit web apps.
</p>
</div>
""",
    unsafe_allow_html=True,
)






st.markdown("""
            <br>
            """ , unsafe_allow_html=True)




# chat strture
st.graphviz_chart("""
digraph G {
    bgcolor="transparent";
    rankdir=LR;
    ratio=fill;
    nodesep=1.2;
    ranksep=1.0;

    node [
        shape=box,
        style=filled,
        fillcolor="transparent",
        color="#4D8BFF",
        fontcolor="#B22222",
        fontsize=10,
        fontname="Helvetica-Bold"
    ];

    Step1 [label="Step 1\nChoose a Service"];
    Step2 [label="Step 2\nFill Out the Project Form"];
    Step3 [label="Step 3\nSubmit Request"];
    Step4 [label="Step 4\nReceive Reply in 6 Hours"];

    Step1 -> Step2 [color="#FF6F61", penwidth=2];
    Step2 -> Step3 [color="#FF6F61", penwidth=2];
    Step3 -> Step4 [color="#FF6F61", penwidth=2];
}
""", use_container_width=True)


# Title: #E0E7FF
# Subtitle: #BFC7D9
# Accents: #4D8BFF
# Glow/Highlight: #8AB4FF

















st.markdown(
    """
<style>

.grid-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 25px;
    width: 100%;
    max-width: 1100px;
    margin: 40px auto 0;
}

/* Top center tile */
.grid-container .center {
    grid-column: 1 / span 2;
    justify-self: center;
    width: 70%;
}

/* Tile design */
.tile {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    padding: 45px 20px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.18);
    text-align: center;
    font-size: 26px;
    font-weight: 600;
    color: #E0E7FF;
    text-decoration: none;
    transition: 0.25s ease;
    box-shadow: 0 6px 28px rgba(0,0,0,0.45);
}

.tile:hover {
    background: rgba(255,255,255,0.22);
    border-color: rgba(255,255,255,0.35);
    transform: translateY(-6px);
}

</style>
<div class="grid-container">
    <a class="tile" href="/Services" target="_self">Service You Want</a>
    <a class="tile" href="/My_Skills" target="_self">My Skills</a>
    <a class="tile" href="/Why_Hire_Me" target="_self">Why Hire Me ?</a>
    <a class="tile" href="/Contact_Me" target="_self">Contact Me</a>
</div>
""",
    unsafe_allow_html=True,
)


