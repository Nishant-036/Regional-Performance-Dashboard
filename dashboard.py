import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# FILE PATH
# -------------------------
file_path = r"C:\Users\NISHANT NUNIWAL\Desktop\DA ASSIGNMENT\EXCEL ASSIGNMENT AND PROJECT\Project-3(Bare International Analysis).xlsx"

# -------------------------
# LOAD EXCEL
# -------------------------
raw = pd.read_excel(file_path, header=None)

# Fix header row
data = raw.iloc[2:].copy()
data.columns = ["Region", "Average Performer", "Bottom Performer",
                "High Performer", "Low Performer", "Grand Total"]

# Clean data
data = data[data["Region"] != "Row Labels"]
data = data.dropna(subset=["Region"])
data = data[data["Region"] != "Grand Total"]

# Convert numeric columns
for col in data.columns[1:]:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# -------------------------
# PERFORMANCE SCORE
# -------------------------
data["Performance Score"] = (
    data["High Performer"] * 0.5 +
    data["Average Performer"] * 0.3 -
    data["Low Performer"] * 0.2
)

# -------------------------
# ADD RANKING
# -------------------------
data = data.sort_values(by="Performance Score", ascending=False)
data["Rank"] = range(1, len(data) + 1)

print("\n===== REGION RANKING =====")
print(data[["Region", "Performance Score", "Rank"]])

# -------------------------
# CORPORATE DASHBOARD
# -------------------------
plt.figure()
plt.bar(data["Region"], data["Performance Score"])

plt.title("Overall Regional Performance Score (Ranked)")
plt.xlabel("Region")
plt.ylabel("Performance Score")

# Add value labels
for i in range(len(data)):
    plt.text(i, data["Performance Score"].iloc[i],
             round(data["Performance Score"].iloc[i], 3),
             ha='center', va='bottom')

# Save image
plt.savefig("Regional_Performance_Dashboard.png", dpi=300)

plt.show()

print("\nDashboard saved as: Regional_Performance_Dashboard.png")