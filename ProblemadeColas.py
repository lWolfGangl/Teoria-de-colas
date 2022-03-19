# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:55:14 2021
@author: David
"""
import matplotlib.pyplot as plt
from random import randint
#Numero de pacientes promedio por dia
numPacientes=100 
#Beneficio por cliente
benCliente=30
#Tiempo prom de atencion por paciente
tiemAten=4
#tiempo maximo de espera(si cumple este tiempo se va)
tiempEsp=120
#Costo total por sala(costo por un Medico+sala de atencion+enfermero o asistente 
#+ mantenimiento de los equipos) al dia
costoSala=300
#numero de salas
numSalas=6
salasPrueba=[1,2,3,4,5,6]
#Tiempo estimado de llegada maximo entre pacientes en minutos
tiemEstPac=12
#Contador de pacientes Recibidos
pacAtendidos=0
#Contador de pacientes Perdidos
pacPerdidos=0
#Arreglo de tiempo de espera promedio
tiempEsperaProm=[]
#Arreglo de pacientes perdidos
pacPerProm=[]
#Arreglo de pacientes atendidos 
pacAteProm=[]
#Arreglo del beneficio del dia
benDia=[]
#Arreglo del costo por sala
costSala=[]
#Arreglo del flujo neto del dia
fluNeto=[]
#Arreglo del flujo neto estimado del dia
fluNetoEst=[]
def creadorPacientesEntrada(numPacientes):
    HoraEntrada=[]
    num=0
    for i in range(numPacientes):
        HoraEntrada.append(num)
        num=num+randint(0, tiemEstPac)
    return (HoraEntrada)
HoraEntrada=[]
HoraEntrada=creadorPacientesEntrada(numPacientes)
print(HoraEntrada)


def creadorPacientesSalida(numPacientes,HoraEntrada):
    HoraSalida=[]
    for i in range(numPacientes):
        HoraSalida.append(HoraEntrada[i]+tiempEsp)
    return (HoraSalida)
HoraSalida=[]
HoraSalida=creadorPacientesSalida(numPacientes,HoraEntrada)
print(HoraSalida)

def simulacion(numSalas):
    #1440 minutos que tiene el dia
    salas=[]
    pacPerdidos=0
    pacAtendidos=0
    tiempoDeEsperaTotal=0
    for i in range(numSalas):
        salas.append(0)
    for tiempo in range(1440):
        if (len(HoraSalida)>0):
            if (HoraSalida[0]<tiempo):
                HoraEntrada.pop(0)
                HoraSalida.pop(0)
                pacPerdidos+=1
        for disp in range (numSalas):
            if (tiempo>=salas[disp] and len(HoraSalida)>0 and tiempo>=HoraEntrada[0]):
                salas[disp]=tiempo+tiemAten
                tiempoDeEsperaTotal=tiempoDeEsperaTotal+tiempo-HoraEntrada[0]
                #print(salas," minuto:",tiempo," ID:",HoraEntrada[0])
                HoraEntrada.pop(0)
                HoraSalida.pop(0)
                pacAtendidos=pacAtendidos+1
    print("")
    print("Con ",numSalas," salas")
    print("Tiempo de espera promedio:",tiempoDeEsperaTotal/pacAtendidos)
    tiempEsperaProm.append(tiempoDeEsperaTotal/pacAtendidos)
    print("pacientes perdidos",pacPerdidos)
    pacPerProm.append(pacPerdidos)
    print("pacientes Atendidos",pacAtendidos)
    pacAteProm.append(pacAtendidos)
    print("Perdidas estimadas por pacientes perdidos",pacPerdidos*benCliente)
    print("Costo por sala",numSalas*costoSala," costo total: ",numSalas*costoSala+pacPerdidos*benCliente)
    costSala.append(numSalas*costoSala)
    print("Beneficios del dia",benCliente*pacAtendidos)
    benDia.append(benCliente*pacAtendidos)
    print("Flujo neto:",benCliente*pacAtendidos-numSalas*costoSala)
    fluNeto.append(benCliente*pacAtendidos-numSalas*costoSala)
    print("Flujo neto estimado:",benCliente*pacAtendidos-(numSalas*costoSala+pacPerdidos*benCliente))
    fluNetoEst.append(benCliente*pacAtendidos-(numSalas*costoSala+pacPerdidos*benCliente))
    print("___________________________________________________________________")
for i in range (numSalas):
    HoraEntrada=creadorPacientesEntrada(numPacientes)
    HoraSalida=creadorPacientesSalida(numPacientes,HoraEntrada)
    simulacion(i+1)

plt.plot(salasPrueba,tiempEsperaProm,'-o',color='black')
plt.xlabel('Numero de Salas')
plt.ylabel('Tiempo de Espera')
plt.title("Tiempos de espera por sala")
plt.show()

plt.plot(salasPrueba,pacPerProm,'-o',color='red')
plt.plot(salasPrueba,pacAteProm,'-o',color='g')
plt.xlabel('Numero de Salas')
plt.ylabel('Pacientes perdidos')
plt.title("Pacientes perdidos/atendidos por numero de salas")
plt.show()

plt.plot(salasPrueba,benDia,'-o',color='black')
plt.xlabel('Numero de Salas')
plt.ylabel('Beneficios al dia')
plt.title("Beneficios al dia por numero de salas")
plt.show()

plt.plot(salasPrueba,fluNeto,'-o',color='black')
plt.xlabel('Numero de Salas')
plt.ylabel('Flujo Neto al dia')
plt.title("Flujo neto al dia por numero de salas")
plt.show()

plt.plot(salasPrueba,fluNetoEst,'-o',color='black')
plt.xlabel('Numero de Salas')
plt.ylabel('Flujo Neto al dia')
plt.title("Perdidas/costos y beneficios")
plt.show()
