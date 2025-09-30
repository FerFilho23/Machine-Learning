# 📘 Custom Training on Google Cloud  

## 🎯 Learning Objectives  
- Understand **custom training** as the do-it-yourself (DIY) ML option on Vertex AI.  
- Learn the difference between **pre-built containers** and **custom containers** for training environments.  
- Explore how to use **Vertex AI Workbench** and **Colab Enterprise** for coding ML workflows.  
- Recognize the role of popular **ML libraries** (TensorFlow, Scikit-learn, PyTorch, JAX) in custom training.  
- Understand the basic workflow of building a model with **TensorFlow/Keras**.  

---

## 📝 Summary  

While Google Cloud offers **pre-trained APIs**, **BigQuery ML**, and **AutoML**, some ML engineers and data scientists require full control of their environment and pipeline.  
This is where **Custom Training** on Vertex AI comes in.  

Custom training allows you to **design, code, and manage your ML workflow** with maximum flexibility:  
- Define the **training environment**.  
- Write and run **custom ML code**.  
- Leverage Google Cloud’s infrastructure for scaling and deployment.  

---

## ⚙️ Training Environments  

- **Pre-built Containers:**  
  - Like a furnished kitchen — comes with ML frameworks pre-installed (e.g., Python, TensorFlow, PyTorch).  
  - Best for when you don’t care about the underlying infrastructure details.  

- **Custom Containers:**  
  - Like an empty kitchen — you bring your own tools and configurations.  
  - Define details such as environment, machine type, disks, and dependencies.  
  - Provides full control for specialized ML workloads.  

---

## 🛠️ Tools for Custom Training  

- **Vertex AI Workbench:**  
  - A managed Jupyter Notebook environment.  
  - Supports the full ML lifecycle: exploration → training → deployment.  

- **Colab Enterprise (since 2023):**  
  - Collaborative coding environment integrated into Vertex AI.  
  - Familiar for users of Google Colab, with enterprise-grade integration.  

---

## 📚 ML Libraries for Custom Training  

- **TensorFlow (Google-supported):**  
  - End-to-end ML framework with multiple abstraction levels:  
    - Low-level APIs (C++, Python ops).  
    - Model libraries (neural layers, metrics).  
    - High-level APIs (**Keras**) for simplified model building.  
  - Runs on CPUs, GPUs, and TPUs.  
  - Fully hosted on Vertex AI.  

- **Scikit-learn & PyTorch:** Popular open-source frameworks widely used in ML development.  

- **JAX:** Google’s high-performance numerical computation library for flexible, research-grade ML.  

---

## 🔬 Example: Building a Model with TensorFlow/Keras  

1. **Create a Model:**  
   - Use `Sequential()` to define layers of a neural network.  
   - Example: A simple 3-layer neural network.  

2. **Compile the Model:**  
   - Define loss function (e.g., mean squared error).  
   - Choose optimizer (e.g., Adam, SGD).  
   - Set evaluation metrics.  

3. **Train the Model:**  
   - Use `.fit()` with training data.  
   - Specify number of **epochs** (iterations).  

4. **Deploy & Predict:**  
   - Once trained, deploy the model to Vertex AI.  
   - Use it to serve real-time or batch predictions.  

---

## 💡 Key Insights  
- **Custom Training = maximum flexibility.** Ideal for ML engineers needing control over the environment and pipeline.  
- Pre-built containers are **quick and easy**, while custom containers are for **specialized, fine-grained control**.  
- TensorFlow (with Keras APIs) remains the core framework, but **JAX** is emerging as a promising future option.  
- Vertex AI provides the **infrastructure + managed services** so you can focus on the ML code.  

---

## 📚 References  
- [Custom Training on Vertex AI](https://cloud.google.com/vertex-ai/docs/training/custom-training-overview)  
- [TensorFlow on Google Cloud](https://cloud.google.com/vertex-ai/docs/start/tensorflow?hl=pt-br)  
- [JAX: High-performance ML](https://github.com/google/jax)  
