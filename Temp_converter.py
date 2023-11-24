import tkinter as tk


def temprature_F2C(temp):
    try:
        num_tempf = float(temp)
        converted_tempc = (((5 * num_tempf) - 160) / 9)
        converted_tempc = ("%.2f" % round(converted_tempc, 2))
        return converted_tempc, "C"

    except:
        return "Enter numbers only"


def temprature_C2F(temp):
    try:
        num_tempc = float(temp)
        converted_tempf = (((9 * num_tempc) + 160) / 5)
        converted_tempf = ("%.2f" % round(converted_tempf, 2))
        return converted_tempf, "F"

    except:
        return "Enter numbers only"


def get_tempF(temp):
    global ans
    ans.config(text=temprature_C2F(temp))


def get_tempC(temp):
    global ans
    ans.config(text=temprature_F2C(temp))


def main():
    # Create window
    window = tk.Tk()
    window.title("Ido's TempConverter")

    # Create main label
    frame = tk.Canvas(window, width=500, height=500).pack()
    tk.Label(frame, text="Fahrenheit and Celsius Converter", font=("Segoe UI Semilight", 24, "bold"), bg="red",
             fg="white").place(relwidth=1, relheight=0.2)

    # Create Temp input label and entry
    tk.Label(frame, text="Enter Temprature:", font=("Segoe UI Semilight", 18)).place(rely=0.28, relx=0.1,
                                                                                     relwidth=0.4, relheight=0.05)
    tempinput = tk.Entry(frame, width=30, justify="center", font=("Segoe UI Semilight", 12))
    tempinput.place(rely=0.28, relx=0.5, relwidth=0.4, relheight=0.05)

    # Convert buttons
    convertButtonF = tk.Button(frame, cursor="hand2", text="Convert Celsius to Fahrenheit",
                               font=("Segoe UI Semilight", 16), fg="black",
                               bg="pink", command=lambda: get_tempF(tempinput.get()))
    convertButtonC = tk.Button(frame, cursor="hand2", text="Convert Fahrenheit to Celsius",
                               font=("Segoe UI Semilight", 16), fg="black",
                               bg="pink", command=lambda: get_tempC(tempinput.get()))
    convertButtonF.place(relwidth=0.45, relheight=0.15, relx=0.03, rely=0.4)
    convertButtonC.place(relwidth=0.45, relheight=0.15, relx=0.52, rely=0.4)

    # Answer label
    global ans
    ans = tk.Label(window, bg="gray", text="Answer", font=("Segoe UI Semilight", 16))
    ans.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.15)

    # Quit button
    tk.Button(frame, text="Exit", fg="red", font=("Segoe UI Semilight", 18), command=window.quit).place(relx=0.8,
                                                                                                        rely=0.9,
                                                                                                        relheight=0.08,
                                                                                                        relwidth=0.2)

    window.mainloop()


if __name__ == "__main__":
    main()
