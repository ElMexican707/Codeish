import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, ROUND_HALF_UP

def calculate_costs():
    try:
        competition_fee = Decimal(entry_competition_fee.get())
        housing_fee = Decimal(entry_housing_fee.get())
        total_people = int(entry_total_people.get())
        competing_people = int(entry_competing_people.get())

        non_competing_people = total_people - competing_people

        if competing_people > 0:
            comp_fee_per_person = (competition_fee / competing_people).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            housing_fee_per_person = (housing_fee / total_people).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            cost_per_competing = comp_fee_per_person + housing_fee_per_person
        else:
            cost_per_competing = (housing_fee / total_people).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        cost_per_non_competing = (housing_fee / total_people).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        cost_per_competing = cost_per_competing.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        cost_per_non_competing = cost_per_non_competing.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        label_result_competing.config(text=f"The cost per competing person is: ${cost_per_competing:.2f}")
        label_result_non_competing.config(text=f"The cost per non-competing person is: ${cost_per_non_competing:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

root = tk.Tk()
root.title("Shit Calc Thing™")

label_competition_fee = tk.Label(root, text="Competition Fee:")
label_competition_fee.grid(row=0, column=0, padx=10, pady=5)
entry_competition_fee = tk.Entry(root)
entry_competition_fee.grid(row=0, column=1, padx=10, pady=5)
entry_competition_fee.insert(0, "1000")

label_housing_fee = tk.Label(root, text="Housing Fee:")
label_housing_fee.grid(row=1, column=0, padx=10, pady=5)
entry_housing_fee = tk.Entry(root)
entry_housing_fee.grid(row=1, column=1, padx=10, pady=5)
entry_housing_fee.insert(0, "900")

label_total_people = tk.Label(root, text="Total Number of People Attending:")
label_total_people.grid(row=2, column=0, padx=10, pady=5)
entry_total_people = tk.Entry(root)
entry_total_people.grid(row=2, column=1, padx=10, pady=5)
entry_total_people.insert(0, "9")

label_competing_people = tk.Label(root, text="Number of Competing People:")
label_competing_people.grid(row=3, column=0, padx=10, pady=5)
entry_competing_people = tk.Entry(root)
entry_competing_people.grid(row=3, column=1, padx=10, pady=5)
entry_competing_people.insert(0, "6")

button_calculate = tk.Button(root, text="Calculate", command=calculate_costs)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

label_result_competing = tk.Label(root, text="The cost per competing person is: $")
label_result_competing.grid(row=5, column=0, columnspan=2, pady=5)

label_result_non_competing = tk.Label(root, text="The cost per non-competing person is: $")
label_result_non_competing.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()