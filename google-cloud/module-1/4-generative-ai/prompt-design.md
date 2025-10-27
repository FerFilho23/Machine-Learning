# 📘 Prompt Design on Google Cloud  

## 🎯 Learning Objectives  
- Understand the **core principles of prompt design** for generative AI.  
- Learn the difference between **zero-shot**, **one-shot**, and **few-shot prompting**.  
- Explore **best practices** for writing clear, structured prompts.  
- Understand how **model parameters** such as **temperature**, **top-K**, and **top-P** control response randomness and creativity.  

---

## 📝 Summary  

**Prompt design** is both an **art and a science**. It’s the process of crafting inputs that guide a generative AI model toward useful, accurate, or creative outputs. The way a prompt is written directly determines how the model interprets your request and what type of response it produces.  

In **Vertex AI Studio**, you can experiment with prompts in both **free-form** and **structured** modes, exploring how small adjustments affect model behavior.  

---

## 💬 Prompting Methods  

There are **three main prompting strategies** for shaping model behavior:  

| **Method** | **Description** | **Example** |
|-------------|----------------|--------------|
| **Zero-Shot Prompting** | You provide an **instruction** with no examples. The model uses general knowledge to respond. | “Generate a list of items I need for a camping trip to Joshua Tree National Park.” |
| **One-Shot Prompting** | You give the model **one example** to demonstrate the desired behavior. | “Here’s a poem example → Now write a similar poem about the ocean.” |
| **Few-Shot Prompting** | You include **multiple examples** of input-output pairs to guide the model’s style and logic. | IT Help Desk context with several Q&A examples before asking a new question. |

Few-shot prompting is especially powerful when you want the model to **imitate patterns** or **adhere to a tone or style**, such as customer support, data extraction, or storytelling.  

---

## 🧱 Structured Prompts  

A **structured prompt** combines several components:  

| **Component** | **Purpose** | **Example** |
|----------------|-------------|--------------|
| **Context** | Guides how the model should behave and respond. | “You are an environmental researcher answering questions about rainforest vegetation.” |
| **Examples** | Shows model how to respond using prior question-answer pairs. | “Q: What does LGM stand for? → A: Last Glacial Maximum.” |
| **Input** | The new query you want the model to answer. | “Q: What did the analysis from the sediment deposits indicate?” |

By combining context, examples, and input, you can quickly **prototype a Q&A system** or **simulate domain expertise** within minutes.  

---

## ✅ Best Practices for Effective Prompts  

- **Be concise and specific.** Clearly define the task or question.  
- **Ask one task at a time.** Avoid overloading the prompt with unrelated requests.  
- **Use examples.** Demonstrating the desired output improves consistency.  
- **Experiment.** Different formats and phrasings can yield different results, there’s no single “best” prompt.  

If a prompt produces strong results, you can **save it** in **Vertex AI Studio’s Prompt Gallery**, a curated library of reusable and shareable prompts across use cases.  

---

## ⚙️ Model Parameters for Fine-Tuning Responses  

Beyond prompt wording, **Vertex AI Studio** provides several model parameters that affect the **randomness**, **creativity**, and **focus** of responses.  

### 🔹 1. Temperature  
Controls **how deterministic or creative** the model’s responses are.  
- **Low (0–0.3):** Predictable and focused — best for Q&A or summarization tasks.  
- **High (0.7–1.0):** Diverse and imaginative — better for brainstorming, storytelling, or marketing copy.  

### 🔹 2. Top-K Sampling  
Limits the next token (word) choices to the **K most probable options**, then randomly picks one.  
- Example: **Top-2** → randomly selects between the two most likely next words.  
- Too small a K may cause repetitive answers; too large may introduce incoherence.  

### 🔹 3. Top-P (Nucleus) Sampling  
Selects from the **smallest subset of words** whose cumulative probability ≥ **P**.  
- Example: **P = 0.75** → sample from words that collectively make up 75% of likelihood.  
- Dynamic approach — adapts to the model’s probability distribution for smoother, natural variation.  

### 🔹 4. Model Selection  
Each model is tuned for specific domains (e.g., text, multimodal, chat).  
Choose the one that best matches your use case before sending the prompt.  

> ⚠️ You don’t need to constantly tweak all parameters — **temperature** alone often provides sufficient control for most prompt-testing scenarios.  

---

## 💡 Key Insights  

- **Prompt design** determines how effectively you can harness a GenAI model’s intelligence.  
- Use **zero-shot** for quick tasks, **one-shot** for stylistic control, and **few-shot** for complex behavior modeling.  
- Structured prompts (context + examples + input) enable consistent and domain-specific performance.  
- Experimentation is essential, refine prompts iteratively based on output quality.  
- Parameters like **temperature**, **top-K**, and **top-P** let you balance between precision and creativity.  
- Saved prompts in **Prompt Gallery** help you build reusable GenAI assets for future projects.  

---

## 📚 References  
- [Content generation parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters)  
- [Vertex AI Studio Prompt Gallery](https://cloud.google.com/vertex-ai/docs/generative-ai/prompt-gallery)  
