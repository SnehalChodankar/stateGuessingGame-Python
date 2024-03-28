import turtle

import pandas

screen = turtle.Screen()
screen.title("States Game")
img = "./India_States.gif"
screen.addshape(img)
turtle.shape(img)

guessed_states = []
missed_states = []
total_states = 0
guess_count = 0


def write_to_image(state_name, xcor, ycor):
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.color("black")

    writer.goto(int(xcor), int(ycor))
    writer.write(state_name)


def check_if_guess_left():
    print(len(guessed_states))
    print(guess_count)
    if len(guessed_states) < total_states and guess_count < total_states:
        return True
    else:
        return False


def generate_missed_states():
    all_states = df_states_data["state"].to_list()
    # print(all_states)

    for state in all_states:
        if state not in guessed_states:
            missed_states.append(state)

    missed_states_df = pandas.DataFrame(missed_states)
    missed_states_df.to_csv("./missed_states.csv")


guess_left = True
while guess_left:
    df_states_data = pandas.read_csv("./Indian_States.csv")
    # print(df_states_data.state.count())

    total_states = df_states_data.state.count()
    print(total_states)

    ans_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} States Correct",
                                 prompt="State Name: ").title()
    print(ans_state)

    if ans_state == "Exit":
        generate_missed_states()
        break

    ds_state = df_states_data[df_states_data["state"] == ans_state]
    # print(f"state: {ds_state}")
    # print(int(ds_state["x"]))
    # print(int(ds_state["y"]))

    if not ds_state.empty:
        print(True)

        guessed_states.append(ans_state)
        guess_count += 1

        state_x = ds_state.x.iloc[0]
        print(state_x)
        state_y = ds_state.y.iloc[0]
        print(state_y)
        # Write to the image with xy from file
        write_to_image(ans_state, state_x, state_y)

        state_x = state_y = 0
    else:
        print(False)
        guess_count += 1
        if not check_if_guess_left():
            guess_left = False


# # Needed for getting state coordinates
# def get_mouse_click_coor(x, y):
#     print(int(x), int(y))
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
