USE [ProyectoCitasMedicas]
GO

/****** Object:  Table [dbo].[Citas]    Script Date: 25/08/2024 11:58:39 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Citas](
	[idCita] [int] IDENTITY(1,1) NOT NULL,
	[idPaciente] [int] NOT NULL,
	[idDoctor] [int] NOT NULL,
	[idTratamiento] [int] NOT NULL,
	[fechaCreacion] [date] NULL,
	[fechaCita] [datetime] NOT NULL,
	[idEstado] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[idCita] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Citas] ADD  DEFAULT (getdate()) FOR [fechaCreacion]
GO

ALTER TABLE [dbo].[Citas]  WITH CHECK ADD  CONSTRAINT [fk_CitasDoctor] FOREIGN KEY([idDoctor])
REFERENCES [dbo].[Doctores] ([idDoctor])
GO

ALTER TABLE [dbo].[Citas] CHECK CONSTRAINT [fk_CitasDoctor]
GO

ALTER TABLE [dbo].[Citas]  WITH CHECK ADD  CONSTRAINT [fk_CitasEstado] FOREIGN KEY([idEstado])
REFERENCES [dbo].[Estado] ([idEstado])
GO

ALTER TABLE [dbo].[Citas] CHECK CONSTRAINT [fk_CitasEstado]
GO

ALTER TABLE [dbo].[Citas]  WITH CHECK ADD  CONSTRAINT [fk_CitasPaciente] FOREIGN KEY([idPaciente])
REFERENCES [dbo].[Paciente] ([idPaciente])
GO

ALTER TABLE [dbo].[Citas] CHECK CONSTRAINT [fk_CitasPaciente]
GO

ALTER TABLE [dbo].[Citas]  WITH CHECK ADD  CONSTRAINT [fk_CitasTratamiento] FOREIGN KEY([idTratamiento])
REFERENCES [dbo].[Tratamiento] ([idTratamiento])
GO

ALTER TABLE [dbo].[Citas] CHECK CONSTRAINT [fk_CitasTratamiento]
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  Table [dbo].[Doctores]    Script Date: 25/08/2024 11:58:45 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Doctores](
	[idDoctor] [int] IDENTITY(1,1) NOT NULL,
	[idEspecialidad] [int] NOT NULL,
	[nombreDoctor] [varchar](max) NOT NULL,
	[contacto] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[idDoctor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[Doctores]  WITH CHECK ADD  CONSTRAINT [fk_DoctoresEspecialedad] FOREIGN KEY([idEspecialidad])
REFERENCES [dbo].[Especialidad] ([idEspecialidad])
GO

ALTER TABLE [dbo].[Doctores] CHECK CONSTRAINT [fk_DoctoresEspecialedad]
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  Table [dbo].[Especialidad]    Script Date: 25/08/2024 11:58:58 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Especialidad](
	[idEspecialidad] [int] IDENTITY(1,1) NOT NULL,
	[nombreEspecialidad] [varchar](max) NULL,
	[descripcionEspecialidad] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[idEspecialidad] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  Table [dbo].[Estado]    Script Date: 25/08/2024 11:59:04 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Estado](
	[idEstado] [int] IDENTITY(1,1) NOT NULL,
	[nombreestado] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[idEstado] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  Table [dbo].[Paciente]    Script Date: 25/08/2024 11:59:12 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Paciente](
	[idPaciente] [int] IDENTITY(1,1) NOT NULL,
	[nombrePaciente] [varchar](max) NOT NULL,
	[edad] [int] NOT NULL,
	[contactoPaciente] [varchar](max) NULL,
	[direccion] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[idPaciente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  Table [dbo].[Tratamiento]    Script Date: 25/08/2024 11:59:19 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Tratamiento](
	[idTratamiento] [int] IDENTITY(1,1) NOT NULL,
	[nombreTratamiento] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[idTratamiento] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionarCitas]    Script Date: 25/08/2024 11:59:36 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE   PROCEDURE [dbo].[sp_GestionarCitas]
@idCita int,
@idPaciente int,
@idDoctor int,
@idTratamiento int,
@fechaCita datetime,
@idEstado int
AS 
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;

        IF (@idCita = 0 OR @idCita IS NULL) 
        BEGIN
            IF (@idPaciente IS NULL AND @idDoctor IS NULL AND @idTratamiento IS NULL AND @fechaCita IS NULL AND @idEstado IS NULL)
            BEGIN
                SELECT Citas.idCita, Paciente.nombrePaciente as idPaciente, Doctores.nombreDoctor as idDoctor,
					Tratamiento.nombreTratamiento as idTratamiento, 
						Citas.fechaCreacion, Citas.fechaCita,  Estado.nombreestado as idEstado
                FROM Citas 
                INNER JOIN Paciente ON Citas.idPaciente = Paciente.idPaciente
                INNER JOIN Doctores ON Citas.idDoctor = Doctores.idDoctor
                INNER JOIN Estado ON Citas.idEstado = Estado.idEstado
                INNER JOIN Tratamiento ON Citas.idTratamiento = Tratamiento.idTratamiento
                WHERE Citas.idEstado <> 2;
            END
            ELSE
            BEGIN
                INSERT INTO Citas (idPaciente, idDoctor, fechaCreacion, idTratamiento, fechaCita, idEstado)
                VALUES (@idPaciente, @idDoctor, GETDATE(), @idTratamiento, @fechaCita, @idEstado);
            END
        END
        ELSE
        BEGIN
            IF (@idPaciente IS NOT NULL AND @idDoctor IS NOT NULL AND @idTratamiento IS NOT NULL AND @fechaCita IS NOT NULL AND @idEstado IS NOT NULL)
            BEGIN
                UPDATE Citas
                SET idPaciente = @idPaciente, idDoctor = @idDoctor, fechaCreacion = GETDATE(), idTratamiento = @idTratamiento, fechaCita = @fechaCita, idEstado = @idEstado
                WHERE idCita = @idCita;
            END
            ELSE 
            BEGIN
                DELETE FROM Citas
                WHERE idCita = @idCita;
            END
        END

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
        BEGIN
            ROLLBACK TRANSACTION;
            PRINT('Realicé un rollback de la transacción');
        END;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
        PRINT(@ErrorMessage);
        PRINT(@ErrorSeverity);
        PRINT(@ErrorState);
    END CATCH
END;
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionarDoctores]    Script Date: 25/08/2024 11:59:47 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE   PROCEDURE [dbo].[sp_GestionarDoctores]
@idEspecialidad int,
@nombreDoctor varchar(max),
@contacto varchar(max)
AS 
BEGIN
	begin try
		begin transaction;
			insert into Doctores
				values (@idEspecialidad, @nombreDoctor, @contacto)
			commit transaction;
	end try
	begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionarEspecialidad]    Script Date: 25/08/2024 11:59:54 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE   PROCEDURE [dbo].[sp_GestionarEspecialidad]
@nombreEspecialidad varchar(max),
@descripcionEspecialidad varchar(max)
AS 
BEGIN
	begin try
		begin transaction;
			insert into Especialidad
				values (@nombreEspecialidad, @descripcionEspecialidad)
			commit transaction;
	end try
	begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;

GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionarEstado]    Script Date: 25/08/2024 11:59:59 p. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE   PROCEDURE [dbo].[sp_GestionarEstado]
@nombreestado varchar(max)
AS 
BEGIN
	begin try
		begin transaction;
			insert into Estado
				values (@nombreestado)
			commit transaction;
	end try
	begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionarTratamiento]    Script Date: 26/08/2024 12:00:07 a. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE   PROCEDURE [dbo].[sp_GestionarTratamiento]
@nombreTratamiento varchar(max)
AS 
BEGIN
	begin try
		begin transaction;
			insert into Tratamiento
				values (@nombreTratamiento)
			commit transaction;
	end try
	begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;

GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionarTratamiento]    Script Date: 26/08/2024 12:00:12 a. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE   PROCEDURE [dbo].[sp_GestionarTratamiento]
@nombreTratamiento varchar(max)
AS 
BEGIN
	begin try
		begin transaction;
			insert into Tratamiento
				values (@nombreTratamiento)
			commit transaction;
	end try
	begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;

GO

USE [ProyectoCitasMedicas]
GO

/****** Object:  StoredProcedure [dbo].[sp_GestionPacientes]    Script Date: 26/08/2024 12:00:18 a. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE   PROCEDURE [dbo].[sp_GestionPacientes]
@nombrePaciente varchar(max),
@edad int ,
@contactoPaciente varchar(max),
@direccion varchar(max)
AS 
BEGIN
	begin try
		begin transaction;
		IF @nombrePaciente IS NULL AND @edad IS NULL AND @contactoPaciente IS NULL AND @direccion IS NULL
			select idPaciente, nombrePaciente, edad, contactoPaciente, direccion from Paciente
		ELSE
		BEGIN
			insert into Paciente values (@nombrePaciente,@edad,@contactoPaciente,@direccion)
			commit transaction;
		END
	end try
	begin catch
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO

