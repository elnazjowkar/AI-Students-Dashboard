import pandas as pd
import matplotlib.pyplot as plt

# ====================================
# LOAD DATA
# ====================================

df = pd.read_csv("AI_Impact_Student_Life_2026.csv")

# ====================================
# DATA OVERVIEW
# ====================================

print(df.head())
print(df.info())
print(df.columns.tolist())
print(df.describe())

# ====================================
# DATA QUALITY CHECK
# ====================================

print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# ====================================
# FEATURE ENGINEERING
# ====================================

df["GPA_Improvement"] = df["GPA_Post_AI"] - df["GPA_Baseline"]

# ====================================
# SECTION 3 - UNIVARIATE ANALYSIS
# ====================================

# Question 1 - Age Distribution
age_count = df["Age"].value_counts().sort_index()
print(age_count)

# Question 2 - Major Distribution
major_count = df["Major"].value_counts()
print(major_count)

# Question 3 - Most Popular AI Tool
tool_usage = df["Primary_AI_Tool"].value_counts()
print(tool_usage)

# Question 4 - Main Usage Case
usage_count = df["Main_Usage_Case"].value_counts()
print(usage_count)

# Question 5 - AI Ethics Concern
ethics_count = df["AI_Ethics_Concern"].value_counts()
print(ethics_count)

# Question 6 - Career Confidence Score
career_confidence = df["Career_Confidence_Score"].value_counts()
print(career_confidence)

# Question 7 - Daily AI Usage Frequency
task_count = df["Task_Frequency_Daily"].value_counts()
print(task_count)

# ====================================
# SECTION 4 - GPA ANALYSIS
# ====================================

# Question 8 - Average GPA Before AI
gpa_before = df["GPA_Baseline"].mean()
print("Average GPA Before AI:", gpa_before)

# Question 9 - Average GPA After AI
gpa_after = df["GPA_Post_AI"].mean()
print("Average GPA After AI:", gpa_after)

# Question 10 - GPA Improvement
print("GPA Improvement:", gpa_after - gpa_before)

# Question 11 - GPA Distribution Before AI
gpa_before_dist = df["GPA_Baseline"].value_counts().sort_index()
print(gpa_before_dist)

# Question 12 - GPA Distribution After AI
gpa_after_dist = df["GPA_Post_AI"].value_counts().sort_index()
print(gpa_after_dist)

# ====================================
# SECTION 5 - TIME SAVED ANALYSIS
# ====================================

# Question 13 - Average Time Saved
avg_time_saved = df["Time_Saved_Hours_Weekly"].mean()
print("Average Time Saved Per Week:", avg_time_saved)

# Question 14 - Maximum Time Saved
print("Max Time Saved:", df["Time_Saved_Hours_Weekly"].max())

# Question 15 - Minimum Time Saved
print("Min Time Saved:", df["Time_Saved_Hours_Weekly"].min())

# Question 16 - Time Saved Distribution
time_dist = df["Time_Saved_Hours_Weekly"].value_counts()
print(time_dist)

# ====================================
# SECTION 6 - AI TOOL COMPARISON
# ====================================

# Question 17 - GPA Improvement by Tool
tool_gpa = df.groupby("Primary_AI_Tool")["GPA_Improvement"].mean()
print(tool_gpa.sort_values(ascending=False))

# Question 18 - Time Saved by Tool
tool_time = df.groupby("Primary_AI_Tool")["Time_Saved_Hours_Weekly"].mean()
print(tool_time.sort_values(ascending=False))

# Question 19 - Overall Tool Comparison
tool_compare = df.groupby("Primary_AI_Tool").agg({
    "GPA_Improvement": "mean",
    "Time_Saved_Hours_Weekly": "mean"
})

print(tool_compare.sort_values("GPA_Improvement", ascending=False))

# ====================================
# SECTION 7 - MAJOR ANALYSIS
# ====================================

# Question 20 - GPA Improvement by Major
major_gpa = df.groupby("Major")["GPA_Improvement"].mean()
print(major_gpa.sort_values(ascending=False))

# Question 21 - Time Saved by Major
major_time = df.groupby("Major")["Time_Saved_Hours_Weekly"].mean()
print(major_time.sort_values(ascending=False))

# ====================================
# SECTION 8 - ADVANCED ANALYSIS
# ====================================

# Question 22 - Correlation Between Time Saved and GPA Improvement
correlation = df["Time_Saved_Hours_Weekly"].corr(df["GPA_Improvement"])
print(correlation)

# Question 23 - GPA Improvement by Daily Usage Frequency
gpa_by_frequency = df.groupby("Task_Frequency_Daily")["GPA_Improvement"].mean()
print(gpa_by_frequency)

# Question 24 - Time Saved by Daily Usage Frequency
time_by_frequency = df.groupby("Task_Frequency_Daily")["Time_Saved_Hours_Weekly"].mean()
print(time_by_frequency)

# Question 25 - GPA Improvement by Ethics Concern
ethics_gpa = df.groupby("AI_Ethics_Concern")["GPA_Improvement"].mean()
print(ethics_gpa)

# Question 26 - GPA Improvement by Career Confidence
career_gpa = df.groupby("Career_Confidence_Score")["GPA_Improvement"].mean()
print(career_gpa)