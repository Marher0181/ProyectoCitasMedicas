
import tkinter as tk
from tkinter import messagebox, Toplevel, ttk, Listbox
from tkcalendar import Calendar, DateEntry
from Models.Paciente import Paciente
from Controladores import Doctor, Paciente, Cita
from database import Database

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

        self.menu_libros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_libros.add_command(label="Agregar Libro", command=self.abrir_ventana_registrar_paciente)
        self.menu_libros.add_command(label="Salir", command=self.salir_del_programa)
        self.menu_libros.add_command(label="Eliminar Libro", command=self.abrir_ventana_registrar_paciente)
        self.menu_libros.add_command(label="Buscar Libro", command=self.abrir_ventana_registrar_paciente)
        self.menu_bar.add_cascade(label="Libros", menu=self.menu_libros)

        self.menu_usuarios = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_usuarios.add_command(label="Registrar Usuario", command=self.abrir_ventana_registrar_paciente)
        self.menu_usuarios.add_command(label="Eliminar Usuario", command=self.abrir_ventana_registrar_paciente)
        self.menu_bar.add_cascade(label="Usuarios", menu=self.menu_usuarios)

        self.menu_prestamos = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_prestamos.add_command(label="Prestar Libro", command=self.abrir_ventana_registrar_paciente)
        self.menu_prestamos.add_command(label="Devolver Libro", command=self.abrir_ventana_registrar_paciente)
        self.menu_bar.add_cascade(label="Préstamos", menu=self.menu_prestamos)

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
        buttonu = tk.Button(root, text="  Paciente", command=self.abrir_ventana_registrar_paciente, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_paciente)
        buttonu.pack(pady=10)
        buttonp = tk.Button(root, text="  Doctor", command=self.abrir_ventana_registrar_doctor, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_doctor)
        buttonp.pack(pady=10)
        buttonm = tk.Button(root, text="  Especialidad", command=self.abrir_ventana_registrar_especialidad, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_especialidad)
        buttonm.pack(pady=10)
        buttonm = tk.Button(root, text="  Tratamiento", command=self.abrir_ventana_registrar_tratamiento, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_tratamiento)
        buttonm.pack(pady=10)
        buttonm = tk.Button(root, text="  Salir", command=self.salir_del_programa, bg="white", fg="#3C372B",
                            font=("Montserrat", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_salir)
        buttonm.pack(pady=10)
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
                                    fg="#3C372B", font=("Montserrat", 15, "bold italic"), width=225, height=25,
                                    compound="left", image=self.imagen_registrar_usuario)
        boton_registrar.grid(row=5, column=3, pady=5)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Montserrat", 15, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=2, pady=10, padx=10, sticky="w")
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
                                    font=("Times New Roman", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_doctor)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
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
                                    font=("Times New Roman", 20, "bold italic"), width=325, height=30, compound="left", image=self.imagen_especialidad)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
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
                        "EXEC sp_GestionarTratamiento @nombreTratamiento = ?",
                        (nombre))
                    self.db.cursor.commit()
                    messagebox.showinfo("Éxito", "Tratamiento agregado exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar tratamiento: {e}")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

        boton_registrar = tk.Button(ventana, text="   Registrar Tratamiento", command=add_tra, bg="white", fg="#3C372B",
                                    font=("Times New Roman", 20, "bold italic"), width=325, height=30, compound="left", image=self.imagen_tratamiento)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_citas(self):
        ventana = Toplevel(self.root)
        ventana.title("Citas")
        ventana.config(bg="#119DA4")
        label = tk.Label(ventana, text="Cita", font=("Times New Roman", 60, "bold italic"), fg="#3C372B",
                         bg="#119DA4", compound="center")
        label.pack(pady=10)
        self.centrar_ventana(ventana, 500, 430)

        button1 = tk.Button(ventana, text="  Crear Cita", command=self.abrir_ventana_registrar_cita, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Cita", command=self.abrir_ventana_eliminar_cita, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Citas", command=self.abrir_ventana_ver_cita, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        button4 = tk.Button(ventana, text="  Modificar Cita", command=self.abrir_ventana_modificar_cita, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button3.pack(pady=10)
        button1.pack(pady=10)
        button4.pack(pady=10)
        button2.pack(pady=10)

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
                                    font=("Times New Roman", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_cita)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
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
                                    font=("Times New Roman", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_cita)
        boton_registrar.grid(row=5, column=1)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_eliminar_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Cita")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        label = tk.Label(ventana, text="Seleccione una cita:", bg="#119DA4", fg="#3C372B",
                         font = ("Times New Roman", 25, "bold italic"))
        label.grid(row=0, column=0, pady=5)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_citas.obtener_citas()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato}"
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
                                    font=("Times New Roman", 20, "bold italic"), width=225, height=30, compound="left", image=self.imagen_eliminar)
        boton_registrar.grid(row=5, column=0, pady=5)

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
    def abrir_ventana_ver_cita(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Citas")
        ventana.config(bg="#119DA4")
        self.centrar_ventana(ventana, 1124, 500)

        listbox = tk.Listbox(ventana, height=15, width=100, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        listbox.grid(row=2, column=0, pady=5)
        datos = self.controlador_citas.obtener_citas()
        datostemp = []
        if datos != []:
            for dato in datos:
                dato = f"{dato}"
                listbox.insert(tk.END, dato)
                datostemp.append(dato)
        else:
            listbox.insert(tk.END, "No hay citas para mostrar")

        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                                   fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=5, column=0, pady=10, padx=10, sticky="w")
def main():
    # Configura los parámetros de conexión a MSSQL
    server = 'DESKTOP-HMS6GDC\\SQLEXPRESS'
    database = 'ProyectoCitasMedicas'
    username = 'ADMIN'
    password = 'ADMIN'

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