# SE NECESITA AYUDA URGENTE

Si te parece importante este repositorio, ***porfavor ayudanos***. 

Necesitamos voluntarios queÑ
- Busquen, recopilen y verifiquen informacion. 
- Utilizando estos datos de Guatemala, contribuyan al [repositorio de latinoamérica](https://github.com/DataScienceResearchPeru/covid-19_latinoamerica).
- Generen visualizaciones a través de nuestros datos.

Escribenos un correo ncovgt2020@hotmail.com, o escribe un [issue](https://github.com/ncovgt2020/ncovgt2020/issues)

# Base de datos de pacientes infectados por corona virus en Guatemala

Descripcion: Esta es un dataset ***no oficial***, recopilado de fuentes oficiales, de los casos confirmados de Corona Virus en Guatemala.

Proposito: Que investigadores/desarrolladores/sociedad civil se informen y estudien la propagacion del virus corona NCOVID-19 en Guatemala. Proveer una base de datos para que otras personas desarrollen visualizaciones y analisis.

***Licencia: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)***
## Actualizaciones

22 de Mayo 2020: Ahora estamos recopilando el numero de pruebas utilizando los reportes de [OjoConMiPisto](https://twitter.com/_ojoconmipisto). ¡Gracias OjoConMiPisto!

## Estadisticas

confirmados:  3954

recuperados:  274

fallecidos:  63

activos 3600

pruebas realizadas:  28696

![alt tag](https://github.com/ncovgt2020/ncovgt2020/blob/master/imgs/resumen.png)
![alt tag](https://github.com/ncovgt2020/ncovgt2020/blob/master/imgs/pruebas.png)


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
	- 2: vuelo 6 de marzo ib	eria
	- 3: contacto con paciente 2 (primer fallecido)
	- 4: vuelo 26 de marzo, rescate de Espana
	- 5: contacto con familiar paciente 38 (este familiar de paciente 38 vino de Nueva York)_
	- 6: contacto con paciente 32, que a su vez tu contacto con familiar de paciente 2 (primer fallecido)
- razon_infeccion: causa de la infeccion (viaje, visita a familiar, visita a hospital, contacto con paciente, etc) (string)
- ingreso_guatemala: aa-mm-dd, si viajo al extranjero, fecha en que regreso a Guatemala, o campo vacio si es desconocido (string)
- infectado_por: id del paciente que transmitio, -99: desconocido (numerico, entero)
- fecha_inicio_sintomas: aa-mm-dd fecha en que se comienza a observar sintomas (string)
- fecha_confirmacion: aa-mm-dd fecha en la que se confirmo la infeccion, o campo vacio si es desconocido (string)
- fecha_recuperacion: aa-mm-dd fecha en la que el paciente se recupero, o campo vacio si es desconocido (string)
- fecha_deceso: aa-mm-dd fecha en que el paciente fallecio, o campo vacio (string)
- estado: 0: aislado  1: recuperado  2: fallecido (numerico, entero)
- fuente: enlace a la fuente de la noticia en wayback machine (ver abajo) (string)

## resumen_casos.csv

Contiene la informacion de casos confirmados, recuperados y fallecidos ordenados por dia. Debido a dificultad para conseguir informacion oficial, es posible que en el futuro cercano no logremos recopilar informacion por paciente, sino solo totales de cada dia.

- fecha: aa-mm-dd, fecha correspondiente a los datos (string)
- confirmados: confirmados en la fecha indicada (numerico, entero)
- recuperados: recuperados en la fecha indicada (numerico, entero)
- fallecidos: fallecidos en la fecha indicada (numerico, entero)
- fuente: fuente de informacion de los datos (string)


## falsos.csv 

***Actualizacion 07 de Abril 2020 ***
Tuvimos la intencion de recopilar informacion falsa que surge durante esta pandemia. Por la gran cantidad de tiempo que requiere, no le estamos haciendo desde el 15 de marzo de 2020. 


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
