import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
import base64

class DESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Encryption Standard (DES)")

        self.label_key = tk.Label(root, text="Key (8 bytes):")
        self.label_key.pack()

        self.entry_key = tk.Entry(root, width=50)
        self.entry_key.pack()

        self.label_input = tk.Label(root, text="Input Text:")
        self.label_input.pack()

        self.text_input = tk.Text(root, height=10, width=50)
        self.text_input.pack()

        self.label_output = tk.Label(root, text="Output Text:")
        self.label_output.pack()

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack()

        self.button_encrypt = tk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.button_encrypt.pack()

        self.button_decrypt = tk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.button_decrypt.pack()

    def encrypt_text(self):
        key = self.entry_key.get().encode('utf-8')
        input_text = self.text_input.get("1.0", tk.END).strip()

        if len(key) != 8:
            messagebox.showerror("Error", "Key must be 8 bytes long.")
            return

        cipher = DES.new(key, DES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(input_text.encode('utf-8'), DES.block_size))
        iv = cipher.iv
        encrypted_text = base64.b64encode(iv + ct_bytes).decode('utf-8')

        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        key = self.entry_key.get().encode('utf-8')
        input_text = self.text_input.get("1.0", tk.END).strip()

        if len(key) != 8:
            messagebox.showerror("Error", "Key must be 8 bytes long.")
            return

        try:
            raw = base64.b64decode(input_text)
            iv = raw[:DES.block_size]
            ct = raw[DES.block_size:]
            cipher = DES.new(key, DES.MODE_CBC, iv)
            decrypted_text = unpad(cipher.decrypt(ct), DES.block_size).decode('utf-8')

            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", "Decryption failed. Please check your input.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DESApp(root)
    root.mainloop()