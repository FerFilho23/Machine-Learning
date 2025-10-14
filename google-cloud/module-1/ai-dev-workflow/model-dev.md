# 📘 Model Development on Google Cloud  

## 🎯 Learning Objectives  
- Understand the **model development stage** of the ML workflow: training and evaluation.  
- Learn how to configure **training objectives**, **target columns**, and **training options** in Vertex AI.  
- Explore **evaluation metrics** such as confusion matrix, recall, and precision.  
- Understand how **feature importance** and **explainable AI** help interpret model results.  

---

## 📝 Summary  

The **model development** stage is the **second phase** of the ML workflow — where data becomes a working model.  
Using the cooking analogy:  
- **Data preparation** = collecting ingredients.  
- **Model training** = cooking the recipe.  
- **Model evaluation** = tasting and adjusting for quality.  

Model development is an **iterative process** of training, evaluating, and refining.  

---

## ⚙️ Step 1: Model Training  

When training a model in **Vertex AI**, you must define:  
1. **Training Method**  
   - Choose **AutoML** (no-code) or **Custom Training** (code-based).  
   - Specify the **dataset** prepared during the data preparation stage.  

2. **Training Objective**  
   - Based on data type:  
     - **Tabular:** Regression, Classification, Forecasting.  
     - **Image:** Object detection, Classification, Segmentation.  
     - **Text:** Sentiment analysis, Entity extraction, Classification.  
     - **Video:** Action recognition, Object tracking.  

3. **Training Details**  
   - Choose the **target column** (label) for supervised learning.  
   - Select which features to include or transform.  
   - Set the **training budget** and start the training job.  

**AutoML** automatically runs experiments with thousands of model architectures using two powerful technologies:  
- **Neural Architecture Search (NAS):** Tests multiple architectures to find the best-performing models.  
- **Transfer Learning:** Leverages pre-trained models to improve accuracy and reduce training time.  

---

## ⚙️ Step 2: Model Evaluation  

Once trained, the model’s performance must be evaluated using **quantitative metrics**.  
Vertex AI provides built-in evaluation visualizations and metrics — particularly for **classification tasks**.  

### 🔹 Confusion Matrix  
A confusion matrix shows the relationship between **predicted** and **actual** outcomes.  

| Prediction | Actual Positive | Actual Negative |
|-------------|----------------|----------------|
| **Predicted Positive** | True Positive (TP) | False Positive (FP, Type I error) |
| **Predicted Negative** | False Negative (FN, Type II error) | True Negative (TN) |

- **True Positive (TP):** Model correctly predicts a positive case.  
- **True Negative (TN):** Model correctly predicts a negative case.  
- **False Positive (FP):** Model incorrectly predicts positive.  
- **False Negative (FN):** Model incorrectly predicts negative.  

### 🔹 Key Metrics  

- **Recall (Sensitivity):**  
  Measures how many actual positives were correctly predicted.  
  \[
  Recall = TP / (TP + FN)
  \]  
  > Example: Catching 80 of 100 fish → Recall = 80%.  

- **Precision:**  
  Measures how many predicted positives were actually correct.  
  \[
  Precision = TP / TP + FP
  \]  
  > Example: If 80 fish and 80 rocks were caught → Precision = 50%.  

**Trade-off:**  
- High **recall** = more positives caught, but more false alarms.  
- High **precision** = fewer false positives, but might miss some true positives.  

### 🧪 Imagine: You’re a Medical Test for Detecting a Disease
| Term | 	What it Measures | Intuitive Question |
|-------------|----------------|----------------|
| **Precision** | "Of all the patients you said are sick, how many are actually sick?" | “When I say someone is sick, how often am I right?” |
| **Recall** | Of all the patients who are truly sick, how many did I detect? | “Did I catch all the sick people?” |


### 🧠 Another Way to Think About It
- **Precision**:	Being careful — don’t make false accusations. (avoiding false positives)
- **Recall**:	Being thorough — catch every possible case. (avoiding false negatives)

### 📊 Example

Let’s say there are 100 actual sick people, and your model predicts 20 people as sick,
but only 10 of those 20 are really sick.

Precision = 10 / 20 = 0.5 → 50% of your alarms are correct.

Recall = 10 / 100 = 0.1 → You caught only 10% of all sick people.

So:

- You’re precise only if your alerts are reliable.

- You have high recall only if you don’t miss many true cases.

---

## 🔎 Feature Importance & Explainable AI  

**Feature Importance:**  
- Displays how much each feature contributes to model predictions.  
- Shown as a **bar chart** in Vertex AI.  
- Longer bars = greater predictive influence.  
- Helps determine which features to keep or remove for optimization.  

**Explainable AI (XAI):**  
- A suite of tools in Vertex AI to **interpret model predictions**.  
- Enhances **transparency and trust** in ML models.  
- Supports regulatory and ethical AI practices.  

---

## 💡 Key Insights  
- Model development is an **iterative experiment cycle**: train → evaluate → refine.  
- **AutoML** simplifies training by automating model selection and tuning.  
- **Recall and Precision** measure model effectiveness and trade-offs.  
- **Feature Importance** and **Explainable AI** improve model interpretability.  
- A good model is not just accurate — it’s **understandable, monitored, and continuously improved**.  

---

## 📚 References  
- [Vertex AI Model Training](https://cloud.google.com/vertex-ai/docs/training/overview)  
- [Model Evaluation in Vertex AI](https://cloud.google.com/vertex-ai/docs/evaluation/introduction)  
- [Explainable AI on Google Cloud](https://cloud.google.com/explainable-ai)  
