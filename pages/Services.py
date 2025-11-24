import json
import os
import streamlit as st






def save_request_to_json(data, filename="client_requests.json"):
    """Append a new client request to a JSON file."""
    # Check if file exists
    if os.path.exists(filename):
        # Load existing data
        with open(filename, "r", encoding="utf-8") as f:
            try:
                all_requests = json.load(f)
            except json.JSONDecodeError:
                all_requests = []
    else:
        all_requests = []

    # Append new request
    all_requests.append(data)

    # Save back to file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_requests, f, indent=4, ensure_ascii=False)












st.set_page_config(page_title="Services", page_icon="🛠️", layout="wide")

# --- Initialize session state ---
if "selected_service" not in st.session_state:
    st.session_state.selected_service = None

# --- Top padding adjustment ---
st.markdown("""
<style>
.block-container {
    padding-top: 0.95rem !important;   
}
</style>
""", unsafe_allow_html=True)

# --- Background image ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://raw.githubusercontent.com/y-india/images_hosting/refs/heads/main/SELECTED_BACKGROUND_FOR_HIRING_WEB.jpg");
    background-size: cover;
} 
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)






st.markdown("""
<style>
.service-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.25);
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    color: #E0E7FF;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
    transition: 0.25s ease;
    cursor: pointer;
    margin-bottom: 25px;
    width: 100%;
}
.service-btn:hover {
    transform: translateY(-4px) scale(1.02);
    background: rgba(255,255,255,0.20);
    border-color: rgba(255,255,255,0.45);
    box-shadow: 0 0 18px rgba(255,215,0,0.8), 
                0 0 28px rgba(255,215,0,0.5); /* yellow glow */
}
</style>
""", unsafe_allow_html=True)






# --- Navbar ---
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

# --- Page title ---
st.markdown(
    "<h1 style='text-align:center; color:#E0E7FF;'>🛠️ Our Services 🛠️</h1>",
    unsafe_allow_html=True
)













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
        fontcolor="#FFD700",
        fontsize=10,
        fontname="Helvetica-Bold"
    ];

    Step1 [label="🖱️ Step 1\nClick on Service You Want"];
    Step2 [label="✏️ Step 3\nFill Out the Project Form"];
    Step3 [label="📤 Step 4\nSubmit Request"];
    Step4 [label="⏰ Step 5\nReceive Response Within 6 Hours"];

    Step1 -> Step2 [color="#FFD700", penwidth=2];
    Step2 -> Step3 [color="#FFD700", penwidth=2];
    Step3 -> Step4 [color="#FFD700", penwidth=2];
}
""", use_container_width=True)



st.markdown("""
            <br>
            """, unsafe_allow_html=True)




services = [
    "Streamlit Web App Development",
    "Machine Learning Project Assistance",
    "OpenCV Automation / Project Development",
    "Python Data Cleaning",
    "Python Data Analysis",
    "Data Visualization Dashboard",
    "Portfolio Website Development",
    "Academic Support / Notes / Teaching",
    "Full ML Project + Streamlit Deployment + Report",
    "Custom / Other Request"
]

st.markdown("""
<style>
.service-btn {
    display: block;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.25);
    text-align: center;
    font-size: 20px;
    color: #E0E7FF;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
    text-decoration: none;
    transition: 0.25s ease;
    margin-bottom: 15px;
}
.service-btn:hover {
    transform: translateY(-4px) scale(1.02);
    background: rgba(255,255,255,0.20);
    border-color: rgba(255,255,255,0.45);
    box-shadow: 0 0 18px rgba(129,176,255,0.8), 0 0 28px rgba(129,176,255,0.5);
}
</style>
""", unsafe_allow_html=True)

# Display services as clickable links to form page
for service in services:
    # URL encode the service name for query params
    service_param = service.replace(" ", "%20")
    st.markdown(
        f"<a href='/Service_Form?service={service_param}' class='service-btn' target='_self'>{service}</a>", 
        unsafe_allow_html=True
    )

