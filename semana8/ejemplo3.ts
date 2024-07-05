/**
 * Como tipamos un objecto en 75
 * para ello tenemos 2 soluciones
 * 1.   Interface: La cual me permite poder definir los atributos del objeto y el tipo de dato
 *                 de cada atributo
 * 2.   Type: Lo mismo que interface
 */

interface Persona {
    nombre: string
    apellido: string
    dni: number
    edad: number
    direccion?: string
}

type Persona2 = {
    nombre: string
    apellido: string
    dni: number
    edad: number
    direccion?: string
}

const persona: Persona = {
    nombre: "Pepe",
    apellido: "Perez",
    dni: 72813350,
    edad: 86,
    direccion: "Av. mi casa"
}

const persona2: Persona2 = {
    nombre: "Juan",
    apellido: "Perez",
    dni: 72813350,
    edad: 86
}

const listaDePersonas: Persona[] = [
    {
        nombre: "Persona 1",
        apellido: "Perez",
        dni: 72813350,
        edad: 86
    }, 
    {
        nombre: "Persona 2",
        apellido: "Perez",
        dni: 72813350,
        edad: 86
    }
]

function saludar(persona: Persona) {
    console.log(
        `Hola me llamo ${persona.nombre} ${persona.apellido} y tengo ${persona.edad} años de edad`
    );   
}

saludar(persona)