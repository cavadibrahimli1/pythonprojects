import turtle  #for making screen and turtle actions
import pandas  #for working csv file

#screen alignment
screen = turtle.Screen()
screen.title("U.S. States quiz by Javad Ibrahimli") #quiz 
image = "blank_states_img.gif" 
screen.addshape(image) 
turtle.shape(image)

data = pandas.read_csv("50_states.csv")  #importing data to a variable
all_states = data.state.to_list() 
guessed_states = [] #list for guessed states

while len(guessed_states) < 50: #main game algorithm
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="Write the name of the state").title()
    if answer_state == "Exit": 
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:  #writing the name of the state on Map
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
