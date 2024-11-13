import tkinter as tk

class CaesarCipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Cipher Encryption Machine")

        # Judul
        self.title_label = tk.Label(master, text="Cipher Encryption Machine", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Pesan Selamat Datang
        self.welcome_label = tk.Label(master, text="Selamat datang di program enkripsi saya", font=("Helvetica", 12))
        self.welcome_label.pack(pady=5)

        # Frame untuk Input dan Output
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        # Bagian Input
        self.input_label = tk.Label(self.frame, text="Masukkan Teks:")
        self.input_label.grid(row=0, column=0)

        self.text_input = tk.Text(self.frame, height=10, width=30)
        self.text_input.grid(row=1, column=0)

        self.shift_label = tk.Label(self.frame, text="Masukkan Pergeseran (1-25):")
        self.shift_label.grid(row=2, column=0)

        self.shift_input = tk.Entry(self.frame)
        self.shift_input.grid(row=3, column=0)

        # Tombol untuk Enkripsi dan Dekripsi
        self.encrypt_button = tk.Button(self.frame, text="Enkripsi", command=self.encrypt)
        self.encrypt_button.grid(row=4, column=0)

        self.decrypt_button = tk.Button(self.frame, text="Dekripsi", command=self.decrypt)
        self.decrypt_button.grid(row=5, column=0)

        # Bagian Output
        self.output_label = tk.Label(self.frame, text="Hasil:")
        self.output_label.grid(row=0, column=1)

        self.result_output = tk.Text(self.frame, height=10, width=30)
        self.result_output.grid(row=1, column=1)

        # Menjalankan aplikasi
        self.result_output.config(state=tk.DISABLED)  # Disable output text box

    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - shift_base + shift) % 26 + shift_base
                result += chr(shifted)
            else:
                result += char
        return result

    def encrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        try:
            shift = int(self.shift_input.get())
            encrypted_text = self.caesar_cipher(text, shift)
            self.display_result(encrypted_text)
        except ValueError:
            self.display_result("Masukkan nilai pergeseran yang valid.")

    def decrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        try:
            shift = int(self.shift_input.get())
            decrypted_text = self.caesar_cipher(text, -shift)
            self.display_result(decrypted_text)
        except ValueError:
            self.display_result("Masukkan nilai pergeseran yang valid.")

    def display_result(self, result):
        self.result_output.config(state=tk.NORMAL)  # Enable output text box
        self.result_output.delete("1.0", tk.END)  # Clear previous output
        self.result_output.insert(tk.END, result)  # Insert new result
        self.result_output.config(state=tk.DISABLED)  # Disable output text box

# Membuat jendela utama
root = tk.Tk()
app = CaesarCipherApp(root)

# Menjalankan aplikasi
root.mainloop()