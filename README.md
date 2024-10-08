# TranslaBot Translation Chatbot (assignment)

This python application is a translation tool that uses Streamlit for the frontend and LangChain framework for the translation functionality. It allows users to translate text from English to multiple languages. The application also includes monitoring capabilities using Prometheus to track translation response times.


In order to know more details about the solutions, please go the [Provided solutions](#provided-solutions) section below.


## Document Descriptions
- **bc_evaluation_notebook.pdf/ipynb**: contains the translation application evaluation methodology description and analysis
- **brokerchooser_AI_developments.pdf**: contains the AI product ideas
- **README.md**: project description and languages cost optimization answer

## Getting Started

### Prerequisits

- **Python 3.10.10**: Ensure you have Python 3.10.10 installed on your machine.
- **Docker**: Docker is required to run the PostgreSQL database in a container.
- **OpenAI API key**: In order to use the chatmodel

<br>


⚠️ **Important:** Before running the Docker build, ensure that a valid OpenAI API key is inserted in the `.env` file.

   ```sh
   [OpenAI]
        OPENAI_API_KEY='...YOUR API KEY GOES HERE...'
   ```

### Building the Docker Image

1. Open a terminal and navigate to the project directory.

2. Build the Docker image using the following command:

   ```sh
   docker build -t translator-app .
   ```

### Running the Docker Container

1. Run the Docker container using the following command:

   ```sh
   docker run -p 8501:8501 translator-app
   ```
   
2. Open a web browser and go to `http://localhost:8501` to access the application.
3. Select a language in the dropwdown menu and write a text to be translated in the chat window.

4. In order to get latency monitoring data run the following curl command:

    ```sh
   curl localhost:8501/_stcore/metrics
   ```

## Application Usage

1. Open the application in your web browser at `http://localhost:8501`.
2. Select a language from the dropdown menu.
3. Enter the text you want to translate in the text area and press <kbd>Enter</kbd> to get the translation.


## Provided solutions

This translation application leverages several advanced technologies to provide a seamless user experience. The frontend is built using Streamlit, which allows for an interactive and user-friendly web interface. For the translation functionality, the application utilizes OpenAI's ChatGPT, integrated through the LangChain framework. Given the simplicity of this solution, a more complex tool like LangGraph was deemed unnecessary. Instead, a basic chain with straightforward chain-of-thought prompting is employed.

For monitoring, Prometheus is used to track key performance metrics. While LangSmith would be ideal for monitoring LLMs, especially during the testing phase, it requires a paid API key and was therefore omitted. The data collected by Prometheus can be visualized using various tools, with Grafana being one of the preferred options due to its robust visualization capabilities.

> **Write a paragraph on how we should pick and prioritize languages to optimize our costs.**

To optimize costs associated with language translations, I recommend a structured approach based on profitability and usage metrics. The following steps outline our strategy:

1. **Profit/Cost Analysis**: Conduct a monthly or quarterly analysis to determine which language translations generate the most profit. Rank the languages based on their profitability.
2. **Usage Analysis**: Perform a monthly or quarterly study to identify the most frequently used languages. Rank the languages based on their usage.
3. **Scoring System**: Develop a scoring system that combines the results of the profit/cost and usage analyses. This scoring system will guide business strategy decisions.
4. **Categorization**: Based on the scoring system, categorize languages into three priority levels: high, medium, and low.
   - **High Priority**: Languages critical to business success and strategic goals.
   - **Medium Priority**: Important languages that are not critical.
   - **Low Priority**: Languages with lower importance and impact.
5. **Strategy Assignment**: Define and assign specific strategies for each priority group to optimize costs and performance.

#### Example Strategies

- **Alpha_XXL Strategy** (High Priority Languages):
  - Live translation using the best-performing LLM model.
  - Enhanced prompts for the most precise and comprehensive translations.

- **Beta Strategy** (Medium Priority Languages):
  - Live translation using a cost-effective LLM model (either an external API service or a self-hosted smaller model).
  - Prompts designed to enforce brevity, reducing token usage and costs.

- **Gamma Strategy** (Low Priority Languages):
  - Offline translation using a small LLM model with Retrieval-Augmented Generation (RAG) for question and answer.

#### Additional Options

1. **RAG for Previous Answers**: Store and reuse previous questions and answers to reduce redundant translations.
2. **Open Source Models**: Host open-source or very small models to handle translations for low-priority languages.

By implementing this structured approach, we can effectively manage and optimize translation costs while ensuring that business-critical languages receive the necessary resources and attention.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.com/)
- [Prometheus](https://prometheus.io/)


## Author/Connect

[zs.lorant@gmail.com](zs.lorant@gmail.com)
