import re
from collections import Counter

# Membaca log akses
with open("access.log", "r") as f:
    logs = f.readlines()

# Ambil hanya alamat IP
ips = [re.match(r"^\d+\.\d+\.\d+\.\d+", log).group() for log in logs]

# Hitung frekuensi akses
counter = Counter(ips)

print("Jumlah akses per IP:")
for ip, jumlah in counter.items():
    print(ip, ":", jumlah)

print("\nIP paling sering mengakses:", counter.most_common(1)[0][0])
