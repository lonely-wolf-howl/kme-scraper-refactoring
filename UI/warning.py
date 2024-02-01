import customtkinter as ctk


class WarningUI:
    def __init__(self, message):
        self.message = message

    def show_warning(self):
        root = ctk.CTk()
        root.title("경고")
        root.geometry("200x100")

        ctk.set_appearance_mode("dark")  # system, dark, light
        ctk.set_default_color_theme("blue")  # blue(standard), green, dark-blue

        font_style = ctk.CTkFont("돋움", size=13)

        notice_label = ctk.CTkLabel(root, text=self.message, font=font_style)
        notice_label.pack(fill="both", expand=True)

        root.mainloop()
