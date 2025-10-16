import streamlit as st
import requests
import base64

# Backend URL configuration
FASTAPI_URL = "http://127.0.0.1:8000"  # Change this if backend is remote

st.set_page_config(
    page_title="🧠 InsightBrain",
    layout="wide",
)

st.title("🧠InsightBrain - Research Summarizer")

# Mode selection in sidebar
mode = st.sidebar.radio("Select Mode", ["Quick Research", "Deep Research"])
st.sidebar.markdown("---")

# User input section
query = st.text_input("Enter your research topic", placeholder="e.g. Impact of AI on healthcare")
submit = st.button("🔍 Generate Summary")

if submit and query.strip():
    st.info("Fetching top sources and generating reasoning summary... ⏳")
    try:
        endpoint = "/research" if mode == "Quick Research" else "/deep_research"
        resp = requests.post(f"{FASTAPI_URL}{endpoint}", json={"query": query, "history": []})
        if resp.status_code != 200:
            st.error(f"❌ Error: {resp.text}")
        else:
            data = resp.json()
            st.success("✅ Summary generated successfully!")

            # Show source links
            with st.expander("🔗 Sources", expanded=False):
                for s in data.get("sources", []):
                    st.markdown(f"- [{s}]({s})")

            # Display analysis results
            st.subheader("🧩 Reasoning Summary")
            st.write(data["reasoning_summary"])

            st.subheader("✅ Fact Consistency Check")
            st.write(data["fact_consistency"])

            st.subheader("💡 Follow-up Questions")
            for q in data["follow_up_questions"]:
                st.markdown(f"- {q}")

            # PDF export section
            st.markdown("---")
            st.subheader("📄 Download Report")

            with st.spinner("Generating PDF..."):
                pdf_resp = requests.post(
                    f"{FASTAPI_URL}/generate_pdf",
                    json={"query": query, "report_md": data["report_md"]},
                )

            if pdf_resp.status_code == 200:
                b64_pdf = base64.b64encode(pdf_resp.content).decode("utf-8")
                href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="{query}_report.pdf">📥 Download Research Report</a>'
                st.markdown(href, unsafe_allow_html=True)
            else:
                st.error("Failed to generate PDF report.")
    except Exception as e:
        st.error(f"Error occurred: {e}")

elif submit:
    st.warning("Please enter a valid research query.")
