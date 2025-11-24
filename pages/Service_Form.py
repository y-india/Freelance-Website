import streamlit as st
import json
import os

st.markdown("""
<style>
.block-container {
    padding-top: 3rem !important;   
}

/* Proofs Navbar */
.proof-nav {
    width: 100vw;
    padding: 14px 0;
    margin: 20px 0 0 0; /* push down from top */
    background: rgba(20,20,30,0.85);
    backdrop-filter: blur(20px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 30px;
    border-bottom: 1px solid rgba(80,200,255,0.25);
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    z-index: 999;
}

/* Proof links on the left */
.proof-links {
    display: flex;
    gap: 22px;
}

.proof-btn {
    color: #80D4FF !important;
    font-size: 14px;
    font-weight: 600;
    padding: 6px 16px;
    border-radius: 8px;
    background: rgba(0,50,80,0.25);
    border: 1px solid rgba(80,200,255,0.25);
    transition: 0.22s ease;
    text-decoration: none;
}

.proof-btn:hover {
    background: rgba(0,150,255,0.2);
    border-color: rgba(0,200,255,0.45);
    box-shadow: 0 0 12px rgba(0,200,255,0.45);
    transform: translateY(-1px);
}

/* Right message */
.proof-msg {
    color: #80D4FF;
    font-size: 16px;
    font-weight: 700;
}
</style>

<div class="proof-nav">
    <div class="proof-links">
        <a class="proof-btn" href="https://yuvirana.streamlit.app" target="_blank">✦ Portfolio </a>
        <a class="proof-btn" href="https://github.com/y-india" target="_blank">✦ GitHub </a>
        <a class="proof-btn" href="https://www.linkedin.com/in/yranaind" target="_blank">✦ LinkedIn </a>
    </div>
    <div class="proof-msg"> 🢀 Proof of Service You Want </div>
</div>
""", unsafe_allow_html=True)






























st.markdown("""
<style>
.block-container {
    padding-top: 3rem !important;   
}
</style>
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
<br>""" , unsafe_allow_html=True
)

def save_request_to_json(data, filename="service_requests.json"):
    """Save form submission to a JSON file. Appends if file exists."""
    all_data = []

    # Check if file exists
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                all_data = json.load(f)
            except json.JSONDecodeError:
                all_data = []

    # Append new request
    all_data.append(data)

    # Save back to JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)


# Get query params
# Get query params (new method)
query_params = st.query_params
selected_service = query_params.get("service", [""])[0]  # default empty








if selected_service:
    st.markdown(f"### 📝 Request Form for: **{selected_service}**")

    with st.form(key="service_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        role = st.text_input("Role / Background")
        budget = st.text_input("Project Budget (in ₹)")
        deadline_options = ["1 Day", "3 Days", "1 Week", "2 Weeks", "Flexible", "Other"]
        deadline = st.selectbox("Deadline / Timeline", options=deadline_options)
        if deadline == "Other":
            deadline = st.text_input("Please specify your timeline")
        description = st.text_area("Project Description (What you want?)")
        uploaded_files = st.file_uploader("Files / Dataset (Optional)", accept_multiple_files=True)
        additional_notes = st.text_area("Any Additional Notes")

        submit_button = st.form_submit_button("Submit Request")
        if submit_button:
            request_data = {
                "service": selected_service,
                "full_name": full_name,
                "email": email,
                "role": role,
                "budget": budget,
                "deadline": deadline,
                "description": description,
                "additional_notes": additional_notes,
                "files": [f.name for f in uploaded_files] if uploaded_files else []
            }
            save_request_to_json(request_data)
            st.success("✅ Thank you! I will respond within 6 hours.")


            
elif selected_service == [""] or selected_service is None:
    st.error("Please select a service from the SERVICES.")



else:
    st.error("Please select a service from the SERVICES.")