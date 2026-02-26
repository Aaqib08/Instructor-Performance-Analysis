import pandas as pd

# ---------------- LOAD DATA ----------------

users = pd.read_csv("EduPro Online Platform.xlsx - Users.csv")
teachers = pd.read_csv("Teachers.csv")
courses = pd.read_csv("Courses.csv")
transactions = pd.read_csv("Transactions.csv")

# ---------------- MERGE ----------------

df = (
    transactions.merge(users, on="UserID")
               .merge(courses, on="CourseID")
               .merge(teachers, on="TeacherID")
)
print("Merged Shape:", df.shape)

# ---------------- KPIs ----------------

avg_teacher_rating = df["TeacherRating"].mean()
avg_course_rating = df["CourseRating"].mean()
experience_corr = df[["YearsOfExperience","TeacherRating"]].corr().iloc[0,1]

print("\nAverage Teacher Rating:", round(avg_teacher_rating,2))
print("Average Course Rating:", round(avg_course_rating,2))
print("Experience Impact:", round(experience_corr,2))

# ---------------- GROUP METRICS ----------------

expertise_perf = df.groupby("Expertise")["CourseRating"].mean()
level_perf = df.groupby("CourseLevel")["CourseRating"].mean()
leaderboard = df.groupby("TeacherName")["CourseRating"].mean().sort_values(ascending=False)

print("\nTop Teachers:\n", leaderboard.head(10))

# ---------------- SAVE FOR STREAMLIT ----------------

df.to_csv("processed_data.csv", index=False)
expertise_perf.to_csv("expertise_perf.csv")
level_perf.to_csv("level_perf.csv")
leaderboard.to_csv("leaderboard.csv")

print("\nProcessed files saved for Streamlit!")
