# 📘 Model Serving on Google Cloud  

## 🎯 Learning Objectives  
- Understand the **model serving stage** of the ML workflow.  
- Learn the difference between **model deployment** and **model monitoring**.  
- Identify **deployment options**: real-time (online), batch (offline), and edge/off-cloud.  
- Recognize how **Vertex AI Pipelines** and **Workbench** help automate and manage the workflow.  

---

## 📝 Summary  

The **model serving** stage is the **final step** of the machine learning workflow — where your trained model is delivered to users and continuously monitored for performance.  

Using the cooking analogy:  
- **Data preparation** = preparing ingredients.  
- **Model development** = cooking the meal.  
- **Model serving** = serving the dishes and ensuring the restaurant runs smoothly.  

Model serving includes two key steps:  
1. **Model Deployment** — serving predictions.  
2. **Model Monitoring** — ensuring ongoing performance.  

---

## 🍽️ Step 1: Model Deployment  

This is the moment your model becomes operational and starts producing predictions.  
Vertex AI provides **multiple deployment options** depending on latency, scale, and use case.  

### 🔹 Deployment Options  

| **Deployment Type** | **Description** | **Example Use Case** |
|----------------------|-----------------|----------------------|
| **Online Prediction (Real-Time)** | Deploy the model to an **endpoint** for instant predictions. Requires low latency and continuous availability. | Product recommendations, fraud detection, chatbots. |
| **Batch Prediction (Offline)** | Generate predictions periodically without deploying to an endpoint. No immediate response needed. | Marketing campaign segmentation, weekly sales predictions. |
| **Off-Cloud / Edge Deployment** | Deploy the model outside of Google Cloud — for privacy, latency, or offline needs. | IoT object detection in manufacturing, edge cameras, healthcare devices. |

You can deploy a model via:  
- **Vertex AI Console (UI)** — no-code deployment.  
- **Vertex AI SDK / APIs** — code-based approach for developers.  

---

## 🖥️ Step 2: Model Monitoring  

Once deployed, a model’s performance must be **monitored continuously** to ensure it remains accurate and reliable.  
This includes tracking **data drift**, **prediction accuracy**, and **system health**.  

### 🔹 Vertex AI Pipelines  
- The **backbone of automation** for ML workflows on Vertex AI.  
- Automates, monitors, and governs the ML lifecycle in a **serverless** way.  
- Enables **continuous integration, delivery, and training (CI/CD/CT)** for ML systems.  
- Automatically triggers alerts or retraining jobs when performance drops below thresholds.  

### 🔹 Vertex AI Workbench  
- Notebook-based tool for building and managing custom pipelines.  
- Use **SDKs and pre-built components** to define each stage of the pipeline (data → training → evaluation → deployment → monitoring).  
- Promotes modular, reusable ML development.  

---

## 💡 Key Insights  
- **Model deployment** transforms theory into production — turning trained models into real-world applications.  
- **Online predictions** prioritize speed; **batch predictions** prioritize efficiency.  
- **Off-cloud deployments** address latency, privacy, and offline operation needs.  
- **Model monitoring** ensures long-term reliability and is often automated with **Vertex AI Pipelines**.  
- The ML workflow is **complete** when deployment and monitoring are in place — the "restaurant" is officially open and running smoothly.  

---

## 📚 References  
- [Vertex AI Model Deployment](https://cloud.google.com/vertex-ai/docs/predictions/deploy-model-api)  
- [Batch Predictions on Vertex AI](https://cloud.google.com/vertex-ai/docs/predictions/get-batch-predictions)  
- [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines)  