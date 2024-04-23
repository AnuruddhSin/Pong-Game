# from turtle import Turtle
# #starting_postion=[(280,0),(280,-20),(280,20)]
# #Move_distance=20

   
# class Pong:
        
#     def __init__(self,position):
#         #self.all_pong_part=[]
#         self.create_pong()
#         self.new_create_pong()
#         #self.head=self.all_pong_part[]
#     def create_pong(self):
            
#             self.tim=Turtle(shape="square")
#             self.tim.color("white")
#             self.tim.penup()
            
#             self.tim.shapesize(stretch_wid=5,stretch_len=1)
#             self.tim.goto(280,0)
#             self.tim.speed("fastest")
#             self.goto(position)
#            # self.all_pong_part.append(tim)

#     def new_create_pong(self):
            
#             self.new_tim=Turtle(shape="square")
#             self.new_tim.color("white")
#             self.new_tim.penup()
            
#             self.new_tim.shapesize(stretch_wid=5,stretch_len=1)
#             self.new_tim.goto(-280,0)
#             self.new_tim.speed("fastest")
#     # def move(self):
#     #             for seg_pong_part in range(len(self.all_pong_part)-1,0,-1):
#     #                 new_x=self.all_pong_part[seg_pong_part].xcor()
#     #                 new_y=self.all_pong_part[seg_pong_part].ycor() 
#     #                 self.all_pong_part[seg_pong_part].goto(new_x,new_y)
                 

    
#     def w(self):
#  #       if self.head.heading()!=DOWN:
#            # self.tim.setheading(UP)
#             self.new_tim.goto(self.new_tim.xcor(),self.new_tim.ycor()+20)
#             # self.tim.speed(0) 
#             # self.tim.fd(Move_distance)

#     def s(self):
# #        if self.head.heading()!=UP:
#           #  self.tim.setheading(DOWN)
#             self.new_tim.goto(self.new_tim.xcor(),self.new_tim.ycor()-20)
#             # self.tim.speed(0) 
#             # self.tim.fd(Move_distance)        
              
#     def up(self):
#  #       if self.head.heading()!=DOWN:
#            # self.tim.setheading(UP)
#             self.tim.goto(self.tim.xcor(),self.tim.ycor()+20)
#             # self.tim.speed(0) 
#             # self.tim.fd(Move_distance)

#     def down(self):
# #        if self.head.heading()!=UP:
#           #  self.tim.setheading(DOWN)
#             self.tim.goto(self.tim.xcor(),self.tim.ycor()-20)
#             # self.tim.speed(0) 
#             # self.tim.fd(Move_distance)           


from turtle import Turtle

class Pong(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)            