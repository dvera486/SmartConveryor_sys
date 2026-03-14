import tkinter as tk
from conveyor import Conveyor
from box import Box

class ConveyorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Smart Conveyor System Simulator')
        self.conveyor = Conveyor()

        self.speed_label = tk.Label(root, text='Speed: 10.0')
        self.speed_label.pack()
        self.box_count_label = tk.Label(root, text='Boxes: 0')
        self.box_count_label.pack()

        self.add_button = tk.Button(root, text='Add Box', command=self.add_box)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.remove_button = tk.Button(root, text='Remove Box', command=self.remove_box)
        self.remove_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.start_button = tk.Button(root, text='Start', command=self.start_conveyor)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button = tk.Button(root, text='Stop', command=self.stop_conveyor)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.running = True
    def start_conveyor(self):
        self.running = True
    def stop_conveyor(self):
        self.running = False

        # Canvas for conveyor visualization
        self.canvas_width = 400
        self.canvas_height = 100
        self.box_width = 40
        self.box_height = 40
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='lightgray')
        self.canvas.pack(pady=20)

        # Track box positions
        self.box_positions = []

        self.update_labels()
        self.animate()

    def add_box(self):
        self.conveyor.add_box(Box(weight=1.0))
        # Add new box at the start of the conveyor
        self.box_positions.append(0)
        self.update_labels()

    def remove_box(self):
        self.conveyor.remove_box()
        if self.box_positions:
            self.box_positions.pop()
        self.update_labels()

    def update_labels(self):
        self.speed_label.config(text=f'Speed: {self.conveyor.get_speed():.2f}')
        self.box_count_label.config(text=f'Boxes: {self.conveyor.get_box_count()}')

    def animate(self):
        if self.running:
            # Move boxes
            speed = self.conveyor.get_speed()
            for i in range(len(self.box_positions)):
                self.box_positions[i] += speed * 0.05  # Adjust multiplier for smoothness
                # Reset position if box reaches end
                if self.box_positions[i] > self.canvas_width - self.box_width:
                    self.box_positions[i] = 0

        # Draw conveyor and boxes
        self.canvas.delete('all')
        # Draw conveyor belt (rollers and stripes)
        belt_y = self.canvas_height//2
        belt_height = 30
        self.canvas.create_rectangle(0, belt_y-belt_height//2, self.canvas_width, belt_y+belt_height//2, fill='#444', outline='black')
        # Draw stripes
        for x in range(0, self.canvas_width, 40):
            self.canvas.create_rectangle(x, belt_y-belt_height//2, x+20, belt_y+belt_height//2, fill='#888', outline='')
        # Draw rollers
        roller_radius = 15
        self.canvas.create_oval(-roller_radius, belt_y-roller_radius, roller_radius, belt_y+roller_radius, fill='silver', outline='black')
        self.canvas.create_oval(self.canvas_width-roller_radius, belt_y-roller_radius, self.canvas_width+roller_radius, belt_y+roller_radius, fill='silver', outline='black')
        # Draw boxes
        for pos in self.box_positions:
            self.canvas.create_rectangle(pos, belt_y-self.box_height//2, pos+self.box_width, belt_y+self.box_height//2, fill='blue', outline='black')

        self.root.after(50, self.animate)

if __name__ == '__main__':
    root = tk.Tk()
    app = ConveyorApp(root)
    root.mainloop()
