import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.root.geometry("400x400")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Draw clock face
        self.canvas.create_oval(50, 50, 350, 350, outline="goldenrod2", width=4)
        self.draw_numbers()
        self.draw_second_ticks()

        # Draw clock hands
        self.hour_hand = self.canvas.create_line(200, 200, 200, 150, width=6, arrow=tk.LAST, fill="black")
        self.minute_hand = self.canvas.create_line(200, 200, 200, 100, width=4, arrow=tk.LAST, fill="blue")
        self.second_hand = self.canvas.create_line(200, 200, 200, 75, width=2, arrow=tk.LAST, fill="red")

        # Update clock
        self.update_clock()

    def draw_numbers(self):
        for i in range(1, 13):
            angle = math.radians(i * 30)
            x = 200 + 120 * math.sin(angle)
            y = 200 - 120 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Helvetica", 12), fill="black")

    def draw_second_ticks(self):
        for i in range(60):
            angle = math.radians(i * 6)
            x1 = 200 + 130 * math.sin(angle)
            y1 = 200 - 130 * math.cos(angle)
            x2 = 200 + 140 * math.sin(angle)
            y2 = 200 - 140 * math.cos(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=1, fill="black")

    def update_clock(self):
        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min
        hours = current_time.tm_hour % 12  # Convert 24-hour format to 12-hour format

        # Update hour hand
        hour_angle = math.radians((hours % 12) * 30 + minutes * 0.5)
        self.canvas.coords(self.hour_hand, 200, 200, 200 + 50 * math.sin(hour_angle), 200 - 50 * math.cos(hour_angle))

        # Update minute hand
        minute_angle = math.radians(minutes * 6 + seconds * 0.1)
        self.canvas.coords(self.minute_hand, 200, 200, 200 + 80 * math.sin(minute_angle), 200 - 80 * math.cos(minute_angle))

        # Update second hand
        second_angle = math.radians(seconds * 6)
        self.canvas.coords(self.second_hand, 200, 200, 200 + 90 * math.sin(second_angle), 200 - 90 * math.cos(second_angle))

        self.root.after(1000, self.update_clock)  # Update every 1000 milliseconds (1 second)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()


