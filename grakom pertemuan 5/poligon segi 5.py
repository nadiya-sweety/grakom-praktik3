
import matplotlib.pyplot as plt

# Daftar titik vertex segi lima
vertex = [(3, 5), (5, 3), (4, 1), (1, 1), (1, 3)]

# Memisahkan koordinat X dan Y
X = [p[0] for p in vertex + [vertex[0]]]
Y = [p[1] for p in vertex + [vertex[0]]]

# Membuat grafik
plt.figure(figsize=(6, 5))

# Menggambar garis dan titik segi lima
plt.plot(X, Y, color='deeppink', marker='o',
         markersize=8, linewidth=2)

# Memberikan warna pada bagian dalam
plt.fill(X, Y, color='pink', alpha=0.4)

# Memberikan label koordinat setiap vertex
for x, y in vertex:
    plt.annotate(
        f'({x}, {y})',
        (x, y),
        textcoords="offset points",
        xytext=(8, 8),
        ha='left',
        fontsize=9,
        color='deeppink'
    )

# Mengatur tampilan grafik
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xticks(range(0, 7))
plt.yticks(range(0, 7))

plt.grid(True)
plt.gca().set_aspect('equal')

plt.title('Poligon Segi Lima')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
