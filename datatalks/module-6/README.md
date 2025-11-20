# 📊 Module 6 — Decision Tress and Ensemble Learning

This module moves from single-tree models to **ensembles** that combine many trees for higher accuracy and robustness. Using a credit risk scoring case, we cover how trees split data, why they overfit, how **Random Forests** reduce variance via bagging, and how **Gradient Boosting/XGBoost** iteratively reduce bias with strong regularization and early stopping.

---

## 🎯 Learning Objectives
- Grasp the structure and splitting logic of **Decision Trees** (Gini/Entropy) and common regularization.
- Understand **ensemble learning**: bagging vs. boosting; when each helps.
- Apply the intuition behind **Random Forests** (variance reduction) and **Gradient Boosting/XGBoost** (bias reduction).
- Know the core **hyperparameters** that control capacity, regularization, and speed.
- Select/tune models with proper validation (e.g., ROC-AUC for imbalanced credit risk).

---

## 🧠 Theoretical Overview

### Decision trees
- **Idea:** Recursively partition the feature space with if/else tests to create regions of high label purity.
- **Split criteria:**  
  - **Gini impurity** (fast, default in many libs) and **Entropy / Information Gain** (information-theoretic).  
- **Stopping / regularization:**  
  - Limit **max_depth**, **min_samples_split/leaf**, **max_leaf_nodes**; or **post-pruning** to control variance.
- **Pros/Cons:**  
  - ✅ Interpretable, handles mixed feature types, minimal preprocessing.  
  - ❌ High variance, sensitive to small data changes, prone to overfitting if not constrained.

---

### Ensembles and random forest
- **Ensemble learning:** Combine many weak/unstable learners to improve stability and accuracy.
- **Bagging (Bootstrap Aggregation):** Train many trees on bootstrapped samples; aggregate by **majority vote** (classification) or **mean** (regression).
- **Random Forest specifics:**  
  - **Row sampling** (bootstrap) + **feature subsampling** at each split → decorrelates trees → strong **variance reduction**.  
  - Useful diagnostics: **Out-of-Bag (OOB) error** (internal validation) and **feature importance** (Gini/Permutation).  
- **Key knobs:** `n_estimators`, `max_depth`, `min_samples_leaf/split`, `max_features` (a.k.a. `mtry`), `bootstrap`, `class_weight` for imbalance.

---

### Gradient Boosting and XGBoost
- **Boosting:** Build trees **sequentially**; each new tree fits the **residuals/gradients** of the current ensemble to reduce remaining error (**bias**).
- **Gradient Boosting Machine (GBM):**  
  - Many **shallow trees** (stumps or small depth) + small **learning rate (η)** + **many iterations**.  
  - Regularization via **shrinkage (η)**, **subsample** (stochastic GBM), **tree depth**, and **min_child_weight / min_samples_leaf**.
- **XGBoost enhancements:**  
  - Optimized tree growth and parallelism; **L1/L2** regularization; **column/row subsampling** (`colsample_bytree`, `subsample`), **missing-value handling**, and **early stopping** (monitor a valid metric like **AUC**).  
  - Typical core params:  
    - Capacity: `max_depth`, `min_child_weight`, `gamma` (min loss reduction to split)  
    - Regularization: `lambda` (L2), `alpha` (L1)  
    - Stochasticity: `subsample`, `colsample_bytree`  
    - Optimization: `eta` (learning rate), `n_estimators`/`num_boost_round`, `eval_metric` (e.g., `auc`)

---

### Hyperparameter Tuning
- **Validation protocol:** Use **Stratified K-Fold** (or OOB for RF) and **ROC-AUC** for imbalanced credit risk; keep a final **holdout** set.  
- **Search strategies:**  
  - **Grid Search** (exhaustive, small grids), **Random Search** (efficient on large spaces), or **Bayesian/SMBO** (iterative).  
  - For boosting, prefer **early stopping** on a validation fold to pick `num_boost_round`.  
- **What to tune (typical):**  
  - **Decision Tree:** `max_depth`, `min_samples_leaf`, `min_samples_split`, `criterion`.  
  - **Random Forest:** `n_estimators`, `max_depth`, `min_samples_leaf`, `max_features`, (optionally) `class_weight`.  
  - **XGBoost:** start with `eta`, `max_depth`, `min_child_weight`, then add `subsample`, `colsample_bytree`, regularizers (`lambda`, `alpha`); use `early_stopping_rounds`.  
- **Metrics & trade-offs:** Monitor **bias vs. variance**; choose thresholds post-training based on business costs (e.g., catching defaulters: prioritize Recall/AUC).

---

## 💡 Key Takeaways
- **Single trees** are intuitive but high-variance; **constrain or prune** to generalize.
- **Random Forests** average many decorrelated trees → strong **variance reduction**, robust defaults on tabular data.
- **Gradient Boosting/XGBoost** add trees sequentially to fix residual errors → strong **bias reduction** with powerful regularization and early stopping.
- Effective models come from **sound validation** (Stratified CV/OOB), **appropriate metrics** (AUC for imbalance), and **targeted hyperparameter tuning**.
- Choose **bagging** (RF) when variance dominates; choose **boosting** (XGBoost) when you need finer decision boundaries and can manage regularization carefully.
