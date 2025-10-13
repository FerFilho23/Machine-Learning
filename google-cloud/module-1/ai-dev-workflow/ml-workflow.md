# 📘 Machine Learning Workflow on Google Cloud  

## 🎯 Learning Objectives  
- Understand the **three main stages** of the ML workflow: data preparation, model development, and model serving.  
- Recognize that the ML workflow is **iterative**, not linear.  
- Learn how **Vertex AI** supports both **no-code (AutoML)** and **code-based (Pipelines)** workflow setups.  
- Identify how **MLOps** automates workflow stages for continuous improvement.  

---

## 📝 Summary  

Building a machine learning model follows a process similar to **serving food in a restaurant**:  
- You start by **preparing ingredients** (data).  
- Then you **experiment with recipes** (model development).  
- Finally, you **serve the meal** (deploy and monitor the model).  

In Google Cloud, this process is implemented with **Vertex AI**, which organizes ML development into three main stages.  

---

## ⚙️ The Three Stages of the ML Workflow  

### 1. **Data Preparation**  
- Involves **data uploading** and **feature engineering**.  
- The **quality and quantity** of data determine model performance.  
- Data can be:  
  - **Real-time streaming** or **batch** data.  
  - **Structured** (tables, text, numbers) or **unstructured** (images, videos).  
- Data preparation ensures that models have **clean, relevant, and usable inputs**.  

---

### 2. **Model Development**  
- Involves **training and evaluation** in an **iterative cycle**.  
- Models are trained, evaluated, and retrained repeatedly to improve performance.  
- Selecting the right architecture, hyperparameters, and evaluation metrics is key.  

---

### 3. **Model Serving**  
- The trained model is **deployed into production** to make real predictions.  
- Continuous **monitoring** ensures reliability and performance.  
- Models must be updated as new data arrives or performance drifts (known as **data drift**).  
- Without deployment, a model remains **theoretical** and has no real business value.  

---

## 🔁 The Iterative Nature of ML Workflows  
- ML workflows are **not linear** — they require constant feedback loops.  
- During training, new features might need to be engineered.  
- During serving, **monitoring** may reveal model degradation, prompting retraining.  
- **MLOps** automates this iteration, enabling continuous integration, delivery, and training (CI/CD/CT).  

---

## 🧰 Workflow Options in Vertex AI  

### **Option 1 — AutoML (No-Code Solution)**  
- Build and train models through an intuitive **UI**.  
- Ideal for users without coding or ML experience.  
- Handles preprocessing, model selection, and deployment automatically.  

### **Option 2 — Vertex AI Pipelines (Code-Based Solution)**  
- Programmatically build end-to-end ML workflows.  
- Uses **SDKs and APIs** to define and automate pipeline steps.  
- Suitable for **ML engineers and data scientists** who prefer coding and automation.  
- Typically executed in **Vertex AI Workbench** or **Colab Enterprise**.  

---

## 💡 Key Insights  
- The **three stages (data → model → deployment)** form the backbone of every ML project.  
- ML workflows are **cyclical**, requiring constant iteration and monitoring.  
- **Vertex AI** simplifies both **no-code** and **custom-code** workflows.  
- **MLOps** ensures automation, scalability, and production reliability.  

---

## 📚 References  
- [Vertex AI Overview](https://cloud.google.com/vertex-ai)  
- [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines)  
- [MLOps on Google Cloud](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)  
