# 📘 Model Garden on Google Cloud  

## 🎯 Learning Objectives  
- Understand what **Model Garden** is and how it complements **Vertex AI Studio**.  
- Learn to search, discover, and apply **foundation**, **task-specific**, and **fine-tunable/open-source models**.  
- Explore how to use filters to find the right model for your business or research problem.  
- Understand the **workflow integration** between Model Garden, Vertex AI Studio, and code-based environments like Colab or Workbench.  

---

## 📝 Summary  

**Model Garden** is a unified **library of generative AI models** available on **Google Cloud** through **Vertex AI**.  
It provides access not only to **Google’s foundation models** but also to **third-party** and **open-source** models — all from a single, searchable interface.  

While **Vertex AI Studio** is ideal for building, fine-tuning, and testing models in a low-code environment, **Model Garden** serves as the **discovery hub** — where you can explore, filter, and launch models tailored to specific modalities or tasks.

Each model in Model Garden is accompanied by a **model card**, summarizing its **overview**, **intended use cases**, **limitations**, and **links to documentation or sample code**.  

---

## 🧭 When to Use Model Garden vs. Vertex AI Studio  

| **Use Case** | **Recommended Tool** | **Description** |
|---------------|----------------------|-----------------|
| You want to **prototype or fine-tune** a GenAI model through a UI. | 🧩 Vertex AI Studio | Build and deploy models via low-code workflows. |
| You want to **explore, compare, and select** the best model for your domain. | 🌱 Model Garden | Browse foundation, task-specific, and open-source models. |
| You want to **develop, train, or deploy models in code** (Colab / Workbench). | 💻 Model Garden + SDKs | Open sample notebooks and deploy directly from code. |

Model Garden integrates seamlessly with **Vertex AI Studio**, letting you open a chosen model directly in the Studio for testing or tuning — or launch a notebook to work programmatically.

---

## 🧠 Model Categories  

Model Garden organizes its models into **three main categories**:  

### 🔹 1. Foundation Models  
Large, pre-trained models capable of performing multiple tasks and adaptable to different domains through **tuning** or **prompting**.  

Examples include:  
| **Model** | **Purpose** |
|------------|-------------|
| **Gemini** | Multimodal model (text, image, video). |
| **Gemma** | Lightweight open model for text generation. |
| **Imagen** | Image generation and captioning. |
| **Embeddings API** | Create text or multimodal embeddings. |
| **Chirp** | Speech-to-text and voice processing. |
| **Codey** | Code generation and completion. |

These models can be accessed via **Vertex AI Studio**, **APIs**, or **SDKs** for both experimentation and production workflows.  

---

### 🔹 2. Task-Specific Models  
Models optimized to solve **specific AI tasks**.  
These are typically pre-trained for targeted use cases and require minimal configuration.  

Examples include:  
- **Entity analysis**  
- **Sentiment analysis**  
- **Syntax analysis**  
- **Object detection**  
- **Text translation**  

Many of these tasks are powered by the same APIs you explored in the **Pre-Trained APIs** class — but in Model Garden, you can interact with them in one central place.  

---

### 🔹 3. Fine-Tunable & Open-Source Models  
These models are generally **community-developed** or **open-source**, allowing you to:  
- Download and customize the model’s weights.  
- Fine-tune it in your own **notebooks or pipelines**.  
- Deploy it to **Vertex AI endpoints** for production inference.  

Open-source models provide flexibility for advanced users who prefer full control over architecture, data, and tuning strategies.  

---

## 🔍 Filtering and Searching Models  

Model Garden includes powerful filters to help you quickly find the right model:  

| **Filter Type** | **Examples** | **Purpose** |
|------------------|--------------|--------------|
| **Modality** | Language, Vision, Speech | Filter by data type or media format. |
| **Task** | Generation, Classification, Detection | Filter by functional goal. |
| **Features** | Pipeline, Notebook, One-Click Deployment | Filter by development or deployment capability. |

Using these filters, you can narrow your search to models that precisely match your project needs — from **language understanding** to **object detection** or **audio transcription**.  

---

## 🚀 Workflow Example: Using Model Garden  

Here’s how you might use Model Garden in a **real-world vision use case**:

1. **Filter for Vision Models**  
   - Open Model Garden in Google Cloud Console.  
   - Select **Modality → Vision**.  

2. **Select a Task**  
   - Under **Task**, choose **Detection**.  

3. **Explore Models**  
   - The results show models like **OWL Vision Transformer (OWL-ViT)** — an open-source zero-shot text-conditioned object detection model.  
   - This model allows you to query an image with one or more text prompts (e.g., “Find all cats in this image”).  

4. **Inspect the Model Card**  
   - Read the overview, documentation links, and example code snippets.  

5. **Open the Notebook**  
   - Click **Open Notebook** to launch a **Colab notebook** that demonstrates:  
     - Deploying the model to a **Vertex AI endpoint**.  
     - Sending an image to the endpoint.  
     - Receiving a prediction (e.g., “dog”, “tree”, or “car”).  

This workflow highlights how **Model Garden simplifies the journey** from discovery → testing → deployment in just a few clicks.  

---

## 💡 Key Insights  

- **Model Garden** is the central hub for discovering, comparing, and deploying GenAI models.  
- It integrates with **Vertex AI Studio**, **SDKs**, and **Colab notebooks** for a smooth, end-to-end workflow.  
- Offers **Google**, **third-party**, and **open-source** models across **language, vision, and speech** modalities.  
- Includes built-in filters for modality, task, and deployment capability.  
- Provides **model cards**, **sample code**, and **one-click deployment** for faster experimentation.  
- Reduces time-to-production by streamlining model selection and integration.  

---

## 📚 References  
- [Model Garden on Vertex AI](https://cloud.google.com/model-garden?hl=en)  
- [OWL-ViT: Open-Source Vision Transformer](https://huggingface.co/google/owlvit-base-patch32)  
