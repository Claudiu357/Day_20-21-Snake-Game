from turtle import Turtle


class Snake:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.segments = []
        for position in self.STARTING_POSITIONS:
            self.new_segment = Turtle(shape="square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(position)
            self.segments.append(self.new_segment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(20)