import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

WIDTH, HEIGHT = 800, 700
FONT = 'Consolas', 14

mem_idx = 0
reg_idx = 0

main_core = Core(12, 4, 12, 16, {"layers":2,"sizes":[16,64]})

def interpret_command(command):
	return command

def append_output(event):
	out_field.config(state='normal')
	out_field.insert('end', f'{interpret_command(cmd_field.get())}\n\n')
	out_field.config(state='disabled')
	out_field.see('end')
	cmd_field.delete(0, 'end')

def memory_array():
	return ['Cache level 0', 'Cache level 1', 'RAM']

def register_array():
	return [f'Register {i}' for i in range(32)]

def find_in_memory_field(find_field, mem_field):
	find_field.delete(0, 'end')

def update_display(label, field, inc, mem):
	global mem_idx #ik, ik, i'll change it later
	global reg_idx

	marray = memory_array()
	rarray = register_array()

	if mem:
		mem_idx = min(max(mem_idx+inc, 0), len(marray)-1)
		val = marray[mem_idx]
	else:
		reg_idx = min(max(reg_idx+inc, 0), len(rarray)-1)
		val = rarray[reg_idx]

	label['text'] = val
	field.config(state='normal')
	field.delete('1.0', 'end')
	field.insert('end', val)
	field.config(state='disabled')

def get_cycle_count():
	return 0

root = tk.Tk()
root.title('AMMM v1.1')
root.geometry(f'{WIDTH}x{HEIGHT}')
# root.wm_state('zoomed')

tabs = ttk.Notebook(root, height=HEIGHT, width=WIDTH)

# COMMAND LINE
cmd_tab = tk.Frame(tabs)
cmd_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

cmd_label = tk.Label(cmd_tab, text='Enter a command:', font=FONT)
cmd_label.place(rely=0, relx=0, relheight=.05, relwidth=None)

cmd_field = tk.Entry(cmd_tab, font=FONT)
cmd_field.place(rely=.05, relx=0, relwidth=1, relheight=.05)
cmd_field.bind('<Return>', append_output)

out_label = tk.Label(cmd_tab, text='Output:', font=FONT)
out_label.place(rely=.12, relx=0, relheight=.05, relwidth=None)

out_field = scrolledtext.ScrolledText(cmd_tab, font=FONT)
out_field.place(rely=.18, relx=0, relheight=.82, relwidth=1)

# MEMORY TAB
mem_tab = tk.Frame(tabs)
mem_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

mem_label = tk.Label(mem_tab, font=FONT)
mem_label.place(rely=0, relx=0, relheight=.05, relwidth=1)

mem_field = scrolledtext.ScrolledText(mem_tab, font=FONT)
mem_field.place(rely=.05, relx=0, relheight=.8, relwidth=1)

update_display(mem_label, mem_field, 0, True)

find_label = tk.Label(mem_tab, text='Go to address', font=FONT)
find_label.place(rely=.8, relx=0, relheight=.05, relwidth=1)

back_btn = tk.Button(mem_tab, text='Go up', font=FONT, command=lambda: update_display(mem_label, mem_field, -1, True))
back_btn.place(rely=.85, relx=0, relheight=.05, relwidth=.33)

find_field = tk.Entry(mem_tab, font=FONT)
find_field.place(rely=.85, relx=.345, relheight=.05, relwidth=.30)
find_field.bind('<Return>', lambda event: find_in_memory_field(find_field, mem_field))

next_btn = tk.Button(mem_tab, text='Go down', font=FONT, command=lambda: update_display(mem_label, mem_field, 1, True))
next_btn.place(rely=.85, relx=.66, relheight=.05, relwidth=.33)

cache_int = tk.IntVar(value=1)
cache_check = tk.Checkbutton(mem_tab, text='Cache', variable=cache_int, command=lambda: None)
cache_check.place(rely=.95, relx=0, relheight=.05, relwidth=.5)

pipel_int = tk.IntVar(value=1)
pipel_check = tk.Checkbutton(mem_tab, text='Pipeline', variable=pipel_int, command=lambda: None)
pipel_check.place(rely=.95, relx=.5, relheight=.05, relwidth=.5)

# REGISTERS TAB
reg_tab = tk.Frame(tabs)
reg_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

reg_label = tk.Label(reg_tab, font=FONT)
reg_label.place(rely=0, relx=0, relheight=.05, relwidth=1)

reg_field = scrolledtext.ScrolledText(reg_tab, font=FONT)
reg_field.place(rely=.05, relx=0, relheight=.8, relwidth=1)

update_display(reg_label, reg_field, 0, False)

# find_reg_label = tk.Label(mem_tab, text='Go to address', font=FONT)
# find_reg_label.place(rely=.8, relx=0, relheight=.05, relwidth=1)

back_btn = tk.Button(reg_tab, text='Previous', font=FONT, command=lambda: update_display(reg_label, reg_field, -1, False))
back_btn.place(rely=.85, relx=0, relheight=.05, relwidth=.33)

# find_field = tk.Entry(mem_tab, font=FONT)
# find_field.place(rely=.85, relx=.345, relheight=.05, relwidth=.30)
# find_field.bind('<Return>', lambda event: find_in_memory_field(find_field, reg_field))

next_btn = tk.Button(reg_tab, text='Next', font=FONT, command=lambda: update_display(reg_label, reg_field, 1, False))
next_btn.place(rely=.85, relx=.66, relheight=.05, relwidth=.33)

# DIAGNOSTIC TAB
dia_tab = tk.Frame(tabs)

cycles_label = tk.Label(dia_tab, text=f'Cycles: {get_cycle_count()}', font=FONT)
cycles_label.place(rely=0, relx=0, relheight=.05, relwidth=1)

prompt_label = tk.Label(dia_tab, text=f'How many cycles to perform:', font=FONT)
prompt_label.place(rely=0.05, relx=0, relheight=.05, relwidth=1)

cycle_field = tk.Entry(dia_tab, font=FONT)
cycle_field.place(rely=0.1, relx=0, relheight=.05, relwidth=1)
cycle_field.bind('<Return>', lambda event: None)

# TAB CONTROL
tabs.add(cmd_tab, text='Command Line')
tabs.add(mem_tab, text='Memory')
tabs.add(reg_tab, text='Registers')
tabs.add(dia_tab, text='Diagnostic')
tabs.pack(expand=1, fill='both')

root.mainloop()