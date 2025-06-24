# plantuml_app.py

import streamlit as st
import requests
import os

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="PlantUML Renderer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PlantUML Server Configuration ---
plantuml_server_url = os.environ.get('PLANTUML_SERVER_URL', 'http://localhost:8080')

# Ensure it does not end with a slash
plantuml_server_url = plantuml_server_url.rstrip('/')

# Endpoint for POST requests (accepts raw PlantUML code)
render_endpoint = f"{plantuml_server_url}/form"

st.sidebar.info(f"Using PlantUML server: `{plantuml_server_url}`")

# --- UI ---
st.title("🌱 PlantUML Renderer (POST-based)")
st.markdown("Enter your PlantUML code below and click **Render Diagram** to visualize it.")

default_plantuml_code = """
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
Alice -> Bob: Another request
Alice <-- Bob: Another response
@enduml
"""

plantuml_code = st.text_area(
    "PlantUML Code",
    default_plantuml_code,
    height=300,
    help="Enter your PlantUML syntax here. For more information, visit https://plantuml.com/."
)

# --- Render Diagram ---
if st.button("Render Diagram", use_container_width=True):
    if plantuml_code.strip() == "":
        st.warning("Please enter some PlantUML code to render.")
    else:
        st.subheader("Rendered Diagram")
        with st.spinner("Rendering diagram..."):
            try:
                response = requests.post(
                    f"{plantuml_server_url}/png",
                    data=plantuml_code.encode("utf-8"),
                    headers={"Content-Type": "text/plain"}
                )

                if response.status_code == 200 and response.headers["Content-Type"].startswith("image"):
                    st.image(response.content, caption="Generated PlantUML Diagram", use_column_width=True)
                else:
                    st.error(f"Unexpected response from server (status {response.status_code}).")
                    st.code(response.text[:500], language='html')

            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to PlantUML server at {plantuml_server_url}: {e}")

# --- Instructions ---
st.markdown("---")
st.markdown(
    """
    **How to use:**
    1. Start your PlantUML Docker container:
        ```bash
        docker run -p 8080:8080 plantuml/plantuml
        ```

    2. Save this code as `plantuml_app.py`.

    3. Install required libraries:
        ```bash
        pip install streamlit requests
        ```

    4. Run the app:
        ```bash
        streamlit run plantuml_app.py
        ```

    You can override the PlantUML server URL with:
    ```bash
    export PLANTUML_SERVER_URL=http://localhost:8080
    ```
    """
)
st.markdown("For more examples, visit [plantuml.com/examples](https://plantuml.com/examples).")
