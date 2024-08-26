import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
from tkcalendar import DateEntry
from Models.Paciente import Paciente
from Controladores import Doctor, Paciente, Cita
from DB.database import Database

class GestionMedicaApp:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Proyecto Gestión Médica")
        self.imagen = tk.PhotoImage(file="servicios_medicos.png")
        self.title_label = tk.Label(root, text="Citas Médicas", font=("Montserrat", 100, "bold italic"), bg="#264653",
                                    fg="white", compound="center", image=self.imagen)

        self.title_label.pack(pady=0)
        self.db = db
        self.controlador_doctor = Doctor.ControladorDoctor(self.db)
        self.controlador_paciente = Paciente.ControladorPaciente(self.db)
        self.controlador_citas = Cita.ControladorCita(self.db)
        self.centrar_ventana(root, 1000, 800)
        self.create_widgets()
    def centrar_ventana(self, ventana, ancho, altura):
        ancho_de_la_ventana = ventana.winfo_screenwidth()
        alto_de_la_ventana = ventana.winfo_screenheight()
        x = (ancho_de_la_ventana // 2) - (ancho // 2)
        y = (alto_de_la_ventana // 2) - (altura // 2)
        ventana.geometry(f"{ancho}x{altura}+{x}+{y}")
    def salir_del_programa(self):
        respuesta = messagebox.askokcancel("Salir", "¿Desea salir del programa?")
        if respuesta:
            root.quit()
        else:
            return self.root
    def create_widgets(self):
        self.menu_bar = tk.Menu(self.root)

        self.menu_morosidad = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_morosidad.add_command(label="Verificar Morosidad", command=self.abrir_ventana_registrar_paciente)
        self.menu_bar.add_cascade(label="Morosidad", menu=self.menu_morosidad)

        self.imagen_cita = tk.PhotoImage(file=r"Iconos\cita_medica.png")
        self.imagen_paciente = tk.PhotoImage(file=r"Iconos\usuarios.png")
        self.imagen_doctor = tk.PhotoImage(file=r"Iconos\doctor.png")
        self.imagen_especialidad = tk.PhotoImage(file=r"Iconos\especialidad.png")
        self.imagen_tratamiento = tk.PhotoImage(file=r"Iconos\tratamiento.png")
        self.imagen_salir = tk.PhotoImage(file=r"Iconos\salir.png")
        self.imagen_agregar = tk.PhotoImage(file=r"Iconos\agregar.png")
        self.imagen_eliminar = tk.PhotoImage(file=r"Iconos\eliminar.png")
        self.imagen_listar = tk.PhotoImage(file=r"Iconos\listar.png")
        self.imagen_regresar = tk.PhotoImage(file=r"Iconos\regresar.png")

        button = tk.Button(root, text="  Cita", command=self.abrir_ventana_citas, bg="white", fg="#3C372B",
                           font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                           image=self.imagen_cita)
        button.pack(pady=10)
        buttonu = tk.Button(root, text="  Paciente", command=self.abrir_ventana_pacientes, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_paciente)
        buttonu.pack(pady=10)
        buttonp = tk.Button(root, text="  Doctor", command=self.abrir_ventana_doctores, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_doctor)
        buttonp.pack(pady=10)
        buttonm = tk.Button(root, text="  Especialidad", command=self.abrir_ventana_especialidad, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_especialidad)
        buttonm.pack(pady=10)
        buttonm = tk.Button(root, text="  Tratamiento", command=self.abrir_ventana_tratamient, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_tratamiento)
        buttonm.pack(pady=10)
        buttonm = tk.Button(root, text="  Salir", command=self.salir_del_programa, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_salir)
        buttonm.pack(pady=10)


    def abrir_ventana_pacientes(self):
        ventana = Toplevel(self.root)
        ventana.title("Pacientes")
        ventana.config(bg="#119DA4")
        label = tk.Label(ventana, text="Pacientes", font=("Montserrat", 60, "bold italic"), fg="#3C372B",
                         bg="#119DA4", compound="center")
        label.pack(pady=10)
        self.centrar_ventana(ventana, 500, 500)

        button1 = tk.Button(ventana, text="  Agregar Paciente", command=self.abrir_ventana_registrar_paciente, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Paciente", command=self.abrir_ventana_eliminar_paciente, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Pacientes", command=self.abrir_ventana_ver_paciente, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button4 = tk.Button(ventana, text="  Modificar Paciente", command=self.abrir_ventana_modificar_paciente, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button3.pack(pady=10)
        button1.pack(pady=10)
        button4.pack(pady=10)
        button2.pack(pady=10)

        boton_regresar.pack(pady=10, padx=10, anchor="se")


    def abrir_ventana_registrar_paciente(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Paciente")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 830, 220)

        label_nombre = tk.Label(ventana, text="Nombre del paciente:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=0, column=0)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.config(width=25)
        entry_nombre.grid(row=0, column=1, padx=5)

        label_edad = tk.Label(ventana, text="Edad:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_edad.grid(row=1, column=0)

        entry_edad = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_edad.config(width=25)
        entry_edad.grid(row=1, column=1, padx=5)

        label_contacto = tk.Label(ventana, text="Contacto:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_contacto.grid(row=2, column=0)

        entry_contacto = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_contacto.config(width=25)
        entry_contacto.grid(row=2, column=1, padx=5)

        label_direccion = tk.Label(ventana, text="Direccion:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_direccion.grid(row=3, column=0)

        entry_direccion = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_direccion.config(width=25)
        entry_direccion.grid(row=3, column=1, padx=5)

        def add_paciente():
            nombre = entry_nombre.get()
            edad = entry_edad.get()
            contacto = entry_contacto.get()
            direccion = entry_direccion.get()

            if nombre and edad and contacto and direccion:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionPacientes @nombrePaciente = ?, @edad = ?, @contactoPaciente = ?, @direccion = ?",
                        (nombre, edad, contacto, direccion))
                    self.db.conn.commit()
                    messagebox.showinfo("Éxito", "Paciente agregado exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar paciente: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        boton_registrar = tk.Button(ventana, text="  Registrar Paciente", command=add_paciente, bg="white",
                                    fg="#3C372B", font=("Montserrat", 10, "bold italic"), width=225, height=25,
                                    compound="left", image=self.imagen_paciente)
        boton_registrar.grid(row=5, column=3, pady=5)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 15, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=2, pady=10, padx=10, sticky="w")
    def abrir_ventana_ver_paciente(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Pacientes")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_paciente.obtener_paciente()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"Nombre: {dato.get_nombrePaciente()}, Contacto: {dato.get_contactoPaciente()}, Direccion: {dato.get_direccion()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay citas para mostrar")

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_modificar_paciente(self):
        ventana = Toplevel(self.root)
        ventana.title("Modificar Paciente")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 600, 280)

        label_id = tk.Label(ventana, text="Id del paciente:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_id.grid(row=0, column=0)

        entry_id = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_id.config(width=25)
        entry_id.grid(row=0, column=1, padx=5)

        label_nombre = tk.Label(ventana, text="Nombre del paciente:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=1, column=0)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.config(width=25)
        entry_nombre.grid(row=1, column=1, padx=5)

        label_edad = tk.Label(ventana, text="Edad:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_edad.grid(row=2, column=0)

        entry_edad = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_edad.config(width=25)
        entry_edad.grid(row=2, column=1, padx=5)

        label_contacto = tk.Label(ventana, text="Contacto:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_contacto.grid(row=3, column=0)

        entry_contacto = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_contacto.config(width=25)
        entry_contacto.grid(row=3, column=1, padx=5)

        label_direccion = tk.Label(ventana, text="Direccion:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_direccion.grid(row=4, column=0)

        entry_direccion = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_direccion.config(width=25)
        entry_direccion.grid(row=4, column=1, padx=5)

        def mod_pac():

            if entry_id.get() and entry_nombre.get() and entry_edad.get() and entry_contacto.get() and entry_direccion.get():
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionPacientes  @idPaciente = ?, @nombrePaciente = ?, @edad = ?, @contactoPaciente = ?, @direccion = ?",
                        (entry_id.get(), entry_nombre.get(),entry_edad.get(), entry_contacto.get(), entry_direccion.get()))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Paciente modificada exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al modificar paciente: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Modificar Paciente", command=mod_pac, bg="white", fg="#3C372B",
                                    font=("Montserrat", 12, "bold italic"), width=225, height=30, compound="left", image=self.imagen_cita)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_eliminar_paciente(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Paciente")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        label = tk.Label(ventana, text="Seleccione un paciente:", bg="#119DA4", fg="#3C372B",
                         font=("Montserrat", 25, "bold italic"))
        label.grid(row=0, column=0, pady=5)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_paciente.obtener_paciente()
        datostemp = []
        if datos != []:
            for dato in datos:

                dato = f"{dato.get_idPaciente()}, Paciente: {dato.get_nombrePaciente()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)

        else:
            listbox.insert(tk.END, "No hay pacientes para mostrar")

        def del_cita():

            indice = listbox.curselection()

            if indice != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar al paciente?", message=", ".join(listbox.get(i) for i in indice)):
                    for idx in indice:
                        dato = datostemp[idx]
                        print(dato)
                        id = int(dato[0])

                self.db.cursor.execute("sp_GestionPacientes @idPaciente = ?, @nombrePaciente = null, @edad = null, @contactoPaciente = null, @direccion = null", (id))
                self.db.conn.commit()
                messagebox.showinfo("Éxito", "Paciente Eliminado Exitosamente.")
                ventana.destroy()

        boton_registrar = tk.Button(ventana, text="   Eliminar Paciente", command=del_cita, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_eliminar)
        boton_registrar.grid(row=5, column=0, pady=5)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")




    def abrir_ventana_doctores(self):
        ventana = Toplevel(self.root)
        ventana.title("Doctores")
        ventana.config(bg="#119DA4")
        label = tk.Label(ventana, text="Doctores", font=("Montserrat", 60, "bold italic"), fg="#3C372B",
                         bg="#119DA4", compound="center")
        label.pack(pady=10)
        self.centrar_ventana(ventana, 500, 500)

        button1 = tk.Button(ventana, text="  Agregar Doctor", command=self.abrir_ventana_registrar_doctor, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Doctor", command=self.abrir_ventana_eliminar_doctor, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Doctores", command=self.abrir_ventana_ver_doctor, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button4 = tk.Button(ventana, text="  Modificar Doctores", command=self.abrir_ventana_modificar_doctor, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button3.pack(pady=10)
        button1.pack(pady=10)
        button4.pack(pady=10)
        button2.pack(pady=10)

        boton_regresar.pack(pady=10, padx=10, anchor="se")
    def abrir_ventana_registrar_doctor(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Doctor")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 650, 300)

        label_nombre = tk.Label(ventana, text="Nombre del Doctor:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=0, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.grid(row=0, column=1, padx=5)

        label_contacto = tk.Label(ventana, text="Contacto:", bg="#119DA4", fg="#3C372B",
                                  font=("Montserrat", 20, "bold italic"))
        label_contacto.grid(row=1, column=0, padx=10, pady=10)

        entry_contacto = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_contacto.grid(row=1, column=1, padx=5)

        label_especialidad = tk.Label(ventana, text="Especialidad:", bg="#119DA4", fg="#3C372B",
                                      font=("Montserrat", 20, "bold italic"))
        label_especialidad.grid(row=2, column=0, padx=10, pady=10)

        combo_especialidad = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_especialidad.grid(row=2, column=1, padx=5)

        especialidades = self.controlador_doctor.obtener_especialidades()
        combo_especialidad['values'] = [es.get_nombreEspecialidad() for es in especialidades]
        combo_especialidad.especialidades = especialidades

        def add_doctor():
            nombre = entry_nombre.get()
            contacto = entry_contacto.get()
            especialidad_nombre = combo_especialidad.get()
            especialidad = next((es for es in combo_especialidad.especialidades if es.get_nombreEspecialidad() == especialidad_nombre), None)

            if nombre and especialidad and contacto:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarDoctores  @idEspecialidad = ?, @nombreDoctor = ?, @contacto = ?",
                        (especialidad.get_idEspecialidad(), nombre, contacto))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Doctor agregado exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar doctor: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Registrar Doctor", command=add_doctor, bg="white", fg="#3C372B",
                                    font=("Montserrat", 12, "bold italic"), width=225, height=30, compound="left", image=self.imagen_doctor)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_modificar_doctor(self):
        ventana = Toplevel(self.root)
        ventana.title("Modificar Doctor")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 650, 300)

        label_id = tk.Label(ventana, text="ID del Doctor:" ,  bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_id.grid(row=0, column=1, padx=5)

        label_nombre = tk.Label(ventana, text="Nombre del Doctor:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=1, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.grid(row=1, column=1, padx=5)

        label_contacto = tk.Label(ventana, text="Contacto:", bg="#119DA4", fg="#3C372B",
                                  font=("Montserrat", 20, "bold italic"))
        label_contacto.grid(row=2, column=0, padx=10, pady=10)

        entry_contacto = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_contacto.grid(row=2, column=1, padx=5)

        label_especialidad = tk.Label(ventana, text="Especialidad:", bg="#119DA4", fg="#3C372B",
                                      font=("Montserrat", 20, "bold italic"))
        label_especialidad.grid(row=3, column=0, padx=10, pady=10)

        combo_especialidad = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_especialidad.grid(row=3, column=1, padx=5)

        especialidades = self.controlador_doctor.obtener_especialidades()
        combo_especialidad['values'] = [es.get_nombreEspecialidad() for es in especialidades]
        combo_especialidad.especialidades = especialidades

        def add_doctor():
            id = entry_id.get()
            nombre = entry_nombre.get()
            contacto = entry_contacto.get()
            especialidad_nombre = combo_especialidad.get()
            especialidad = next(
                (es for es in combo_especialidad.especialidades if es.get_nombreEspecialidad() == especialidad_nombre),
                None)

            if nombre and especialidad and contacto and id:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarDoctores @idDoctor = ?,  @idEspecialidad = ?, @nombreDoctor = ?, @contacto = ?",
                        (id, especialidad.get_idEspecialidad(), nombre, contacto))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Doctor modificado exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al modificar doctor: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Modificar Doctor", command=add_doctor, bg="white", fg="#3C372B",
                                    font=("Montserrat", 12, "bold italic"), width=225, height=30, compound="left",
                                    image=self.imagen_doctor)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_eliminar_doctor(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Doctor")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1000, 500)

        label = tk.Label(ventana, text="Seleccione un Doctor:", bg="#119DA4", fg="#3C372B",
                         font=("Montserrat", 25, "bold italic"))
        label.grid(row=0, column=0, pady=5)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_doctor.obtener_doctores()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idDoctor()}, Nombre: {dato.get_nombreDoctor()} "
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay Doctores para mostrar")

        def del_cita():

            indice = listbox.curselection()

            if indice != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar al doctor?", message=", ".join(listbox.get(i) for i in indice)):
                    datos = self.controlador_citas.obtener_citas()
                    for idx in indice:
                        dato = datostemp[idx]
                        dato.split(",")
                        id = dato[0]

                self.db.cursor.execute("sp_GestionarDoctores @idDoctor = ? , @idEspecialidad = null, @nombreDoctor = null, @contacto = null", (id))
                self.db.conn.commit()
                messagebox.showinfo("Éxito", "Doctor Eliminado Exitosamente.")
                ventana.destroy()

        boton_registrar = tk.Button(ventana, text="   Eliminar Doctor", command=del_cita, bg="white", fg="#3C372B",
                                    font=("Montserrat", 15, "bold italic"), width=225, height=30, compound="left", image=self.imagen_eliminar)
        boton_registrar.grid(row=5, column=0, pady=5)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_ver_doctor(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Doctor")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1000, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_doctor.obtener_doctores()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idDoctor()}, Nombre: {dato.get_nombreDoctor()}, Contacto: {dato.get_contacto()}, Especialidad: {dato.get_idEspecialidad()} "
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay Doctores para mostrar")

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_especialidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Especialidades")
        ventana.config(bg="#119DA4")
        label = tk.Label(ventana, text="Especialidades", font=("Montserrat", 60, "bold italic"), fg="#3C372B",
                         bg="#119DA4", compound="center")
        label.pack(pady=10)
        self.centrar_ventana(ventana, 600, 500)

        button1 = tk.Button(ventana, text="  Agregar Especialidad", command=self.abrir_ventana_registrar_especialidad, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Especialidades", command=self.abrir_ventana_eliminar_especialidad, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Especialidades", command=self.abrir_ventana_ver_especialidad, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button4 = tk.Button(ventana, text="  Modificar Especialidad", command=self.abrir_ventana_modificar_especialidad, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button3.pack(pady=10)
        button1.pack(pady=10)
        button4.pack(pady=10)
        button2.pack(pady=10)

        boton_regresar.pack(pady=10, padx=10, anchor="se")
    def abrir_ventana_ver_especialidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Especialidades")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_doctor.obtener_especialidades()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idEspecialidad()}.- Especialidad: {dato.get_nombreEspecialidad()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay Especialidades para mostrar")

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_eliminar_especialidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Especialidades")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"),
                             relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_doctor.obtener_especialidades()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idEspecialidad()}.- Especialidad: {dato.get_nombreEspecialidad()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay Especialidades para mostrar")

        def del_esp():

            indice = listbox.curselection()

            if indice != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar la cita?", message=", ".join(listbox.get(i) for i in indice)):
                    datos = self.controlador_citas.obtener_citas()
                    for idx in indice:
                        dato = datostemp[idx]
                        dato.split(",")
                        id = dato[0]

                self.db.cursor.execute("EXEC sp_GestionarEspecialidad @idEspecialidad = ?, @nombreEspecialidad = null, @descripcionEspecialidad = null", (id))
                self.db.conn.commit()
                messagebox.showinfo("Éxito", "Cita Eliminada Exitosamente.")
                ventana.destroy()

        boton_registrar = tk.Button(ventana, text="   Eliminar Cita", command=del_esp, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_eliminar)
        boton_registrar.grid(row=5, column=0, pady=5)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_registrar_especialidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Especialidad")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 750, 200)

        label_nombre = tk.Label(ventana, text="Nombre de la Especialidad:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=0, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.grid(row=0, column=1, padx=5)

        label_des = tk.Label(ventana, text="Descripcion:", bg="#119DA4", fg="#3C372B",
                                  font=("Montserrat", 20, "bold italic"))
        label_des.grid(row=1, column=0, padx=10, pady=10)

        entry_des = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_des.grid(row=1, column=1, padx=5)

        def add_esp():
            nombre = entry_nombre.get()
            des = entry_des.get()

            if nombre and des:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarEspecialidad @nombreEspecialidad = ?, @descripcionEspecialidad = ?",
                        (nombre, des))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Especialidad agregada exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar especialidad: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Registrar Especialidad", command=add_esp, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=325, height=30, compound="left", image=self.imagen_especialidad)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_modificar_especialidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Modificar Especialidad")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 750, 300)

        label_id = tk.Label(ventana, text="ID Especialidad:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_id.grid(row=0, column=1, padx=5)

        label_nombre = tk.Label(ventana, text="Nombre de la Especialidad:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=1, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.grid(row=1, column=1, padx=5)

        label_des = tk.Label(ventana, text="Descripcion:", bg="#119DA4", fg="#3C372B",
                             font=("Montserrat", 20, "bold italic"))
        label_des.grid(row=2, column=0, padx=10, pady=10)

        entry_des = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_des.grid(row=2, column=1, padx=5)

        def add_esp():
            id = entry_id.get()
            nombre = entry_nombre.get()
            des = entry_des.get()

            if nombre and des and id:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarEspecialidad @idEspecialidad = ?, @nombreEspecialidad = ?, @descripcionEspecialidad = ?",
                        (id, nombre, des))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Especialidad modificada exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al modificar especialidad: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Modificar Especialidad", command=add_esp, bg="white",
                                    fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=325, height=30, compound="left",
                                    image=self.imagen_especialidad)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")


    def abrir_ventana_tratamient(self):
        ventana = Toplevel(self.root)
        ventana.title("Tratamientos")
        ventana.config(bg="#119DA4")
        label = tk.Label(ventana, text="Tratamientos", font=("Montserrat", 60, "bold italic"), fg="#3C372B",
                         bg="#119DA4", compound="center")
        label.pack(pady=10)
        self.centrar_ventana(ventana, 600, 500)

        button1 = tk.Button(ventana, text="  Agregar Tratamiento", command=self.abrir_ventana_registrar_tratamiento, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Tratamiento", command=self.abrir_ventana_eliminar_tratamiento, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Tratamientos", command=self.abrir_ventana_ver_tratamiento, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button4 = tk.Button(ventana, text="  Modificar Tratamiento", command=self.abrir_ventana_modificar_tratamiento, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button3.pack(pady=10)
        button1.pack(pady=10)
        button4.pack(pady=10)
        button2.pack(pady=10)

        boton_regresar.pack(pady=10, padx=10, anchor="se")

    def abrir_ventana_registrar_tratamiento(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Tratamiento")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 750, 150)

        label_nombre = tk.Label(ventana, text="Nombre del Tratamiento:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=0, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.grid(row=0, column=1, padx=5)

        def add_tra():
            nombre = entry_nombre.get()

            if nombre:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarTratamiento @idTratamiento = null,  @nombreTratamiento = ?",
                        (nombre))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Tratamiento agregado exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar tratamiento: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Registrar Tratamiento", command=add_tra, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=325, height=30, compound="left", image=self.imagen_tratamiento)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_modificar_tratamiento(self):
        ventana = Toplevel(self.root)
        ventana.title("Modificar Tratamiento")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 750, 175)

        label_id = tk.Label(ventana, text="ID del Tratamiento:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_id.grid(row=0, column=0, padx=10, pady=10)

        entry_id = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_id.grid(row=0, column=1, padx=5)

        label_nombre = tk.Label(ventana, text="Nombre del Tratamiento:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_nombre.grid(row=1, column=0, padx=10, pady=10)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 12, "italic"), relief="flat", bd=2)
        entry_nombre.grid(row=1, column=1, padx=5)

        def add_tra():
            nombre = entry_nombre.get()
            id = entry_id.get()

            if nombre and id:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarTratamiento @idTratamiento = ?,  @nombreTratamiento = ?",
                        (id, nombre))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Tratamiento agregado exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar tratamiento: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Registrar Tratamiento", command=add_tra, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=325, height=30, compound="left", image=self.imagen_tratamiento)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_ver_tratamiento(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Tratamiento")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_citas.obtener_Tratamiento()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idTratamiento()}.- Tratamiento: {dato.get_nombreTratamiento()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay Tratamientos para mostrar")

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_eliminar_tratamiento(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Tratamientos")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"),
                             relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_citas.obtener_Tratamiento()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idTratamiento()}, Tratamiento: {dato.get_nombreTratamiento()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay Tratamientos para mostrar")

        def del_esp():

            indice = listbox.curselection()

            if indice != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar el Tratamiento?", message=", ".join(listbox.get(i) for i in indice)):
                    datos = self.controlador_citas.obtener_citas()
                    for idx in indice:
                        dato = datostemp[idx]
                        dato = dato.split(",")
                        id = dato[0]
                        print(id)

                self.db.cursor.execute("EXEC sp_GestionarTratamiento @idTratamiento = ?, @nombreTratamiento = null", (id))
                self.db.conn.commit()
                messagebox.showinfo("Éxito", "Tratamiento Eliminado Exitosamente.")
                ventana.destroy()

        boton_registrar = tk.Button(ventana, text="   Eliminar Tratamiento", command=del_esp, bg="white", fg="#3C372B",
                                    font=("Montserrat", 12, "bold italic"), width=225, height=30, compound="left", image=self.imagen_eliminar)
        boton_registrar.grid(row=5, column=0, pady=5)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_citas(self):
        ventana = Toplevel(self.root)
        ventana.title("Citas")
        ventana.config(bg="#119DA4")
        label = tk.Label(ventana, text="Cita", font=("Montserrat", 60, "bold italic"), fg="#3C372B",
                         bg="#119DA4", compound="center")
        label.pack(pady=10)
        self.centrar_ventana(ventana, 500, 600)

        button1 = tk.Button(ventana, text="  Crear Cita", command=self.abrir_ventana_registrar_cita, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Cita", command=self.abrir_ventana_eliminar_cita, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Citas", command=self.abrir_ventana_ver_cita, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button4 = tk.Button(ventana, text="  Modificar Cita", command=self.abrir_ventana_modificar_cita, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button5 = tk.Button(ventana, text="  Historial Cita", command=self.abrir_ventana_ver_historico_cita, bg="white",
                            fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button3.pack(pady=10)
        button1.pack(pady=10)
        button4.pack(pady=10)
        button2.pack(pady=10)
        button5.pack(pady=10)

        boton_regresar.pack(pady=10, padx=10, anchor="se")
    def abrir_ventana_registrar_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Cita")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 830, 300)

        label_paciente = tk.Label(ventana, text="Nombre del paciente:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_paciente.grid(row=0, column=0, padx=10, pady=10)

        combo_pacientes = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_pacientes.grid(row=0, column=1, padx=5)
        pacientes = self.controlador_paciente.obtener_paciente()
        combo_pacientes['values'] = [pa.get_nombrePaciente() for pa in pacientes]
        combo_pacientes.pacientes = pacientes

        label_doctor = tk.Label(ventana, text="Doctor(a):", bg="#119DA4", fg="#3C372B",
                                  font=("Montserrat", 20, "bold italic"))
        label_doctor.grid(row=1, column=0, padx=10, pady=10)

        combo_doctores = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_doctores.grid(row=1, column=1, padx=5)
        doctores = self.controlador_doctor.obtener_doctores()
        combo_doctores['values'] = [do.get_nombreDoctor() for do in doctores]
        combo_doctores.doctores = doctores

        label_fechaCita = tk.Label(ventana, text="Fecha y hora:", bg="#119DA4", fg="#3C372B",
                                      font=("Montserrat", 20, "bold italic"))
        label_fechaCita.grid(row=2, column=0, padx=10, pady=10)

        cal = DateEntry(ventana,background='darkblue',
                        foreground='white', borderwidth=2,  width=12, font=("Montserrat", 20, "bold italic"))
        cal.grid(row=2, column=1, pady=5)
        combo_horas = ttk.Combobox(ventana, values=self.controlador_citas.obtener_horas_disponibles(), width=12, font=("Montserrat", 20, "bold italic"))
        combo_horas.grid(row=2, column=2, pady=5)
        combo_horas.current(0)

        label_tratamiento = tk.Label(ventana, text="Tratamiento:", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_tratamiento.grid(row=3, column=0, padx=10, pady=10)

        combo_tratamiento = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_tratamiento.grid(row=3, column=1, padx=5)
        tratamientos = self.controlador_citas.obtener_Tratamiento()
        combo_tratamiento['values'] = [tra.get_nombreTratamiento() for tra in tratamientos]
        combo_tratamiento.tratamientos = tratamientos

        def add_cita():

            paciente_nombre = combo_pacientes.get()
            paciente = next((pa for pa in combo_pacientes.pacientes if pa.get_nombrePaciente() == paciente_nombre), None)

            doctor_nombre = combo_doctores.get()
            doctor = next((do for do in combo_doctores.doctores if do.get_nombreDoctor() == doctor_nombre), None)

            tratamiento_nombre = combo_tratamiento.get()
            tratamiento = next((tra for tra in combo_tratamiento.tratamientos if tra.get_nombreTratamiento() == tratamiento_nombre), None)

            fechaCita = cal.get() + ' ' + combo_horas.get() + ':00'

            if doctor and paciente and tratamiento:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarCitas  @idCita = null, @idPaciente = ?, @idTratamiento = ?, @idDoctor = ?, @fechaCita = ?, @idEstado = ?",
                        (paciente.get_idPaciente(), tratamiento.get_idTratamiento(), doctor.get_idDoctor(), fechaCita, 1))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "cita agregada exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar cita: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Registrar Cita", command=add_cita, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_cita)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_modificar_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Modificar Cita")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 830, 400)

        label_id = tk.Label(ventana, text=" ID Cita:", bg="#119DA4", fg="#3C372B",
                              font=("Montserrat", 25, "bold italic"))
        label_id.grid(row=0, column=0)

        entry_id = tk.Entry(ventana, width=27, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        entry_id.config(width=25)
        entry_id.grid(row=0, column=1, padx=5)

        label_paciente = tk.Label(ventana, text="Nombre del paciente:", bg="#119DA4", fg="#3C372B",
                                  font=("Montserrat", 20, "bold italic"))
        label_paciente.grid(row=1, column=0, padx=10, pady=10)

        combo_pacientes = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_pacientes.grid(row=1, column=1, padx=5)
        pacientes = self.controlador_paciente.obtener_paciente()
        combo_pacientes['values'] = [pa.get_nombrePaciente() for pa in pacientes]
        combo_pacientes.pacientes = pacientes

        label_doctor = tk.Label(ventana, text="Doctor(a):", bg="#119DA4", fg="#3C372B",
                                font=("Montserrat", 20, "bold italic"))
        label_doctor.grid(row=2, column=0, padx=10, pady=10)

        combo_doctores = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_doctores.grid(row=2, column=1, padx=5)
        doctores = self.controlador_doctor.obtener_doctores()
        combo_doctores['values'] = [do.get_nombreDoctor() for do in doctores]
        combo_doctores.doctores = doctores

        label_fechaCita = tk.Label(ventana, text="Fecha y hora:", bg="#119DA4", fg="#3C372B",
                                   font=("Montserrat", 20, "bold italic"))
        label_fechaCita.grid(row=3, column=0, padx=10, pady=10)

        cal = DateEntry(ventana, background='darkblue',
                        foreground='white', borderwidth=2, width=12, font=("Montserrat", 20, "bold italic"))
        cal.grid(row=3, column=1, pady=5)
        combo_horas = ttk.Combobox(ventana, values=self.controlador_citas.obtener_horas_disponibles(),width=12, font=("Montserrat", 20, "bold italic"))
        combo_horas.grid(row=3, column=2, pady=5)
        combo_horas.current(0)

        label_tratamiento = tk.Label(ventana, text="Tratamiento:", bg="#119DA4", fg="#3C372B",
                                     font=("Montserrat", 20, "bold italic"))
        label_tratamiento.grid(row=4, column=0, padx=10, pady=10)

        combo_tratamiento = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_tratamiento.grid(row=4, column=1, padx=5)
        tratamientos = self.controlador_citas.obtener_Tratamiento()
        combo_tratamiento['values'] = [tra.get_nombreTratamiento() for tra in tratamientos]
        combo_tratamiento.tratamientos = tratamientos

        def add_cita():


            paciente_nombre = combo_pacientes.get()
            paciente = next((pa for pa in combo_pacientes.pacientes if pa.get_nombrePaciente() == paciente_nombre), None)

            doctor_nombre = combo_doctores.get()
            doctor = next((do for do in combo_doctores.doctores if do.get_nombreDoctor() == doctor_nombre), None)

            tratamiento_nombre = combo_tratamiento.get()
            tratamiento = next((tra for tra in combo_tratamiento.tratamientos if tra.get_nombreTratamiento() == tratamiento_nombre), None)

            fechaCita = cal.get() + ' ' + combo_horas.get() + ':00'

            if doctor and paciente and tratamiento:
                try:
                    self.db.cursor.execute(
                        "EXEC sp_GestionarCitas  @idCita = ?, @idPaciente = ?, @idTratamiento = ?, @idDoctor = ?, @fechaCita = ?, @idEstado = ?",
                        (entry_id.get(), paciente.get_idPaciente(), tratamiento.get_idTratamiento(), doctor.get_idDoctor(), fechaCita, 1))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "cita modificada exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al modificar cita: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Modificar Cita", command=add_cita, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_cita)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_eliminar_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Cita")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        label = tk.Label(ventana, text="Seleccione una cita:", bg="#119DA4", fg="#3C372B",
                         font=("Montserrat", 25, "bold italic"))
        label.grid(row=0, column=0, pady=5)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_citas.obtener_citas()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato.get_idCita()}, El Paciente: {dato.get_idPaciente()}, tiene su cita el día: {dato.get_fechaCita()}, con El/la Dr(a): {dato.get_idDoctor()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay citas para mostrar")

        def del_cita():

            indice = listbox.curselection()

            if indice != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar la cita?", message=", ".join(listbox.get(i) for i in indice)):
                    datos = self.controlador_citas.obtener_citas()
                    for idx in indice:
                        dato = datostemp[idx]
                        dato.split(",")
                        id = dato[0]

                self.db.cursor.execute("sp_GestionarCitas @idCita = ? , @idPaciente = null, @idDoctor = null, @idTratamiento = null, @fechaCita = null, @idEstado = null", (id))
                self.db.conn.commit()
                messagebox.showinfo("Éxito", "Cita Eliminada Exitosamente.")
                ventana.destroy()

        boton_registrar = tk.Button(ventana, text="   Eliminar Cita", command=del_cita, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_eliminar)
        boton_registrar.grid(row=5, column=0, pady=5)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_ver_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Citas")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_citas.obtener_citas()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"El Paciente: {dato.get_idPaciente()}, tiene su cita el día: {dato.get_fechaCita()}, con El/la Dr(a): {dato.get_idDoctor()}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay citas para mostrar")

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_ver_historico_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Citas")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1400, 600)

        label_paciente = tk.Label(ventana, text="Nombre del paciente:", bg="#119DA4", fg="#3C372B",
                                  font=("Montserrat", 20, "bold italic"))
        label_paciente.grid(row=0, column=0, padx=10, pady=10)

        combo_pacientes = ttk.Combobox(ventana, state="readonly", width=27, font=("Montserrat", 12, "italic"))
        combo_pacientes.grid(row=0, column=1, padx=5)
        pacientes = self.controlador_paciente.obtener_paciente()
        combo_pacientes['values'] = [pa.get_nombrePaciente() for pa in pacientes]
        combo_pacientes.pacientes = pacientes

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Montserrat", 15, "italic"),
                             relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)

        def mostrar():
            listbox.delete(0, tk.END)
            paciente_nombre = combo_pacientes.get()
            paciente = next((pa for pa in combo_pacientes.pacientes if pa.get_nombrePaciente() == paciente_nombre), None)
            print(paciente)
            if paciente:
                datos = self.controlador_citas.obtener_citas_historico(paciente.get_idPaciente())
                datostemp = []
                if datos != []:
                    for dato in datos:
                        dato = f"{dato}"
                        listbox.insert(tk.END, dato)
                        datostemp.append(dato)
                else:
                    listbox.insert(tk.END, "No hay citas para mostrar")

        boton_consulta = tk.Button(ventana, text="   Consultar Cita", command=mostrar, bg="white", fg="#3C372B",
                                    font=("Montserrat", 20, "bold italic"), width=225, height=30, compound="left",
                                    image=self.imagen_cita)
        boton_consulta.grid(row=5, column=1)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")



def main():
    server = 'PC-DEV36'
    database = 'ProyectoCitasMedicas'
    username = 'ADMINMH'
    password = 'Marlon123'

    try:
        db = Database(server, database, username, password)
        app = GestionMedicaApp(root, db)
        root.mainloop()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        try:
            db.cerrar()
        except Exception:
            print("No hay conexión que cerrar.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    root.config(bg="#264653")
    main()