# Baca file ce.txt
with open("ce.txt", "r") as file:
    urls = file.readlines()

# Filter URL yang hanya punya tepat satu tanda '='
filtered = [url.strip() for url in urls if url.count('=') == 1]

# Simpan hasil ke file baru
with open("filtered.txt", "w") as out:
    out.write("\n".join(filtered))

print(f"{len(filtered)} URL disimpan ke 'filtered.txt' (hanya satu '=' per URL).")
