from box import Box

class Conveyor:
    def __init__(self):
        self.boxes = []
        self.base_speed = 10.0  # units per second
        self.speed = self.base_speed

    def add_box(self, box):
        self.boxes.append(box)
        self.update_speed()

    def remove_box(self):
        if self.boxes:
            self.boxes.pop()
            self.update_speed()

    def update_speed(self):
        total_weight = sum(box.weight for box in self.boxes)
        # Simple physics: speed decreases as weight increases
        self.speed = max(1.0, self.base_speed - 0.5 * total_weight)

    def get_speed(self):
        return self.speed

    def get_box_count(self):
        return len(self.boxes)
