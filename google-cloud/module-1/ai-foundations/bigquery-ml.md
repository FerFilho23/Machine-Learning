# 📘 BigQuery ML  

## 🎯 Learning Objectives  
- Understand how **BigQuery ML** integrates data analytics and machine learning.  
- Learn the **phases of building an ML model with SQL** in BigQuery.  
- Explore the supported **ML model types** in BigQuery ML.  
- Recognize how BigQuery ML supports **MLOps** for production-ready workflows.  

---

## 📝 Summary  

**BigQuery** is Google Cloud’s primary **data analytics tool** that combines:  
1. **Managed storage** for loading and storing datasets.  
2. **SQL-based analytical engine** for large-scale queries.  

With **BigQuery ML**, you can go beyond analytics and build ML models **directly inside BigQuery** using SQL commands.  
This reduces complexity, since data ingestion, feature preprocessing, model training, evaluation, and prediction can happen in one environment.  

### Key Features of BigQuery ML  
- Build ML models with **SQL syntax**.  
- Automatic handling of **common preprocessing tasks** (e.g., one-hot encoding).  
- Supports **supervised and unsupervised models** (logistic regression, linear regression, k-means, time series forecasting, deep neural networks).  
- Integration with **MLOps** for deployment, monitoring, and lifecycle management.  

---

## ⚙️ Phases of a Machine Learning Project in BigQuery ML  

1. **Data Loading (ETL):**  
   - Load tabular data into BigQuery.  
   - Use connectors (e.g., YouTube → BigQuery) or SQL joins for enrichment.  

2. **Feature Selection & Preprocessing:**  
   - Create training datasets with SQL.  
   - BigQuery ML handles preprocessing like **one-hot encoding**.  

3. **Model Creation:**  
   - Use `CREATE MODEL` with model type + label column.  
   - Example: Predicting customer purchase behavior → **Logistic Regression** (classification).  
   - Supported models:  
     - Logistic Regression (classification)  
     - Linear Regression (regression)  
     - k-means clustering (unsupervised)  
     - Time series forecasting  
     - Deep Neural Networks (DNN)  

4. **Model Evaluation:**  
   - Use `ML.EVALUATE` to measure performance.  
   - Metrics: accuracy, precision, recall, etc.  

5. **Prediction:**  
   - Use `ML.PREDICT` on the trained model.  
   - Returns predictions + model confidence.  
   - Predictions appear as new fields in the result set.  

---

## 💡 Key Insights  
- **BigQuery ML bridges analytics and ML** by letting you train models without leaving SQL.  
- **Start simple**: Use linear/logistic regression as baselines before moving to DNNs or more complex models.  
- BigQuery ML is particularly effective for **tabular data problems** common in business (e.g., churn prediction, sales forecasting).  
- Integration with **MLOps** makes it easier to deploy models into production pipelines.  

---

## 📚 References  
- [BigQuery ML Documentation](https://cloud.google.com/bigquery/docs/bqml-introduction)  
