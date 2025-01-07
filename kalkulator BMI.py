# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program kalkulator BMI

def hitung_bmi(berat, tinggi):
    """Menghitung BMI berdasarkan berat (kg) dan tinggi (m)."""
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    """Menentukan kategori berdasarkan nilai BMI."""
    if bmi < 18.5:
        return "Kurus (Underweight)"
    elif 18.5 <= bmi < 24.9:
        return "Normal (Healthy Weight)"
    elif 25 <= bmi < 29.9:
        return "Gemuk (Overweight)"
    else:
        return "Obesitas (Obesity)"

def main():
    print("Kalkulator BMI (Body Mass Index)")
    try:
        berat = float(input("Masukkan berat badan Anda (kg): "))
        tinggi = float(input("Masukkan tinggi badan Anda (cm): ")) / 100  #
        bmi = hitung_bmi(berat, tinggi)
        print(f"\nBMI Anda: {bmi:.2f}")
        print(f"Kategori: {kategori_bmi(bmi)}")
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka.")

main()