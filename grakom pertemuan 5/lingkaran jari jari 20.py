
import matplotlib.pyplot as plt

# Fungsi algoritma Midpoint Circle
def midpoint_circle(xc, yc, r):
    x, y = 0, r
    d = 1 - r
    points = []

    # Perulangan untuk menghitung titik lingkaran
    while x <= y:

        # Membuat 8 titik simetri
        for px, py in [
            (x, y), (y, x), (-x, y), (-y, x),
            (x, -y), (y, -x), (-x, -y), (-y, -x)
        ]:
            points.append((xc + px, yc + py))

        # Menghitung parameter keputusan
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1

        x += 1

    return points


# Menggambar lingkaran dengan jari-jari 20
r = 20
pts = midpoint_circle(0, 0, r)

# Menghitung jumlah titik unik
jumlah_titik = len(set(pts))

# Memisahkan koordinat X dan Y
x, y = zip(*pts)

# Menampilkan jumlah titik
print("Jari-jari:", r)
print("Jumlah titik:", jumlah_titik)

# Visualisasi lingkaran
plt.figure(figsize=(7, 7))
plt.scatter(x, y, s=20, c='red')

plt.axis('equal')
plt.xlim(-22, 22)
plt.ylim(-22, 22)

plt.grid(True)
plt.title('Lingkaran (r = 20) - Midpoint Algorithm')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
