import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x300")
app.title("Exemplo de Botões para Entry")

# Criando o campo Entry
entry = ctk.CTkEntry(app, width=250, height=40, font=("Arial", 16))
entry.pack(pady=30)

# Função que insere o texto no final do Entry
def inserir_tecla(tecla):
    entry.insert(ctk.END, tecla)

# Criando um frame para organizar os botões
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10)

# Botões simulando um teclado (A, B, C)
btn_a = ctk.CTkButton(frame_botoes, text="A", width=50, command=lambda: inserir_tecla("A"))
btn_a.grid(row=0, column=0, padx=5)

btn_b = ctk.CTkButton(frame_botoes, text="B", width=50, command=lambda: inserir_tecla("B"))
btn_b.grid(row=0, column=1, padx=5)

btn_c = ctk.CTkButton(frame_botoes, text="C", width=50, command=lambda: inserir_tecla("C"))
btn_c.grid(row=0, column=2, padx=5)

# Botão para apagar o último caractere (Backspace)
def apagar():
    current_text = entry.get()
    if current_text:
        entry.delete(len(current_text) - 1, ctk.END)

btn_apagar = ctk.CTkButton(app, text="Apagar", fg_color="red", hover_color="darkred", command=apagar)
btn_apagar.pack(pady=10)

app.mainloop()