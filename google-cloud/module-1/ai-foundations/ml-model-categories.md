# 📘 ML Model Categories  

## 🎯 Learning Objectives  
- Distinguish between **AI** and **Machine Learning**.  
- Understand the relationship between **supervised, unsupervised, deep learning, and generative AI**.  
- Explore the major types of supervised and unsupervised learning.  
- Learn to map real-world problems to the correct ML model category.  

---

## 📝 Summary  

### AI vs. Machine Learning  
- **Artificial Intelligence (AI):** Broad umbrella of computer systems mimicking human intelligence (e.g., self-driving cars, robots).  
- **Machine Learning (ML):** Subset of AI where systems learn from data instead of explicit programming.  

### ML Subsets  
- **Supervised Learning:**  
  - Uses **labeled data**.  
  - Task-driven → learns from known inputs/outputs.  
  - Example: Classify cats vs. dogs with labeled pictures.  
- **Unsupervised Learning:**  
  - Uses **unlabeled data**.  
  - Data-driven → finds hidden patterns.  
  - Example: Group dog breeds without prior labels.  
- **Deep Learning:** Neural networks with multiple layers (input → hidden layers → output) for more complex tasks.  
- **Generative AI (GenAI):** Uses deep learning + large language models (LLMs) to generate content (e.g., Chatbots, LLM-based apps).  

---

### Types of Supervised Learning  
1. **Classification** → Predicts categorical values.  
   - Example: Dog vs. Cat.  
   - Common Model: **Logistic Regression**.  
2. **Regression** → Predicts continuous values.  
   - Example: Forecasting product sales.  
   - Common Model: **Linear Regression**.  

### Types of Unsupervised Learning  
1. **Clustering** → Groups similar data points.  
   - Example: Customer segmentation.  
   - Model: **k-means clustering**.  
2. **Association** → Identifies relationships/correlations.  
   - Example: “Customers who buy X also buy Y.”  
   - Algorithm: **Apriori** (association rule learning).  
3. **Dimensionality Reduction** → Reduces dataset features for efficiency.  
   - Example: Simplifying insurance risk factors into a scoring model.  
   - Model: **Principal Component Analysis (PCA)**.  

---

## ⚙️ Practical Notes  
- **Supervised learning = labeled data.**  
- **Unsupervised learning = no labels, find patterns.**  
- **Classification vs. Regression** → Categorical vs. Continuous outputs.  
- **Example:**  
  - Predicting customer spending → **Supervised, Regression, Linear Regression**.  
  - Finding customer segments → **Unsupervised, Clustering, k-means**.  
- These models can be implemented via **BigQuery ML, AutoML, or Custom Training** in Google Cloud.  

---

## 💡 Key Insights  
- Supervised learning is most useful when you have **clear goals + labeled datasets**.  
- Unsupervised learning is valuable for **exploratory analysis** and pattern discovery.  
- Regression vs. Classification distinction is critical for problem framing.  
- Many ML tasks can be quickly prototyped in **BigQuery ML** without leaving SQL.  

---

## 📚 References  
- [BigQuery ML Models](https://cloud.google.com/bigquery-ml/docs/introduction)  
- [Google Cloud AutoML](https://cloud.google.com/automl)  
