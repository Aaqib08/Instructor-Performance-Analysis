import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="EduPro Dashboard", layout="wide")

# -------- LOAD PROCESSED DATA --------

df = pd.read_csv("processed_data.csv")
expertise_perf = pd.read_csv("expertise_perf.csv", index_col=0)
level_perf = pd.read_csv("level_perf.csv", index_col=0)
leaderboard = pd.read_csv("leaderboard.csv", index_col=0)

st.title("🎓 EduPro Instructor Performance Dashboard")

# -------- FILTERS --------

st.sidebar.header("Filters")

expertise = st.sidebar.multiselect(
"Expertise",
df["Expertise"].unique(),
default=df["Expertise"].unique()
)

filtered = df[df["Expertise"].isin(expertise)]

# -------- KPIs --------

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Teacher Rating", round(filtered["TeacherRating"].mean(),2))
col2.metric("Avg Course Rating", round(filtered["CourseRating"].mean(),2))
col3.metric("Enrollments", filtered.shape[0])

st.divider()

# -------- EXPERIENCE VS RATING --------

st.subheader("Experience vs Rating")
fig1, ax1 = plt.subplots()
ax1.scatter(filtered["YearsOfExperience"], filtered["TeacherRating"])
ax1.set_xlabel("Experience")
ax1.set_ylabel("Rating")
st.pyplot(fig1)

# -------- EXPERTISE PERFORMANCE --------

st.subheader("Course Rating by Expertise")
fig2, ax2 = plt.subplots()
expertise_perf.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# -------- COURSE LEVEL --------

st.subheader("Course Level Performance")
fig3, ax3 = plt.subplots()
level_perf.plot(kind="bar", ax=ax3)
st.pyplot(fig3)

# -------- LEADERBOARD --------

st.subheader("Top Instructors")
st.dataframe(leaderboard.head(10))
