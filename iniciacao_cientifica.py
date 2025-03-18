import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# funções
def importar_imagem():
    arquivo = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if arquivo:
        imagem_original = Image.open(arquivo)
        
        imagem_redimensionada = imagem_original.resize((450, 560))
        
        imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
        
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk

def ajustar_imagem():
    print("Ajustar imagem")

def salvar_imagem():
    arquivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("Todos os arquivos", "*.*")])
    print(f"Imagem salva em: {arquivo}")

# código
root = tk.Tk()
root.title("Interface de Imagem")
root.geometry("500x500")
root.configure(bg='black')

label_imagem = tk.Label(root, bg='black')
label_imagem.place(relx=0.5, rely=0.4, anchor='center')

button_width = 20
button_height = 2

botao_importar = tk.Button(root, text="Importar imagem", command=importar_imagem, width=button_width, height=button_height)
botao_ajustar = tk.Button(root, text="Ajustar imagem", command=ajustar_imagem, width=button_width, height=button_height)
botao_salvar = tk.Button(root, text="Salvar imagem", command=salvar_imagem, width=button_width, height=button_height)

botao_salvar.pack(side=tk.BOTTOM, anchor='w', padx=30, pady=5)
botao_ajustar.pack(side=tk.BOTTOM, anchor='w', padx=30, pady=5)
botao_importar.pack(side=tk.BOTTOM, anchor='w', padx=30, pady=5)

root.mainloop()
