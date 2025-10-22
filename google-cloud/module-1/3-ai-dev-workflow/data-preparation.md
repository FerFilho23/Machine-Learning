# 📘 Data Preparation on Google Cloud  

## 🎯 Learning Objectives  
- Understand the **data preparation stage** of the ML workflow in Vertex AI.  
- Learn the **four supported data types** in AutoML: image, tabular, text, and video.  
- Explore the concept and importance of **feature engineering**.  
- Discover how **Vertex AI Feature Store** helps manage, serve, and share features efficiently.  

---

## 📝 Summary  

**Data preparation** is the **first stage** of the machine learning workflow.  
It includes two major steps:  
1. **Uploading data** from sources such as **Cloud Storage**, **BigQuery**, or a **local machine**.  
2. **Preparing data for training** through **feature engineering**.  

AutoML supports multiple data types, each with unique **objectives (tasks)** it can solve.  

---

## ⚙️ Data Types and Objectives  

| **Data Type** | **Objectives / Problems Solved** | **Examples** |
|----------------|----------------------------------|---------------|
| **Image** | Classification (single-label or multi-label), Object Detection, Image Segmentation | - Identify cats vs dogs (single-label)<br>- Tag multiple features (multi-label)<br>- Detect or segment objects in images |
| **Tabular** | Regression, Classification, Forecasting | - Predict sales trends<br>- Customer churn analysis<br>- Revenue forecasting |
| **Text** | Classification, Entity Extraction, Sentiment Analysis | - Classify emails as spam or not<br>- Extract named entities<br>- Analyze customer feedback tone |
| **Video** | Video Action Recognition, Classification, Object Tracking | - Identify movements or actions<br>- Classify video scenes<br>- Track objects across frames |

> 🧠 Note:  
> Pre-trained APIs use Google’s pre-trained models with no customer data.  
> AutoML, however, **trains custom models** using your own dataset — providing flexibility and domain adaptation.

In practice, many business problems require **combining multiple data types** and **objectives** — something AutoML can handle within Vertex AI.

---

## 🔧 Feature Engineering  

Feature engineering is like **prepping ingredients before cooking**.  
You clean, slice, and prepare data before it’s ready for model training.  

- A **feature** is a variable or attribute that contributes to a model’s prediction.  
- Proper feature preparation is crucial for model accuracy and performance.  
- This process can be time-consuming, which is why Google Cloud offers **Vertex AI Feature Store** to simplify it.  

---

## 🗄️ Vertex AI Feature Store  

**Vertex AI Feature Store** is a **centralized repository** that helps manage, serve, and share features for both **training and serving**.  

### Key Functions  
- Aggregates feature data from multiple sources (e.g., BigQuery).  
- Serves data for **real-time (online)** and **batch (offline)** ML predictions.  
- Automates feature aggregation for **low-latency** serving.  
- Supports **embeddings** for **Generative AI** use cases — allowing retrieval of similar items in real time.  

### Workflow Summary  
1. **Prepare data source** in BigQuery.  
2. (Optional) **Register features** by creating feature groups and definitions.  
3. **Set up online stores and feature views** to connect data sources with serving clusters.  
4. **Serve latest feature values** from feature views for real-time prediction.  

### Benefits of Feature Store  
- **Shareable:** Centralized repository ensures consistency across teams.  
- **Reusable:** Save time and reduce duplication by reusing features.  
- **Scalable:** Automatically scales for low-latency access.  
- **User-Friendly:** Includes an easy-to-navigate UI for management.  

---

## 💡 Key Insights  
- Data preparation is foundational — **the quality of your data defines the quality of your model**.  
- **AutoML** simplifies working with diverse data types and objectives.  
- **Feature engineering** transforms raw data into actionable ML inputs.  
- **Vertex AI Feature Store** ensures scalability, reusability, and real-time readiness, including support for **Generative AI embeddings**.  

---

## 📚 References  
- [Vertex AI Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore)  
- [AutoML Training Overview](https://cloud.google.com/vertex-ai/docs/training/automl-training-overview)  
- [BigQuery Data Sources](https://cloud.google.com/bigquery/docs/loading-data)  
