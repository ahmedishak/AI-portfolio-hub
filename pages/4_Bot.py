import streamlit as st
import streamlit.components.v1 as components

# Expands the page to fit a dashboard layout
st.set_page_config(layout="wide") 

st.title("AI Booking Agent Architecture")

# Create two columns
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("Interactive Demo")
    components.html("""
        <iframe src="https://copilotstudio.microsoft.com/environments/7bd48057-e801-e228-8286-4504dd585749/bots/cr21c_linguistic_69MIK1/canvas?__version__=2&enableFileAttachment=false&cliAgent=true" frameborder="0" style="width: 100%; height: 500px;"></iframe>
    """, height=500)

with col2:
    st.subheader("System Architecture")
    st.image("pages/architecture.png")
    
    st.markdown("""
    **Business Impact:**
    An automated conversational pipeline that eliminates manual data entry, securely writes to a relational database, and triggers formatted stakeholder alerts.
    
    **Tech Stack:**
    * **Frontend UI:** Microsoft Copilot Studio
    * **Database:** Dataverse
    * **Event Trigger & Routing:** Power Automate
    """)
    
    with st.expander("⚙️ View Backend Data Transformation"):
        st.markdown("""
        **Overcoming OData Limitations:**
        Dataverse natively outputs raw internal IDs and unformatted server timestamps. To generate professional stakeholder alerts, I engineered custom string manipulation functions (`formatDateTime`) and queried OData metadata schemas directly via the backend:
        
        `body/cr21c_languagerequired@OData.Community.Display.V1.FormattedValue`
        """)
