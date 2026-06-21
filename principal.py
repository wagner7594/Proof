import customtkinter as ctk
  
class Principal(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("900x500")
		self.title("Principal")


	def crear_boton(self):
		self.bton = ctk.CTkButton(self)
		self.bton.pack()

	def final(self):
		self.mainloop()

