from tkinter import *
import math

# Criando os widgets:
e=""  # A string que aparece no display da calculadora, inicialmente vazia.
root = Tk()
root.title("Calculadora")
frame = Frame(root)
frame2 = Frame(root)
frame.pack(side=TOP)
frame2.pack(side=TOP)
lb = Label(frame,text="",width = 24,relief=RIDGE, font="Arial 12 bold",\
           fg="black")
lb.pack(fill=Y)
b0 = Button(frame2,text="0",bd=3,padx=1,pady=1, width=8, height=2)
b1 = Button(frame2,text="1",bd=3,padx=1,pady=1, width=8, height=2)
b2 = Button(frame2,text="2",bd=3,padx=1,pady=1, width=8, height=2)
b3 = Button(frame2,text="3",bd=3,padx=1,pady=1, width=8, height=2)
b4 = Button(frame2,text="4",bd=3,padx=1,pady=1, width=8, height=2)
b5 = Button(frame2,text="5",bd=3,padx=1,pady=1, width=8, height=2)
b6 = Button(frame2,text="6",bd=3,padx=1,pady=1, width=8, height=2)
b7 = Button(frame2,text="7",bd=3,padx=1,pady=1, width=8, height=2)
b8 = Button(frame2,text="8",bd=3,padx=1,pady=1, width=8, height=2)
b9 = Button(frame2,text="9",bd=3,padx=1,pady=1, width=8, height=2)
soma = Button(frame2,text="+",bd=3,padx=1,pady=1, width=8, height=2)
subtracao = Button(frame2,text="-",bd=3,padx=1,pady=1, width=8, height=2)
multiplicacao = Button(frame2,text="x",bd=3,padx=1,pady=1, width=8, height=2)
divisao = Button(frame2,text="/",bd=3,padx=1,pady=1, width=8, height=2)
resultado = Button(frame2,text="=",bd=3,padx=1,pady=1, width=8, height=2)
abreparents = Button(frame2,text="(",bd=3,padx=1,pady=1, width=8, height=2)
fechaparents = Button(frame2,text=")",bd=3,padx=1,pady=1, width=8, height=2)
limpar = Button(frame2,text="C",bd=3,padx=1,pady=1, width=8, height=2)
ponto = Button(frame2,text=".",bd=3,padx=1,pady=1, width=8, height=2)
parte = Button(frame2,text="1/x",bd=3,padx=1,pady=1, width=8, height=2)
reverso = Button(frame2,text="+-",bd=3,padx=1,pady=1, width=8, height=2)
elevar = Button(frame2,text="x2",bd=3,padx=1,pady=1, width=8, height=2)
raiz_q = Button(frame2,text="√",bd=3,padx=1,pady=1, width=8, height=2)
log = Button(frame2,text="log",bd=3,padx=1,pady=1, width=8, height=2)

sair = Button(frame2,text="OFF",bd=3,padx=1,pady=1, width=16, height=2,\
              command=root.quit)

# Packing:
limpar.grid(row=0,column=0)
reverso.grid(row=0,column=1)
ponto.grid(row=0,column=2)
divisao.grid(row=0,column=3)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
multiplicacao.grid(row=1,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
subtracao.grid(row=2,column=3)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
soma.grid(row=3,column=3)

abreparents.grid(row=4,column=0)
b0.grid(row=4,column=1)
fechaparents.grid(row=4,column=2)
resultado.grid(row=4,column=3)

elevar.grid(row=5,column=0)
parte.grid(row=5,column=1)
raiz_q.grid(row=5,column=2)
log.grid(row=5,column=3)

# Callbacks:
def digito(ev):
    global e,lb
    #remove os zeros à esquerda se o segundo caractere for dígito:
    if len(e) > 1 and e[1].isdigit():
        e = e.lstrip('0')
        lb.config(text=e)
    if ev.widget==b0:
        e+="0"
        lb.config(text=e)
    elif ev.widget==b1:
        e+="1"
        lb.config(text=e)        
    elif ev.widget==b2:
        e+="2"
        lb.config(text=e)
    elif ev.widget==b3:
        e+="3"
        lb.config(text=e)
    elif ev.widget==b4:
        e+="4"
        lb.config(text=e)
    elif ev.widget==b5:
        e+="5"
        lb.config(text=e)
    elif ev.widget==b6:
        e+="6"
        lb.config(text=e)
    elif ev.widget==b7:
        e+="7"
        lb.config(text=e)
    elif ev.widget==b8:
        e+="8"
        lb.config(text=e)
    else: 
        e+="9"
        lb.config(text=e)

def opera(ev):
    global e,lb
    if ev.widget==soma:
        e += "+"
        lb.config(text=e)
    elif ev.widget==subtracao:
        e += "-"
        lb.config(text=e)
    elif ev.widget==multiplicacao:
        e += "*"
        lb.config(text=e)
    elif ev.widget==divisao:
        e += "/"
        lb.config(text=e)
    elif ev.widget==ponto:
        e += "."
        lb.config(text=e)

def parenteses(ev):
    global e,lb
    if ev.widget==abreparents:
        e += "("
        lb.config(text=e)
    elif ev.widget==fechaparents:
        e += ")"
        lb.config(text=e)

# Tecla '=' acionada:
def finaliza(ev):
    global e,lb
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        e = ""
        lb.config(text="Erro!")
        

def clear(ev):
    global e,lb
    e = ""
    lb.config(text = e)

def convert(ev):
    global e,lb
    e += "*-1"
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        e = ""
        lb.config(text="Erro!")

def elevar_ao_quadrado(ev):
    global e,lb
    e += "**2"
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        e = ""
        lb.config(text="Erro!")
    
def divide_parte(ev):
    global e,lb
    e = "1/" + e
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        e = ""
        lb.config(text="Erro!")

def raiz_quadrada(ev):
    global e,lb
    e += "**0.5" 
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        e = ""
        lb.config(text="Erro!")


def calc_log(ev):
    global e,lb
    e = str(math.log10(float(e)))
    try:
        r = eval(e)  # a função eval lança exceção se não puder calcular
        e= str(r)
        lb.config(text= e)       
    except:
        e = ""
        lb.config(text="Erro!")        

# Binding:
b0.bind("<Button-1>",digito)
b1.bind("<Button-1>",digito)
b2.bind("<Button-1>",digito)
b3.bind("<Button-1>",digito)
b4.bind("<Button-1>",digito)
b5.bind("<Button-1>",digito)
b6.bind("<Button-1>",digito)
b7.bind("<Button-1>",digito)
b8.bind("<Button-1>",digito)
b9.bind("<Button-1>",digito)
soma.bind("<Button-1>",opera)
ponto.bind("<Button-1>",opera)
reverso.bind("<Button-1>",convert)
elevar.bind("<Button-1>",elevar_ao_quadrado)
raiz_q.bind("<Button-1>",raiz_quadrada)
log.bind("<Button-1>",calc_log)
parte.bind("<Button-1>",divide_parte)
subtracao.bind("<Button-1>",opera)
multiplicacao.bind("<Button-1>",opera)
divisao.bind("<Button-1>",opera)
abreparents.bind("<Button-1>",parenteses)
fechaparents.bind("<Button-1>",parenteses)
resultado.bind("<Button-1>",finaliza)
limpar.bind("<Button-1>",clear)


#Mainloop:
root.mainloop()

