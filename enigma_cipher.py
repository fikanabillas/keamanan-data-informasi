import tkinter as tk
from tkinter import messagebox

class EnigmaCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = self.shift % 26
                new_char = chr((ord(char) - 65 + shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift_amount) % 26 + 97)
                encrypted_text += new_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = self.shift % 26
                new_char = chr((ord(char) - 65 - shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift_amount) % 26 + 97)
                decrypted_text += new_char
            else:
                decrypted_text += char
        return decrypted_text

class EnigmaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enigma Cipher")

        self.cipher = EnigmaCipher(3)  # Shift 3 for example

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
        input_text = self.text_input.get("1.0", tk.END).strip()
        encrypted_text = self.cipher.encrypt(input_text)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        input_text = self.text_input.get("1.0", tk.END).strip()
        decrypted_text = self.cipher.decrypt(input_text)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, decrypted_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnigmaApp(root)
    root.mainloop()