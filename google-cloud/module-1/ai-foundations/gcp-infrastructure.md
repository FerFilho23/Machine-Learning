# 📘 Google Cloud Infrastructure  

## 🎯 Learning Objectives  
- Understand the **three-layer architecture** of Google Cloud infrastructure.  
- Learn about Google’s **compute options**: VMs, containers, serverless, and TPUs.  
- Explore Google’s **storage and database offerings** for structured and unstructured data.  
- Recognize how Google Cloud **decouples compute and storage** for independent scalability.  

---

## 📝 Summary  

Google Cloud, launched in **2008**, provides secure and scalable infrastructure built on years of AI and data innovation. Its infrastructure can be visualized in **three layers**:  

1. **Networking & Security (Base Layer):** Core foundation for applications and services.  
2. **Compute & Storage (Middle Layer):** Independent scaling of processing power and data storage.  
3. **Data & AI/ML Products (Top Layer):** Ingest, process, and analyze data; build ML models.  

### Compute Services  
- **Compute Engine (IaaS):** Virtual machines for full control and flexibility.  
- **Google Kubernetes Engine (GKE):** Managed Kubernetes for containerized applications.  
- **App Engine (PaaS):** Fully managed platform for web and mobile apps.  
- **Cloud Run:** Serverless compute for event-driven stateless workloads; scales automatically to zero.  
- **Cloud Functions:** Functions as a Service (FaaS) to run code triggered by events.  

### Specialized Hardware for ML  
- **TPUs (Tensor Processing Units):**  
  - Introduced in **2016** as custom ASICs.  
  - Domain-specific for ML matrix multiplications.  
  - Faster and more energy-efficient than CPUs/GPUs.  
  - Available as **Cloud TPUs** for customers.  

### Storage & Databases  
Google Cloud decouples compute and storage for flexibility and scalability.  

**Unstructured Data → Cloud Storage** (four storage classes):  
- **Standard:** Frequently accessed (“hot”) data.  
- **Nearline:** Infrequent access (~monthly).  
- **Coldline:** Infrequent access (~every 90 days).  
- **Archive:** Long-term archival, rarely accessed (≥1 year).  

**Structured Data → Databases (Transactional vs Analytical):**  
- **Transactional Workloads:**  
  - With SQL → **Cloud SQL** (regional) or **Spanner** (global scale).  
  - Without SQL → **Firestore** (NoSQL, document-oriented).  
- **Analytical Workloads:**  
  - With SQL → **BigQuery** (petabyte-scale data warehouse).  
  - Without SQL → **Bigtable** (NoSQL, real-time, high-throughput).  

---

## ⚙️ Practical Notes  
- **Decoupling compute and storage** enables cost-efficient independent scaling.  
- **Cloud Run and Functions** provide event-driven, serverless computing with pay-per-use pricing.  
- **TPUs** make cutting-edge AI supercomputing accessible to cloud users.  
- Storage choices depend on **data type (structured vs unstructured)** and **workload type (transactional vs analytical)**.  

---

## 💡 Key Insights  
- Google Cloud’s infrastructure is designed for **scalability, flexibility, and efficiency**.  
- Decoupling compute and storage is a key differentiator from traditional desktop/server setups.  
- The wide range of compute services covers **VMs → Containers → Serverless → Custom hardware (TPUs)**.  
- Selecting the right storage/database depends on **access frequency, workload type, and SQL/NoSQL needs**.  

---

## 📚 References  
- [Google Cloud Compute Options](https://cloud.google.com/compute)  
- [Google Cloud Storage Classes](https://cloud.google.com/storage/docs/storage-classes)  
- [Cloud Databases Overview](https://cloud.google.com/products/databases)  
- [Cloud TPUs](https://cloud.google.com/tpu)  
