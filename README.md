Prerequisites
Make sure that Python 3.10 or above installed on your machine.
Download and Install Pip to manage project packages.
Create an OpenAI account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the OpenAI website and navigating to the API Key management page.
(Optional): if you use Rainforest API as a data source, create an Rainforest account and get a new API Key. Refer to Rainforest API documentation.
Then, follow the easy steps to install and get started using the sample app.

Step 1: Clone the repository
This is done with the git clone command followed by the URL of the repository:

git clone https://github.com/Boburmirzo/chatgpt-api-python-sales.git
Next, navigate to the project folder:

cd chatgpt-api-python-sales
Step 2: Set environment variables
Create .env file in the root directory of the project, copy and paste the below config, and replace the {OPENAI_API_KEY} configuration value with your key.

OPENAI_API_TOKEN={OPENAI_API_KEY}
HOST=0.0.0.0
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
Optionally, you change other values. By default, the app uses Mock API response to simulate the response from Rainforest API. If you need actual data, you need to specify also {RAINFOREST_BASE_URL} and {RAINFOREST_API_KEY}.

RAINFOREST_BASE_URL={RAINFOREST_BASE_URL}
RAINFOREST_API_KEY={RAINFOREST_API_KEY}
Step 3: Install the app dependencies
Install the required packages:

pip install --upgrade -r requirements.txt
Step 4 (Optional): Create a new virtual environment
Create a new virtual environment in the same folder and activate that environment:

python -m venv pw-env && source pw-env/bin/activate
Step 5: Run and start to use it
You start the application by navigating to llm_app folder and running main.py:

python main.py
Step 6: Run Streamlit UI for file upload
You can run the UI separately by navigating to cd examples/ui and running Streamlit app streamlit run app.py command. It connects to the Discounts backend API automatically and you will see the UI frontend is running http://localhost:8501/ on a browser:
