import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import time

class GUI:
    def __init__(self, core):
        self.core = core
        self.WIDTH = 800
        self.HEIGHT = 700
        self.FONT = 'Consolas', 14

        self.mem_idx = 0
        self.reg_idx = 0

        self.root = tk.Tk()
        self.root.title('AMMM v1.1')
        self.root.geometry(f'{self.WIDTH}x{self.HEIGHT}')
        # root.wm_state('zoomed')

        self.tabs = ttk.Notebook(self.root, height=self.HEIGHT, width=self.WIDTH)

        # COMMAND LINE
        self.cmd_tab = tk.Frame(self.tabs)
        self.cmd_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

        self.cmd_label = tk.Label(self.cmd_tab, text='Enter a command:', font=self.FONT)
        self.cmd_label.place(rely=0, relx=0, relheight=.05, relwidth=None)

        self.cmd_field = tk.Entry(self.cmd_tab, font=self.FONT)
        self.cmd_field.place(rely=.05, relx=0, relwidth=1, relheight=.05)
        self.cmd_field.bind('<Return>', self.append_output)

        self.out_label = tk.Label(self.cmd_tab, text='Output:', font=self.FONT)
        self.out_label.place(rely=.12, relx=0, relheight=.05, relwidth=None)

        self.out_field = scrolledtext.ScrolledText(self.cmd_tab, font=self.FONT)
        self.out_field.place(rely=.18, relx=0, relheight=.82, relwidth=1)

        # MEMORY TAB
        self.mem_tab = tk.Frame(self.tabs)
        self.mem_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

        self.mem_label = tk.Label(self.mem_tab, font=self.FONT)
        self.mem_label.place(rely=0, relx=0, relheight=.05, relwidth=1)

        self.mem_field = scrolledtext.ScrolledText(self.mem_tab, font=self.FONT)
        self.mem_field.place(rely=.05, relx=0, relheight=.8, relwidth=1)

        self.update_display(self.mem_label, self.mem_field, 0, True)

        self.find_label = tk.Label(self.mem_tab, text='Go to address', font=self.FONT)
        self.find_label.place(rely=.85, relx=0, relheight=.05, relwidth=1)

        self.back_btn = tk.Button(self.mem_tab, text='Go up', font=self.FONT, command=lambda: self.update_display(self.mem_label, self.mem_field, -1, True))
        self.back_btn.place(rely=.90, relx=0, relheight=.05, relwidth=.33)

        self.find_field = tk.Entry(self.mem_tab, font=self.FONT)
        self.find_field.place(rely=.90, relx=.345, relheight=.05, relwidth=.30)
        self.find_field.bind('<Return>', lambda event: self.find_in_memory_field(self.find_field, self.mem_field))

        self.next_btn = tk.Button(self.mem_tab, text='Go down', font=self.FONT, command=lambda: self.update_display(self.mem_label, self.mem_field, 1, True))
        self.next_btn.place(rely=.90, relx=.66, relheight=.05, relwidth=.33)

        self.cache_int = tk.IntVar(value=1)
        self.cache_check = tk.Checkbutton(self.mem_tab, text='Cache', variable=self.cache_int, command=lambda: self.core.memory.toggle_cache(True if self.cache_int.get() == 1 else False))
        self.cache_check.place(rely=.95, relx=0, relheight=.05, relwidth=.5)

        self.pipel_int = tk.IntVar(value=1)
        self.pipel_check = tk.Checkbutton(self.mem_tab, text='Pipeline', variable=self.pipel_int, command=lambda: self.core.pipeline.toggle_enabled(True if self.pipel_int.get() == 1 else False))
        self.pipel_check.place(rely=.95, relx=.5, relheight=.05, relwidth=.5)

        # REGISTERS TAB
        self.reg_tab = tk.Frame(self.tabs)
        self.reg_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

        self.reg_label = tk.Label(self.reg_tab, font=self.FONT)
        self.reg_label.place(rely=0, relx=0, relheight=.05, relwidth=1)

        self.reg_field = scrolledtext.ScrolledText(self.reg_tab, font=self.FONT)
        self.reg_field.place(rely=.05, relx=0, relheight=.8, relwidth=1)

        self.update_display(self.reg_label, self.reg_field, 0, False)

        self.back_btn = tk.Button(self.reg_tab, text='Previous', font=self.FONT, command=lambda: self.update_display(self.reg_label, self.reg_field, -1, False))
        self.back_btn.place(rely=.85, relx=0, relheight=.05, relwidth=.33)

        self.next_btn = tk.Button(self.reg_tab, text='Next', font=self.FONT, command=lambda: self.update_display(self.reg_label, self.reg_field, 1, False))
        self.next_btn.place(rely=.85, relx=.66, relheight=.05, relwidth=.33)

        # DIAGNOSTIC TAB
        self.dia_tab = tk.Frame(self.tabs)
        self.dia_tab.place(relx=.025, rely=.025, relwidth=.95, relheight=.95)

        self.cycles_label = tk.Label(self.dia_tab, font=self.FONT)
        self.cycles_label.place(rely=0, relx=0, relheight=.05, relwidth=1)

        self.update_cycle_count(self.cycles_label)

        self.cycles_prompt_label = tk.Label(self.dia_tab, text='How many cycles to run:', font=self.FONT)
        self.cycles_prompt_label.place(rely=.05, relx=0, relheight=.05, relwidth=1)

        self.cycles_field = tk.Entry(self.dia_tab, font=self.FONT)
        self.cycles_field.place(rely=.1, relx=0, relwidth=1, relheight=.05)
        self.cycles_field.bind('<Return>', lambda event: self.run_cycles(self.cycles_label, self.cycles_field))

        self.run_comp = tk.Button(self.dia_tab, text='Run to completion', font=self.FONT, command=lambda: self.run_until_done(self.cycles_label))
        self.run_comp.place(rely=.85, relx=.33, relheight=.05, relwidth=.33)

        # self.root.after(500, self.update_cycle_count, self.cycles_label)

        # PIPELINE TAB
        self.pip_tab = tk.Frame(self.tabs)

        self.pip_label = tk.Label(self.pip_tab, font=self.FONT, justify=tk.LEFT)
        self.pip_label.place(rely=0, relx=0, relheight=1, relwidth=1)

        self.pip_tab.after(500, self.update_pipeline_label, self.pip_label)

        # TAB CONTROL
        self.tabs.add(self.cmd_tab, text='Command Line')
        self.tabs.add(self.mem_tab, text='Memory')
        self.tabs.add(self.reg_tab, text='Registers')
        self.tabs.add(self.dia_tab, text='Diagnostic')
        self.tabs.add(self.pip_tab, text='Pipeline')
        self.tabs.pack(expand=1, fill='both')

    def start(self):
        self.root.mainloop()

    def append_output(self, event):
        self.out_field.config(state='normal')
        self.out_field.insert('end', f'{self.core.interpret_command(self.cmd_field.get())}\n')
        self.out_field.config(state='disabled')
        self.out_field.see('end')
        self.cmd_field.delete(0, 'end')

    def find_in_memory_field(self, find_field, mem_field):
        query = find_field.get()
        mem_field.see(str(float(int(query, 16 if 'x' in query else 10))))
        find_field.delete(0, 'end')

    def update_display(self, label, field, inc, mem):
        mtitles, marray = zip(*self.core.memory_array())
        rtitles, rarray = zip(*self.core.register_array())

        if mem:
            self.mem_idx = min(max(self.mem_idx+inc, 0), len(marray)-1)
            title = mtitles[self.mem_idx]
            val = marray[self.mem_idx]
        else:
            self.reg_idx = min(max(self.reg_idx+inc, 0), len(rarray)-1)
            title = rtitles[self.reg_idx]
            val = rarray[self.reg_idx]

        label['text'] = title
        field.config(state='normal')
        field.delete('1.0', 'end')
        field.insert('end', val)
        field.config(state='disabled')

    def update_cycle_count(self, cycles_label):
        cycles_label['text'] = f'Cycle count: {self.core.cycles}'
        self.root.after(500, self.update_cycle_count, self.cycles_label)

    def run_cycles(self, cycles_label, cycles_field):
        self.core.run_cycles(int(cycles_field.get()))
        self.update_cycle_count(cycles_label)
        self.dia_tab.update()

    def run_until_done(self, cycles_label):
        while format(self.core.status.read(), '032b')[31] != '1':
            self.core.pipeline.run_cycle(self.core.pc, self.core)
            self.core.cycles += 1
            self.update_cycle_count(cycles_label)
            self.dia_tab.update()
            # time.sleep(1)

    def update_pipeline_label(self, pip_label):
        p = self.core.pipeline
        f = p.fstage.instruction
        d = p.dstage.decoded
        e = p.estage.executed
        m = p.mstage.memorized
        w = p.wstage.written

        f = '' if (f is None or f[1] is None) else f[1]
        d = '' if (d is None or d[1] is None) else d[1]
        e = '' if (e is None or e[1] is None) else f'exec:{None if ("code" not in e[1]["execute"]) else e[1]["execute"]["code"]}, mem:{None if ("code" not in e[1]["memory"]) else e[1]["memory"]["code"]}, wrtb:{None if ("code" not in e[1]["writeback"]) else e[1]["writeback"]["code"]}'
        m = '' if (m is None or m[1] is None) else f'exec:{None if ("code" not in m[1]["execute"]) else m[1]["execute"]["code"]}, mem:{None if ("code" not in m[1]["memory"]) else m[1]["memory"]["code"]}, wrtb:{None if ("code" not in m[1]["writeback"]) else m[1]["writeback"]["code"]}'
        w = '' if (w is None or w[1] is None) else f'exec:{None if ("code" not in w[1]["execute"]) else w[1]["execute"]["code"]}, mem:{None if ("code" not in w[1]["memory"]) else w[1]["memory"]["code"]}, wrtb:{None if ("code" not in w[1]["writeback"]) else w[1]["writeback"]["code"]}'


        pip_label['text'] = f'Write Back:\t{w}\nMemory:\t\t{m}\nExecute:\t{e}\nDecode:\t\t{d}\nFetch:\t\t{f}'
        self.pip_tab.update()
        self.pip_tab.after(500, self.update_pipeline_label, pip_label)