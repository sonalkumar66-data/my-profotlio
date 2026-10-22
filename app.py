import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Sonal Kumar | Portfolio", page_icon="💼", layout="wide")

# ============ ADVANCED CUSTOM STYLING (DARK THEME) ============
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .stApp { background-color: #0e1117; color: #e2e8f0; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

    .hero {
        background: linear-gradient(135deg, #1e1e2f 0%, #10101a 100%);
        padding: 40px 30px; border-radius: 20px; text-align: center;
        border: 1px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 30px;
    }
    .profile-pic {
        width: 150px; height: 150px; border-radius: 50%;
        object-fit: cover; border: 4px solid #3b82f6;
        margin-bottom: 15px; box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
    }
    .hero h1 { color: #60a5fa; font-size: 40px; font-weight: 700; margin-bottom: 5px; }
    .hero h3 { color: #94a3b8; font-size: 18px; font-weight: 400; margin-bottom: 15px; }

    .metric-card {
        background: #1e293b; padding: 15px; border-radius: 12px; text-align: center;
        border-left: 4px solid #3b82f6; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .metric-card h2 { color: #60a5fa; font-size: 28px; margin: 0; font-weight: 700; }
    .metric-card p { color: #cbd5e1; font-size: 12px; margin: 5px 0 0 0; font-weight: 500; text-transform: uppercase;}

    .section-title {
        font-size: 24px; font-weight: 700; color: #f8fafc;
        border-left: 5px solid #3b82f6; padding-left: 15px; margin: 30px 0 20px 0;
    }
    .timeline-card {
        background: #1e293b; padding: 20px; border-radius: 12px;
        margin-bottom: 20px; border: 1px solid #334155;
    }
    .timeline-card h4 { color: #93c5fd; font-size: 18px; margin: 0 0 5px 0; }
    .timeline-card h5 { color: #cbd5e1; font-size: 14px; margin: 0 0 10px 0; }
    .timeline-card p, .timeline-card li { color: #94a3b8; font-size: 14px; line-height: 1.6; }

    .skill-tag {
        display: inline-block; background: rgba(59, 130, 246, 0.15); color: #60a5fa;
        padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600;
        margin: 0 8px 8px 0; border: 1px solid rgba(59, 130, 246, 0.3);
    }
    .custom-btn {
        display: inline-block; padding: 10px 25px; font-size: 15px; font-weight: 600;
        color: white; background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        border-radius: 30px; text-decoration: none; margin: 10px 5px;
    }
</style>
""", unsafe_allow_html=True)

# ============ DATA ============
MY_INFO = {
    "name": "SONAL KUMAR",
    "role": "Data Analyst | Power BI Specialist | MIS Executive",
    "location": "Noida, Uttar Pradesh, India",
    "email": "sonalkumar660446@gmail.com",
    "phone": "+91-8579932774",
    "linkedin": "https://www.linkedin.com/in/sonal-kumar-1b1b77324",
    "resume_link": "https://drive.google.com/file/d/1lUwL0QyPOYhK7kcL63QYLuylSsgSXKY0/view?usp=drivesdk"
}

# ============ HERO SECTION ============
# Yahan link mein '.png' update kar diya gaya hai aur cache hatane ke liye ?v=2 lagaya hai
st.markdown(f"""
<div class="hero">
    <img src="https://raw.githubusercontent.com/sonalkumar66-data/my-portfolio/main/profile.png?v=2" class="profile-pic" onerror="this.style.display='none'">
    <h1>{MY_INFO['name']}</h1>
    <h3>{MY_INFO['role']}</h3>
    <p style="color:#94a3b8; font-size:14px;">📍 {MY_INFO['location']} &nbsp;|&nbsp; ✉️ {MY_INFO['email']}</p>
    <div>
        <a href="{MY_INFO['resume_link']}" target="_blank" class="custom-btn">📄 Resume</a>
        <a href="{MY_INFO['linkedin']}" target="_blank" class="custom-btn" style="background: #0077b5;">💼 LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ============ METRICS ============
st.markdown('<div class="section-title">🚀 Key Impact</div>', unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-card"><h2>50K+</h2><p>Records Analyzed</p></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-card"><h2>35%</h2><p>Time Saved</p></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-card"><h2>12%</h2><p>Return Reduced</p></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-card"><h2>100%</h2><p>Data Accuracy</p></div>', unsafe_allow_html=True)

# ============ ABOUT ME ============
st.markdown('<div class="section-title">👨‍💻 About Me</div>', unsafe_allow_html=True)
st.markdown("""
<div class="timeline-card">
    <p>I am a detail-oriented Data Analyst with a strong foundation in Physics and 1 year of hands-on experience in transforming complex, multi-channel operational data into actionable business insights. I specialize in Power BI, Advanced Excel, and SQL, with a proven track record of automating reporting processes and saving over 35% of manual effort. My passion lies in building interactive dashboards that help management make data-driven decisions. Constantly exploring new technologies, I strive to enhance my data storytelling skills and drive business growth.</p>
</div>
""", unsafe_allow_html=True)

# ============ EXPERIENCE ============
st.markdown('<div class="section-title">💼 Professional Experience</div>', unsafe_allow_html=True)
st.markdown("""
<div class="timeline-card">
    <h4>MIS Executive</h4>
    <h5>Divine Trends Light Manufacturers</h5>
    <ul>
        <li>Automated daily, weekly, and monthly MIS reports using Advanced Excel to track sales orders and operational KPIs.</li>
        <li>Processed daily order entries, stock movements, and operational records across multi-channel sales systems with high accuracy.</li>
        <li>Conducted daily data verification and reconciliation checks between master data and dispatch logs to eliminate discrepancies.</li>
        <li>Tracked e-commerce (Amazon) returns, compiled SKU-wise summaries, and analyzed return trends and inventory flow.</li>
        <li>Maintained corporate Excel and Power BI dashboards, organizing raw data into clear, executive-ready operational summaries.</li>
    </ul>
</div>
<div class="timeline-card">
    <h4>Data Entry & MIS Assistant</h4>
    <h5>Dal Mill Industry</h5>
    <ul>
        <li>Managed daily inventory records and prepared production reports using Excel-based automation tracking.</li>
        <li>Recorded daily stock movements, production outputs, and warehouse transactions with 100% accuracy.</li>
        <li>Prepared weekly inventory reconciliation and production performance reports for operational planning and management review.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ============ PROJECTS ============
st.markdown('<div class="section-title">📊 Key Projects</div>', unsafe_allow_html=True)

with st.expander("Sales Performance & KPI Dashboard (Power BI)", expanded=False):
    st.markdown("* **Cleaned & Transformed:** Processed 50,000+ raw sales records using Power Query.\n* **DAX Measures:** Developed custom measures for Total Sales, MoM Revenue Growth, and Profit Margins.\n* **Impact:** Reduced manual reporting time by **35%**.")
    df1 = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Revenue": [45000, 52000, 48000, 61000, 58000, 72000]})
    fig1 = px.line(df1, x="Month", y="Revenue", markers=True, template="plotly_dark")
    fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=250)
    st.plotly_chart(fig1, use_container_width=True)

with st.expander("Customer Complaint Analytics Dashboard (Power BI)", expanded=False):
    st.markdown("* **Monitoring:** Built an interactive dashboard to monitor complaint volumes.\n* **Impact:** Applied trend analysis to identify recurring service gaps.")
    df2 = pd.DataFrame({"Category": ["Quality", "Late Delivery", "Wrong Item", "Damaged"], "Complaints": [150, 220, 80, 45]})
    fig2 = px.bar(df2, x="Category", y="Complaints", color="Complaints", color_continuous_scale="Blues", template="plotly_dark")
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=250)
    st.plotly_chart(fig2, use_container_width=True)

with st.expander("Amazon Returns & Operations Tracker (Excel MIS)", expanded=False):
    st.markdown("* **Analysis:** Analyzed returns and SKU performance across 10,000+ transactions.\n* **Impact:** Helped reduce overall return rates by **12%**.")
    df3 = pd.DataFrame({"Reason": ["Size", "Defective", "Changed Mind", "Other"], "Count": [400, 250, 200, 150]})
    fig3 = px.pie(df3, names="Reason", values="Count", template="plotly_dark", hole=0.4)
    fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=250)
    st.plotly_chart(fig3, use_container_width=True)

# ============ SKILLS & LANGUAGES ============
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="section-title">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    skills = ["Advanced Excel", "Power BI", "DAX", "Power Query", "SQL", "MIS Reporting", "Data Viz"]
    st.markdown(f'<div class="timeline-card">{"".join([f"<span class=\'skill-tag\'>{s}</span>" for s in skills])}</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="section-title">🗣️ Languages</div>', unsafe_allow_html=True)
    langs = ["English", "Hindi", "Japanese"]
    st.markdown(f'<div class="timeline-card">{"".join([f"<span class=\'skill-tag\' style=\'background:rgba(139,92,246,0.15); color:#a78bfa;\'>{l}</span>" for l in langs])}</div>', unsafe_allow_html=True)

# ============ EDUCATION ============
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
edus = [
    {"deg": "Data Analyst Certification", "inst": "Ducat IT Training", "yr": "Power BI, SQL"},
    {"deg": "B.Sc (Physics Honors)", "inst": "Magadh University", "yr": "2023"},
    {"deg": "Class 12th (CBSE)", "inst": "Manav Bharti National School", "yr": "2018 | 54%"},
    {"deg": "Class 10th (CBSE)", "inst": "Param Gyan Niketan", "yr": "2016 | 9 CGPA"}
]
for e in edus:
    st.markdown(f'<div class="timeline-card" style="padding:15px; border-left:3px solid #10b981;"><h4 style="color:#34d399; margin:0;">{e["deg"]}</h4><p style="margin:0; color:#cbd5e1; font-size:14px;">{e["inst"]} | {e["yr"]}</p></div>', unsafe_allow_html=True)
