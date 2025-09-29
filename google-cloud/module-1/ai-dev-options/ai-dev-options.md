# 📘 AI Development Options on Google Cloud  

## 🎯 Learning Objectives  
- Understand the **four AI/ML development options** available on Google Cloud.  
- Compare the **pros and cons** of pre-trained APIs, BigQuery ML, AutoML, and custom training.  
- Learn how to choose the right option based on **business needs, data availability, and expertise**.  
- Recognize trade-offs in **data types supported, expertise required, training time, and flexibility**.  

---

## 📝 Summary  

Google Cloud provides **four main options** for building ML models, depending on your expertise, data availability, and business needs:  

### 1. **Pre-trained APIs**  
- Ready-to-use ML models via APIs.  
- No training data required.  
- Best for common perceptual tasks: **vision, video, natural language, and audio**.  
- Fastest option → zero training time.  
- **No hyperparameter tuning** available.  

### 2. **BigQuery ML**  
- Build ML models using **SQL queries** directly in BigQuery.  
- Ideal if data is already in BigQuery.  
- Supports **tabular data only**.  
- Allows some **hyperparameter tuning**.  
- Requires SQL expertise, but minimal ML background.  

### 3. **AutoML (Vertex AI)**  
- **No-code / low-code** option with a point-and-click interface.  
- Supports **tabular, image, text, and video** data.  
- Requires **training data**, but no coding expertise.  
- Faster than custom training, but less flexible.  
- No manual hyperparameter tuning.  

### 4. **Custom Training (Vertex AI)**  
- **Do-it-yourself approach** → maximum flexibility.  
- Train and deploy models with full control of code and infrastructure.  
- Supports all data types.  
- Requires **large datasets + ML expertise**.  
- Longest training time but allows **hyperparameter tuning** and custom pipelines.  

---

## ⚙️ Comparison Table  

| Option            | Data Types Supported        | Training Data | Expertise Needed       | Hyperparameter Tuning | Training Time       |
|-------------------|-----------------------------|---------------|------------------------|-----------------------|---------------------|
| Pre-trained APIs  | Tabular, Image, Text, Video, Audio | None          | None / Low (business users) | ❌ Not available     | Instant (pre-trained) |
| BigQuery ML       | Tabular only                | Medium to Large         | SQL expertise          | ✅ Medium          | Moderate            |
| AutoML (Vertex AI)| Tabular, Image, Text, Video | Small to medium         | Low (no-code)          | ❌ Not available     | Moderate            |
| Custom Training   | Tabular, Image, Text, Video | Large         | High (ML engineers)    | ✅ High          | Longest (full training) |

---

## 💡 Key Insights  
- **Pre-trained APIs** → best for business users needing quick AI capabilities.  
- **BigQuery ML** → great for analysts familiar with SQL and tabular datasets.  
- **AutoML** → balance between customization and ease of use.  
- **Custom Training** → full control for ML engineers & data scientists building advanced pipelines.  
- Choice depends on **business needs, expertise, budget, and time-to-market**.  

---

## 📚 References  
- [Google Cloud AI & ML Products](https://cloud.google.com/products/ai)  
- [Vertex AI AutoML](https://cloud.google.com/vertex-ai/docs/training-overview)  
- [Custom Training on Vertex AI](https://cloud.google.com/vertex-ai/docs/training/custom-training)  
