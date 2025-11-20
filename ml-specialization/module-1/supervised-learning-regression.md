# 📘 Supervised Learning

## 🎯 Learning Objectives

- Understand what supervised learning is and why it powers most real-world ML applications.

- Learn the concept of input (X) and output/label (Y) mappings.

- Identify common supervised learning applications across industries.

- Understand regression as a type of supervised learning used for predicting numbers.

## 📝 Summary

### 🔍 What Is Supervised Learning?

Supervised learning is a type of machine learning in which the algorithm learns how to map **inputs (X)** to **outputs (Y)** using examples that include the correct answers.

![imge1](./img/image1.png)

After learning this mapping, the model can take a new, unseen input X and predict Y with good accuracy.

This paradigm accounts for ~99% of the economic value created by ML today.

A supervised learning problem always gives the model:

**Input X:** an email, audio clip, image, user profile, sensor reading, etc.

**Output Y:** spam or not, transcript, translated sentence, click or not, price, position, defect label…

The model learns from being given the right answers during training.

### 📦 Examples of Supervised Learning Applications

![imge2](./img/image2.png)

Supervised learning powers a huge range of real-world systems. Advertising alone generates billions in revenue by predicting which ads users will click.

### 📈 Regression: Predicting Housing Prices

To explore supervised learning, we can use housing price prediction as an example.

#### Dataset

**X:** house size in square feet

**Y:** price in thousands of dollars

Each point on the graph is a house with a known size and selling price.

![imge3](./img/image3.png)

#### Goal

Predict the selling price of a 750 sq ft house.

#### Method 1 — Fit a straight line

One learning algorithm fits a straight line to the data and reads off a price prediction:

Prediction = about $150k.

#### Method 2 — Fit a more flexible curve

Another algorithm may fit a curved function that better captures the data, producing a different prediction:

Prediction = closer to $200k.

### 🔢 What Is Regression?

Regression is the supervised learning task where:

- The goal is to predict a number

- There are infinitely many possible outputs

Examples:

- House prices

- Temperature forecasts

- Stock prices

- Customer lifetime value

This housing example is a regression problem because price is a continuous numeric output.

## 📚 References
[Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning)

[Regression Analysis](https://en.wikipedia.org/wiki/Regression_analysis)