# persiapan awal
bulan = {"jan": 0, "feb": 0, "mar": 0}

# input data
for i in bulan:
  bulan[i] = input("Silahkan masukkan pendaptan pada bulan %s: " % i)

# hitung mana yang tertinggi
tertinggi = max(bulan["jan"], bulan["feb"], bulan["mar"])

# cari dan cetak di bulan mana yang tertinggi
for i in bulan:
  if bulan[i] == tertinggi:
    print(i)