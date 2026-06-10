import streamlit as st
import pandas as pd
from src.mock_ai import process_issue_with_mock_ai
from src.database_manager import initialize_database, insert_issue, get_all_issues

# Ensure the database table exists right when the webpage loads
initialize_database()

# Set up clean web browser tab configurations
st.set_page_config(page_title="CoreFlow AI Pipeline", page_icon="⚙️", layout="wide")

# Dashboard Header Layout
st.title("⚙️ CoreFlow AI: Automated Triage Middleware")
st.markdown("""
This production-grade portfolio pipeline captures unstructured human conversational logs, 
processes them via processing logic layers, and systematically commits them into an indexed SQL Database.
""")

st.write("---")

# Split the screen into two clean operational columns
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("📥 Ingest Chaotic Client Data")
    st.caption("Simulate a panicked email, bug report, or service ticket below:")
    
    # Text input box for the user/client to test
    user_input = st.text_area(
        label="Raw Conversational Log String",
        value="Our mobile navigation layout is completely broken on Safari! The links overlap and it looks horrible. Please add a fix asap.",
        height=150
    )
    
    # Process Button
    if st.button("Execute Pipeline Triage", type="primary"):
        if user_input.strip() == "":
            st.warning("Please type some log text to run the pipeline.")
        else:
            with st.spinner("Executing pipeline layers..."):
                # 1. Run the data through our simulation brain
                ai_results = process_issue_with_mock_ai(user_input)
                
                # 2. Commit the clean result directly to our SQLite DB
                insert_issue(user_input, ai_results)
                
                st.success("Pipeline Executed Successfully!")
                
                # Display the extracted JSON fields on screen beautifully
                st.json(ai_results)

with col2:
    st.subheader("🗄️ Real-Time Relational SQL Log Warehouse")
    st.caption("This view reads directly from our live 'project_issues' table:")
    
    # Fetch data straight out of our SQL table
    raw_db_data = get_all_issues()
    
    if raw_db_data:
        # Convert raw SQL data into a beautiful, interactive visual dataframe table
        df = pd.DataFrame(
            raw_db_data, 
            columns=["ID", "Original Text Input", "Category Tag", "Priority Rank", "Clean Summary Log", "Timestamp"]
        )
        # Display the table on the web app
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("The SQL database is currently empty. Execute a triage entry on the left to populate rows!")