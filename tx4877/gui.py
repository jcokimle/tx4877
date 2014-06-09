from tkinter import LabelFrame, ttk
import tkinter

from core import Core


class Gui(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.core = Core()
        self.grid()
        
        notebook = ttk.Notebook(self, padding=(5,5,5,5))
        self.p1 = ttk.Frame(notebook, width=500, padding=(10,5,10,5))
        self.p2 = ttk.Frame(notebook, padding=(10,5,10,5))
        self.p3 = ttk.Frame(notebook, padding=(10,5,10,5))
        notebook.add(self.p1, text='Miller Rabin')
        notebook.add(self.p2, text='Pm1 Pollard')
        notebook.add(self.p3, text='Prime Gen')
        notebook.grid(column=0,row=0)
        
        self.init_miller_rabin()
        self.init_pm1_pollard()
        self.init_prime_gen()
        
        self.grid_columnconfigure(0,weight=1)
        self.update()
        self.geometry(self.geometry())

    def init_miller_rabin(self):
        page = self.p1
        
        self.n = tkinter.IntVar()
        self.entry_n = tkinter.Entry(page,textvariable=self.n,width=100)
        self.entry_n.grid(column=1,row=0,sticky='EW')
        
        self.k = tkinter.IntVar()
        self.k.set(10)
        self.entry_k = tkinter.Entry(page,textvariable=self.k)
        self.entry_k.grid(column=1,row=1,sticky='EW')
        
        self.result = tkinter.StringVar()
        self.entry_result = tkinter.Entry(page,textvariable=self.result)
        self.entry_result.grid(column=1,row=2,sticky='EW')
        
        button = tkinter.Button(page,text=u"Run",command=self.run_miller_rabin)
        button.grid(column=0,row=3)
        
        self.label_variable_n = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_n,anchor="w")
        label.grid(column=0,row=0,sticky='EW')
        self.label_variable_n.set(u"N")
        
        self.label_variable_k = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_k,anchor="w")
        label.grid(column=0,row=1,sticky='EW')
        self.label_variable_k.set(u"K")
        
        self.label_variable_res = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_res,anchor="w")
        label.grid(column=0,row=2,sticky='EW')
        self.label_variable_res.set(u"Result")

    def init_pm1_pollard(self):
        page = self.p2
        
        self.n_pm1 = tkinter.IntVar()
        self.n_pm1.set(1)
        self.entry_n_pm1 = tkinter.Entry(page,textvariable=self.n_pm1,width=100)
        self.entry_n_pm1.grid(column=1,row=0,sticky='EW')
        
        self.b = tkinter.IntVar()
        self.entry_b = tkinter.Entry(page,textvariable=self.b)
        self.entry_b.grid(column=1,row=1,sticky='EW')
        
        self.it = tkinter.IntVar()
        self.it.set(10)
        self.entry_it = tkinter.Entry(page,textvariable=self.it)
        self.entry_it.grid(column=1,row=2,sticky='EW')
        
        self.result_pm1 = tkinter.StringVar()
        self.entry_result_pm1 = tkinter.Entry(page,textvariable=self.result_pm1)
        self.entry_result_pm1.grid(column=1,row=3,sticky='EW')
        
        button_pm1_pollard = tkinter.Button(page,text=u"Run",command=self.run_pm1_pollard)
        button_pm1_pollard.grid(column=0,row=4)
        
        self.label_variable_n = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_n,anchor="w")
        label.grid(column=0,row=0,sticky='EW')
        self.label_variable_n.set(u"N")
        
        self.label_variable_k = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_k,anchor="w")
        label.grid(column=0,row=1,sticky='EW')
        self.label_variable_k.set(u"B")
        
        self.label_variable_it = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_it,anchor="w")
        label.grid(column=0,row=2,sticky='EW')
        self.label_variable_it.set(u"IT")
        
        self.label_variable_res_pm1 = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_res_pm1,anchor="w")
        label.grid(column=0,row=3,sticky='EW')
        self.label_variable_res_pm1.set(u"Result")

    def init_prime_gen(self):
        page = self.p3
        
        self.size_alea = tkinter.IntVar()
        self.size_alea.set(1)
        self.entry_size_alea = tkinter.Entry(page,textvariable=self.size_alea)
        self.entry_size_alea.grid(column=1,row=0,sticky='EW')
        
        self.alea = tkinter.StringVar()
        self.entry_alea = tkinter.Entry(page,textvariable=self.alea,width=100)
        self.entry_alea.grid(column=1,row=1,sticky='EW')
        
        self.label_variable_size_alea = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_size_alea,anchor="w")
        label.grid(column=0,row=0,sticky='EW')
        self.label_variable_size_alea.set(u"Size")
        
        self.label_variable_gen = tkinter.StringVar()
        label = tkinter.Label(page,textvariable=self.label_variable_gen,anchor="w")
        label.grid(column=0,row=1,sticky='EW')
        self.label_variable_gen.set(u"Result")
        
        button_prime_gen = tkinter.Button(page,text=u"Run",command=self.generate)
        button_prime_gen.grid(column=0,row=2)

    def run_miller_rabin(self):
        try:
            n = self.n.get()
            k = self.k.get()
        except ValueError:
            self.result.set("Error")
            return
        if self.core.miller_rabin(n, k):
            self.result.set("Prime")
        else:
            self.result.set("Not prime")
        return
        
    def generate(self):
        try:
            size_alea = self.size_alea.get()
        except ValueError:
            self.alea.set("Error")
            return
        self.alea.set(self.core.prime_gen(size_alea))
        return
        
    def run_pm1_pollard(self):
        try:
            n = self.n_pm1.get()
            b = self.b.get()
            it = self.it.get()
            if b >= n:
                raise ValueError
        except ValueError:
            self.result_pm1.set("Error")
            return
        result = self.core.pm1_pollard(n, b, it)
        if result == 0:
            self.result_pm1.set("Factorization failed")
        else:
            self.result_pm1.set(result)
        return

if __name__ == "__main__":
    app = Gui(None)
    app.title('My application')
    app.mainloop()
    
