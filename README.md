

  <h1>📱 Teen Phone Addiction Predictor</h1>

  <p>
    This project is a machine learning-powered web application that predicts a teen's smartphone addiction level 
    (<strong>Low, Medium, or High</strong>) based on key behavioral and device usage inputs. 
    It leverages a logistic regression model trained on a reduced feature set of the most impactful indicators 
    (e.g., screen time, sleep hours, app usage).
  </p>

  <h2>🔍 Key Features</h2>
  <ul>
    <li>Predicts addiction levels with a streamlined input form</li>
    <li>Built using Streamlit for an interactive user interface</li>
    <li>Logistic Regression model trained on clean, bin-labeled data</li>
    <li>Focused on explainability and user-friendly UX</li>
  </ul>

  <h2>🚀 Demo</h2>
  <p>To launch the app locally:</p>
  <pre><code>streamlit run app.py</code></pre>
  <p>Make sure the following files are in the same directory:</p>
  <ul>
    <li><code>app.py</code> — the Streamlit interface</li>
    <li><code>train_model.py</code> — script to preprocess, train, and save model/scaler</li>
    <li><code>teen_phone_addiction_dataset.csv</code> — your dataset</li>
    <li><code>logistic_regression_addiction_model.pkl</code> — saved trained model</li>
    <li><code>scaler.pkl</code> — saved StandardScaler used for input preprocessing</li>
  </ul>

  <h2>⚙️ Dependencies</h2>
  <p>Install the required libraries using:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  

  <h2>📊 Dataset</h2>
  <p>The dataset includes behavioral, academic, and phone usage patterns of teens. The <code>Addiction_Level</code> column is binned into three categories:</p>
  <ul>
    <li><strong>Low</strong> (0–3.5)</li>
    <li><strong>Medium</strong> (3.6–7.5)</li>
    <li><strong>High</strong> (7.6–10)</li>
  </ul>

  <h2>📌 Project Structure</h2>
  <pre><code>📁 Teen Phone Addiction Predictor/
├── app.py
├── train_model.py
├── teen_phone_addiction_dataset.csv
├── logistic_regression_addiction_model.pkl
├── scaler.pkl
└── README.md</code></pre>


</body>
</html>
