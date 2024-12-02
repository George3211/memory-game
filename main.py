import tkinter as tk

def on_square_click(event):
    current_color = event.widget.cget("bg")
    new_color = "white" if current_color == "lightgray" else "lightgray"
    event.widget.config(bg=new_color)

root = tk.Tk()
root.title("24 Squares Board")

board_frame = tk.Frame(root)
board_frame.pack()

for i in range(4):
    for j in range(6):
        square = tk.Label(board_frame, bg="lightgray", width=10, height=5, borderwidth=1, relief="solid")
        square.grid(row=i, column=j, padx=6, pady=6)
        square.bind("<Button-1>", on_square_click)

root.mainloop()