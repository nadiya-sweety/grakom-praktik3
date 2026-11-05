
import matplotlib.pyplot as plt

# Fungsi untuk membuat lingkaran menggunakan algoritma Midpoint
def midpoint_circle(xc, yc, r):

    # Menentukan titik awal lingkaran
    x, y = 0, r

    # Menghitung nilai awal parameter keputusan
    d = 1 - r

    # Menyiapkan list untuk menyimpan koordinat titik
    points = []

    # Perulangan selama nilai x tidak melebihi y
    while x <= y:

        # Menghasilkan 8 titik simetri lingkaran
        for px, py in [
            (x, y), (y, x), (-x, y), (-y, x),
            (x, -y), (y, -x), (-x, -y), (-y, -x)
        ]:

            # Menambahkan koordinat titik ke dalam list
            points.append((xc + px, yc + py))

        # Memeriksa nilai parameter keputusan
        if d < 0:

            # Jika negatif, pilih titik berikutnya ke arah kanan
            d = d + 2 * x + 3

        else:

            # Jika positif atau nol, pilih titik diagonal
            d = d + 2 * (x - y) + 5

            # Mengurangi nilai y
            y -= 1

        # Menambah nilai x
        x += 1

    # Mengembalikan seluruh koordinat titik lingkaran
    return points


# Menggambar lingkaran dengan jari-jari 5
pts = midpoint_circle(0, 0, 5)

# Memisahkan koordinat X dan Y
x, y = zip(*pts)

# Membuat area gambar berukuran 5 x 5
plt.figure(figsize=(5, 5))

# Menggambar titik lingkaran dengan warna merah
plt.scatter(x, y, s=60, c='red')

# Menyamakan skala sumbu X dan Y serta menampilkan grid
plt.axis('equal')
plt.grid(True)

# Memberikan judul grafik
plt.title('Lingkaran (r = 5) - Midpoint Algorithm')

# Memberikan nama pada sumbu koordinat
plt.xlabel('X')
plt.ylabel('Y')

# Menampilkan hasil gambar lingkaran
plt.show()
