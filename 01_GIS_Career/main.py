from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA = Path(__file__).parent / "data" / "coastline_samples.csv"

def classify_change(change_m):
    if change_m < -1:
        return "Abrasi"
    if change_m > 1:
        return "Akresi"
    return "Relatif stabil"

def main():
    df = pd.read_csv(DATA)
    df["perubahan_m"] = df["posisi_2025_m"] - df["posisi_2020_m"]
    df["kategori"] = df["perubahan_m"].apply(classify_change)
    print("Ringkasan perubahan garis pantai (data simulasi)")
    print(df[["lokasi", "perubahan_m", "kategori"]].to_string(index=False))
    print("\nRata-rata perubahan:", round(df["perubahan_m"].mean(), 2), "meter")
    ax = df.plot(x="lokasi", y="perubahan_m", kind="bar", legend=False,
                 title="Perubahan Posisi Garis Pantai 2020–2025")
    ax.set_ylabel("Perubahan (meter); negatif = mundur ke darat")
    ax.set_xlabel("Lokasi sampel")
    plt.tight_layout()
    output = Path(__file__).parent / "hasil_perubahan_pantai.png"
    plt.savefig(output, dpi=150)
    print(f"Grafik disimpan: {output.name}")

if __name__ == "__main__":
    main()
