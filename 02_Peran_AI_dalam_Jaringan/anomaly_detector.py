import pandas as pd
from sklearn.ensemble import IsolationForest

# Baca data
data = pd.read_csv("traffic_log.csv")

# Model AI sederhana
model = IsolationForest(contamination=0.2)  
model.fit(data[["request_count"]])

# Prediksi anomali
data["anomaly"] = model.predict(data[["request_count"]])

# Tampilkan hasil
print(data)

print("\nIP yang terdeteksi anomali (kemungkinan serangan):")
print(data[data["anomaly"] == -1]["ip"].values)
