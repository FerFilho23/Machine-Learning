# 🧪 Predict Visitor Purchases with BigQuery ML  

## 🎯 Objectives  
- Explore Google Analytics e-commerce data in **BigQuery**.  
- Build and train a **logistic regression model** in BigQuery ML with SQL.  
- Evaluate the model using **ML.EVALUATE**.  
- Make predictions with **ML.PREDICT** and aggregate results by country.  
- Debug and refine queries with **Gemini Code Assist**.  

---

## 📝 Overview  
This lab uses BigQuery ML to predict whether a visitor to the **Google Merchandise Store** will make a purchase.  
The lab demonstrates the full ML workflow:  

1. **Data exploration & preparation** → Create a labeled dataset from public Google Analytics data.  
2. **Model creation** → Train a logistic regression model in BigQuery ML.  
3. **Model evaluation** → Use ML.EVALUATE to test performance.  
4. **Prediction** → Predict transactions per country.  

By the end, you understand how to run an ML pipeline fully within **BigQuery using SQL**.  

---

## ⚙️ Lab Steps  

### 🔹 Task 1: Explore the Data  
- Query the `bigquery-public-data.google_analytics_sample` dataset.  
- Create a **training dataset** (`training_data`) with features:  
  - `label` (transaction: 0 or 1)  
  - `os`, `is_mobile`, `country`, `pageviews`  
- Save results as a view in dataset `bqml_lab`.  

```sql
SELECT
  IF(totals.transactions IS NULL, 0, 1) AS label,
  IFNULL(device.operatingSystem, "") AS os,
  device.isMobile AS is_mobile,
  IFNULL(geoNetwork.country, "") AS country,
  IFNULL(totals.pageviews, 0) AS pageviews
FROM
  `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
  _TABLE_SUFFIX BETWEEN '20160801' AND '20170631'
LIMIT 10000;
```

### 🔹 Task 2: Create a Model  
- Use `CREATE MODEL` with **logistic regression** (`LOGISTIC_REG`).  
- Train on the `training_data` view.  

```sql
CREATE MODEL
 `set at lab start`.`bqml_lab`.`sample_model` OPTIONS ( model_type = 'LOGISTIC_REG',
input_label_cols = ['label']) AS
SELECT
 label,
 os,
 is_mobile,
 country,
 pageviews
FROM
 `set at lab start`.`bqml_lab`.`training_data`;
```

### 🔹 Task 3: Evaluate the Model
- Run ML.EVALUATE to measure accuracy, precision, recall, etc.

```sql
SELECT
*
FROM
ML.EVALUATE( MODEL `set at lab start`.`bqml_lab`.`sample_model`,
TABLE `set at lab start`.`bqml_lab`.`training_data`);
```

### 🔹 Task 4: Use the Model
- Prepare July 2017 data (july_data).
- Run predictions using ML.PREDICT.
- Aggregate predictions by country to find top 10 purchasing regions.

```sql
SELECT
  country,
  SUM(predicted_label) as total_predicted_purchases
FROM
  ml.PREDICT(MODEL `bqml_lab.sample_model`, (
SELECT * FROM `bqml_lab.july_data`))
GROUP BY country
ORDER BY total_predicted_purchases DESC
LIMIT 10;
```

### 🔑 Key Learnings

BigQuery ML allows training + prediction fully in SQL.

Logistic regression is ideal for binary classification (purchase = yes/no).

Gemini Code Assist can explain queries and suggest fixes.

Debugging SQL requires checking valid BigQuery functions.

ML predictions can be integrated with standard SQL aggregation for insights.