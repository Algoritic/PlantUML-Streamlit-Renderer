# 🌱 PlantUML Streamlit Renderer

This project provides a simple yet powerful web application built with Streamlit that allows you to render PlantUML diagrams. It's designed to be a demo and template for integrating PlantUML with Python web applications, particularly useful for visualizing diagrams without needing local PlantUML installations beyond a Docker container.

The application uses a self-hosted PlantUML server (via Docker) to convert PlantUML code into visual diagrams (PNG images).

## ✨ Features

* **Interactive Editor**: Type or paste your PlantUML code directly into the web interface.
* **Live Rendering**: Instantly see your diagrams rendered as you click the "Render Diagram" button.
* **Docker Integration**: Easily set up the PlantUML rendering server using Docker.
* **Environment Variable Configuration**: Customize the PlantUML server URL via an environment variable.

## 🚀 Getting Started

Follow these steps to get your PlantUML Streamlit Renderer up and running.

### Prerequisites

Before you begin, ensure you have the following installed:

* [**Docker**](https://docs.docker.com/get-docker/): For running the PlantUML server.
* [**Python 3.8+**](https://www.python.org/downloads/): For running the Streamlit application.
* [**pip**](https://pip.pypa.io/en/stable/installation/): Python package installer.

### Local Setup (Manual)

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/plantuml-streamlit-renderer.git](https://github.com/your-username/plantuml-streamlit-renderer.git)
    cd plantuml-streamlit-renderer
    ```
    (Remember to replace `your-username` with your actual GitHub username)

2.  **Start the PlantUML Server**:
    The application relies on a running PlantUML server. You can easily start one using Docker:
    ```bash
    docker run -d -p 8080:8080 --name plantuml-server plantuml/plantuml
    ```
    This command starts a PlantUML server in the background, accessible at `http://localhost:8080`.

3.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit App**:
    ```bash
    streamlit run plantuml_app.py
    ```

    The Streamlit application will open in your web browser, usually at `http://localhost:8501`.

### Local Setup (Using Docker Compose)

For an even easier setup, you can use `docker-compose` to run both the PlantUML server and the Streamlit application.

1.  **Clone the Repository** (if you haven't already):
    ```bash
    git clone [https://github.com/your-username/plantuml-streamlit-renderer.git](https://github.com/your-username/plantuml-streamlit-renderer.git)
    cd plantuml-streamlit-renderer
    ```

2.  **Build and Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    This command will:
    * Build the Streamlit application Docker image.
    * Start the PlantUML server container.
    * Start the Streamlit application container.
    * The Streamlit app will be available at `http://localhost:8501`.

    To run in detached mode (in the background):
    ```bash
    docker-compose up -d --build
    ```

    To stop the services:
    ```bash
    docker-compose down
    ```

## ⚙️ Configuration

The PlantUML server URL can be configured using the `PLANTUML_SERVER_URL` environment variable.

By default, the application assumes the PlantUML server is running at `http://localhost:8080`. If your server is hosted elsewhere, you can set this variable:

```bash
export PLANTUML_SERVER_URL="http://your-plantuml-server-ip:port"
streamlit run plantuml_app.py
```
