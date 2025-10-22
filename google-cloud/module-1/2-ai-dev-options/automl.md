# 📘 AutoML on Google Cloud  

## 🎯 Learning Objectives  
- Understand **AutoML** as a no-code solution embedded in Vertex AI.  
- Learn how AutoML automates the **end-to-end ML pipeline**.  
- Explore the technologies powering AutoML: **transfer learning** and **neural architecture search**.  
- Recognize how AutoML balances **accuracy, speed, and accessibility** for ML development.  

---

## 📝 Summary  

**AutoML (Automated Machine Learning)** was introduced by Google in **2018** to reduce the manual effort of developing ML models.  
Since **2021**, AutoML has been fully integrated into **Vertex AI**, making it a core part of Google Cloud’s ML ecosystem.  

AutoML automates tasks from **data preprocessing → model search → tuning → deployment**, enabling non-experts to build ML models through a **point-and-click UI**.  

---

## ⚙️ How AutoML Works  

### 🔹 Phase 1: Data Processing  
- Converts numbers, text, date-time, categories, arrays, and nested fields into ML-ready formats.  
- Automates much of **feature engineering**.  

### 🔹 Phase 2: Model Search & Hyperparameter Tuning  
- **Neural Architecture Search (NAS):**  
  - Explores multiple model architectures automatically.  
  - Tunes hyperparameters based on performance.  
- **Transfer Learning:**  
  - Uses pre-trained models as a foundation.  
  - Fine-tunes models with smaller, domain-specific datasets.  
  - Example: Large Language Models (LLMs) → adapted for retail, finance, or entertainment tasks.  
  - Benefits: Higher accuracy, less data, faster training.  

### 🔹 Phase 3: Model Assembly  
- AutoML selects the **top-performing models** (typically ~10).  
- Combines them (e.g., averaging predictions) → ensemble improves accuracy.  

### 🔹 Phase 4: Prediction  
- The best models are deployed for inference.  
- Users can generate predictions without writing code.  

---

## 💡 Key Insights  
- **AutoML = Democratized ML** → allows analysts and business users to build ML solutions.  
- Advanced ML techniques (NAS + Transfer Learning) enable **speed and efficiency**.  
- Using **ensembles** of top models increases predictive power.  
- Provides a **no-code UI**, shifting focus from infrastructure/code to **solving business problems**.  

---

## 📚 References  
- [AutoML on Vertex AI](https://cloud.google.com/vertex-ai/docs/training/automl-training-overview)
