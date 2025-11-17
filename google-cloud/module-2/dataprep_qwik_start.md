# 📘 Lab — Dataprep: Qwik Start

## 🎯 Learning Objectives
- Learn how to **create and manage Cloud Dataprep flows** for data cleaning and transformation.
- Explore how to **import, wrangle, and join datasets** using the Dataprep interface.
- Practice **data aggregation, renaming, and feature preparation** for ML workflows.
- Understand how **Cloud Dataprep** (Alteryx Designer Cloud) integrates with **Cloud Storage** and **BigQuery**.

---

## 🧭 Overview
In this lab, you use **Cloud Dataprep by Trifacta (Alteryx Designer Cloud)** to prepare U.S. Federal Election Commission (FEC) datasets for analysis.
You create flows, import data from **Cloud Storage**, clean and join datasets, and summarize contribution data for presidential candidates.

---

## 🔹 Task 1 — Create a Cloud Storage Bucket
1. Open **Cloud Console → Storage → Buckets**.
2. Click **Create bucket**.
3. Provide a unique bucket name.
4. Disable **Enforce public access prevention**.
5. Click **Create**.

---

## 🔹 Task 2 — Initialize Cloud Dataprep
1. Run this command in Cloud Shell:
   ```bash
   gcloud beta services identity create --service=dataprep.googleapis.com
   ```
2. In the console, go to **View All Products → Alteryx Designer Cloud**.
3. Accept terms of service.
4. Allow access to project data.
5. Complete setup and open Dataprep.

---

## 🔹 Task 3 — Create a Flow
1. Click the **Flows** icon → **Create → Blank Flow**.
2. Rename the flow to **FEC-2016**.
3. Add a description:  
   *United States Federal Elections Commission 2016*.

---

## 🔹 Task 4 — Import Datasets
1. Click **Add Datasets → Import Datasets**.
2. Select **Cloud Storage**, edit the file path:
   ```
   gs://spls/gsp105
   ```
3. Navigate to `us-fec/`.
4. Import and rename:
   - `cn-2016.txt` → **Candidate Master 2016**
   - `itcont-2016-orig.txt` → **Campaign Contributions 2016**
5. Click **Import & Add to Flow**.

---

## 🔹 Task 5 — Prepare the Candidate File
### Filter data to include only years 2016–2017
1. Open **Candidate Master 2016 → Edit Recipe**.
2. In `column5`, select the 2016 bin.
3. Apply the suggestion:  
   ```
   Keep rows where(DATE(2016,1,1) <= column5) && (column5 < DATE(2018,1,1))
   ```

### Fix mismatched values in State column
1. Column6 shows mismatches because it's typed as **State**.
2. Change the type to **String**.

### Filter for Presidential Candidates
1. In `column7`, select the **P** category.
2. Apply **Keep rows** recommendation.

---

## 🔹 Task 6 — Wrangle Contributions File & Join Datasets
### Clean Contribution Data
1. Open **Campaign Contributions 2016 → Add Recipe → Edit Recipe**.
2. Add New Step and insert:
   ```bash
   replacepatterns col: * with: '' on: `{start}"|"{end}` global: true
   ```

### Join with Candidate Dataset
1. Add New Step → search “Join”.
2. Select **Candidate Master 2016** to join.
3. In join keys, choose:
   ```
   column2 = column11
   ```
4. Add all columns, review, and add to recipe.

---

## 🔹 Task 7 — Generate Summary of Data
Use pivot aggregation:
```bash
pivot value:sum(column16),average(column16),countif(column16 > 0) group: column2,column24,column8
```

This produces a summary table with:
- Candidate ID  
- Candidate Name  
- Party Affiliation  
- Total contribution amount  
- Average contribution  
- Number of contributions  

---

## 🔹 Task 8 — Rename Columns
Add step:
```bash
rename type: manual mapping: [column24,'Candidate_Name'], 
[column2,'Candidate_ID'],
[column8,'Party_Affiliation'], 
[sum_column16,'Total_Contribution_Sum'], 
[average_column16,'Average_Contribution_Sum'], 
[countif,'Number_of_Contributions']
```

Round average contributions:
```bash
set col: Average_Contribution_Sum value: round(Average_Contribution_Sum)
```

---

## ✅ Final Result
You created a transformed dataset summarizing:
- Presidential candidates  
- Their party affiliations  
- Total contributions  
- Average contributions  
- Contribution count  

This dataset is now **ready for ML APIs, BigQuery analysis, or feature engineering**.

---

## 📚 References
- [Dataprep: Qwik Start Lab](https://www.skills.google/paths/17/course_templates/631/labs/594528)
