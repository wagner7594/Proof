import customtkinter as ctk
  

#con clases

class principal(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("900x500")
		self.title("ventana")


	def crear_boton(self):
		self.bton = ctk.CTkButton(self)
		self.bton.pack()



app = principal()
app.mainloop()