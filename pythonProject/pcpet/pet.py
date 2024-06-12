import tkinter as tk
import random

class DesktopPet:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.master.title("Desktop Pet")

        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.pack()

        self.pet_images = [
            tk.PhotoImage(file="pic1.png"),
            # tk.PhotoImage(file="pet2.gif")
        ]

        self.pet = self.canvas.create_image(100, 100, anchor=tk.CENTER, image=random.choice(self.pet_images))

        self.master.bind("<Motion>", self.move_pet)

    def move_pet(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.pet, x, y)

def main():
    root = tk.Tk()
    pet_app = DesktopPet(root)
    root.mainloop()

if __name__ == "__main__":
    main()