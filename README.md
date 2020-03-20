# Base de datos de pacientes infectados por corona virus en Guatemala

Descripcion: Esta es un dataset ***no oficial***, recopilado de fuentes oficiales, de los casos confirmados de Corona Virus en Guatemala.

Proposito: Que investigadores/desarrolladores/sociedad civil se informen y estudien la propagacion del virus corona NCOVID-19 en Guatemala. Proveer una base de datos para que otras personas desarrollen visualizaciones y analisis.

***Licencia: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)***

## Estadisticas

Confirmados: 9

Recuperados: 0

Fallecidos: 1

![alt tag](https://github.com/ncovgt2020/ncovgt2020/blob/master/imgs/confirmados.png)
![alt tag](https://github.com/ncovgt2020/ncovgt2020/blob/master/imgs/fallecidos.png)
![alt tag](https://github.com/ncovgt2020/ncovgt2020/blob/master/imgs/recuperados.png)

Descripcion de campos

## pacientes.csv

Contine la informacion disponible de los casos confirmados de corona virus en Guatemala.

- id: numero de paciente (numerico, entero)
- sexo: m: masculino, f: femenino, x: desconocido (string)
- fecha_nacimiento: aa-mm-dd, ano de nacimiento. Se calcula como: fecha = 2020 - Edad, por tanto el dia y mes no se registran y se utiliza un valor por defecto 01-01(string), o campo vacio
- edad: edad del paciente (numerico, entero), -99: desconocido
- pais: pais de origen/nacionalidad (string) o campo vacio
- departamento: Region donde tuvo mayor actividad (string)
- enfermedad: condicion medica previa o desconocido (string)
- grupo: relacion con algun grupo especifico, -99: desconocido, no aplica (numerico, entero)
	- 1: vuelo 11 de marzo aeromexico
	- 2: vuelo 6 de marzo iberia
	- 3: contacto con paciente 2 (primer fallecido)
- razon_infeccion: causa de la infeccion (viaje, visita a familiar, visita a hospital, contacto con paciente, etc) (string)
- infectado_por: id del paciente que transmitio, -99: desconocido (numerico, entero)
- fecha_confirmacion: aa-mm-dd fecha en la que se confirmo la infeccion, o campo vacio si es desconocido (string)
- fecha_recuperacion: aa-mm-dd fecha en la que el paciente se recupero, o campo vacio si es desconocido (string)
- fecha_deceso: aa-mm-dd fecha en que el paciente fallecio, o campo vacio (string)
- estado: 0: aislado  1: recuperado  2: fallecido (numerico, entero)
- fuente: enlace a la fuente de la noticia en wayback machine (ver abajo) (string)


## falsos.csv
Continen informacion de casos falsos de corona virus: noticias falsas, desinformacion. Intentemos identificar el origen de estas falsas noticias y asi reconocer a los malos actores en la sociedad.

- id: numero de noticia de desinformacion (numerico, entero)
- sexo: sexo del supuesto paciente (string)
- fecha: aa-mm-dd en que aparecio la noticia falsa (string)
- noticia: hipervinculo a la noticia falsa en wayback machine (ver abajo) (string)
- verificacion: hipervinculo al document en el que se desmiente la noticia en wayback machine (ver abajo) (string)

### [Wayback Machine](https://archive.org/web/)?

Es una organizacion que almacena el internet. A este proyecto, sirve dos propositos:
1) Que la fuente de informacion quede almacenada permanentemente
2) Evitar que malos actores utilicen este espacio para distribuir desinformacion o contenido peligroso

Para crear un hipervinculo en wayback machine:

a) Ir a https://archive.org/web/:

b) Copiar el enlace a la fuente y pegarlo en la casilla "Save Page Now"

c) Click en el boton "Save Page"

d) Copiar el enlace a la nueva pagina. Este enlace inicia con https://web.archive.org: 
	- Ejemplo: https://web.archive.org/web/20200315072155/https://www.prensalibre.com/guatemala/comunitario/coronavirus-alejandro-giammattei-confirma-el-primer-caso-de-covid-19-en-guatemala/

Contacto: utiliza la pestana [issues](https://github.com/ncovgt2020/ncovgt2020/issues) para hacer sugerencias/comentarios, notificar sobre nuevos casos. Haz un pull request para contribuir. Escribe un correo a ncovgt2020[arroba]hotmail.com.
