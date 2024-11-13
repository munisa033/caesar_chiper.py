import tkinter as tk
from tkinter import messagebox

# Fungsi untuk enkripsi dengan Caesar Cipher
def encrypt(text, shift):
    result = ""
    # Lakukan pergeseran karakter satu per satu
    for i in range(len(text)):
        char = text[i]
        # Encrypt hanya huruf alfabet
        if char.isalpha():
            # Pergeseran untuk huruf besar (A-Z)
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            # Pergeseran untuk huruf kecil (a-z)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Fungsi untuk dekripsi dengan Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Fungsi untuk menangani tombol Enkripsi
def handle_encrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        encrypted_text = encrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")

# Fungsi untuk menangani tombol Dekripsi
def handle_decrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        decrypted_text = decrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")

# Membuat GUI menggunakan tkinter
window = tk.Tk()
window.title("Caesar Cipher - Enkripsi & Dekripsi")

# Label dan input untuk teks
tk.Label(window, text="Masukkan Teks:").grid(row=0, column=0, padx=10, pady=10)
input_text = tk.Text(window, height=5, width=40)
input_text.grid(row=0, column=1, padx=10, pady=10)

# Label dan input untuk shift
tk.Label(window, text="Kunci Shift:").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(window)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

# Tombol Enkripsi dan Dekripsi
encrypt_button = tk.Button(window, text="Enkripsi", command=handle_encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(window, text="Dekripsi", command=handle_decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Output teks
tk.Label(window, text="Hasil:").grid(row=3, column=0, padx=10, pady=10)
output_text = tk.Text(window, height=5, width=40)
output_text.grid(row=3, column=1, padx=10, pady=10)

# Jalankan aplikasi GUI
window.mainloop()
