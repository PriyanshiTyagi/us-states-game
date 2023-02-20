import turtle
import pandas as pd

screen = turtle.Screen()
state_write = turtle.Turtle()
state_write.pu()
state_write.hideturtle()
screen.title("US States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
right_answers=[]
while len(right_answers)<50:
    user_answer = screen.textinput(title=f"{len(right_answers)}/50 Guess a state", prompt="What is the name of the state?").title()

    data = pd.read_csv("50_states.csv")
    states = data.state.to_list()
    if user_answer=="Exit":
        break

    if  user_answer in states:
        guessed_state_data = data[data.state == user_answer]
        state_write.setpos(int(guessed_state_data.x), int(guessed_state_data.y))
        state_write.write(user_answer)
        right_answers.append(user_answer)

left_states=[names for names in states if names not in right_answers]
df=pd.DataFrame(left_states)
df.to_csv("left_states.csv")
