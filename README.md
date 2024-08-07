# ¿QUE ES TIME2ENJOY?

Time2Enjoy es una herramienta donde un usuario puede contratar o reservar un servicio del hotel. 


El usuario puede gestionar un calendario con las actividades que desea hacer, puede reservar y puede ver el aforo que tiene actualmente uno de los servicios.

## ¿Qué problema resolvemos? 
Gestionamos tu tiempo para que puedas aprovecharlo al máximo. Te aportamos tranquilidad para que disfrutes de tus vacaciones al máximo sin tener que pasar por colas/ esperas. Mientras otros esperan 1h para entrar en la sala de RV, aprovecha y date un chapuzón o date un capricho y ven a relajarte al SPA.

Aparte te iremos actualizando el itinerario para que no se te pase el tiempo de hacer tus actividades.

## ¿Que va a tener nuestra app?

Vamos a tener un cliente donde puedas observar todos los servicios del hotel, para ello te tendrás que registrar. 

Una vez tengamos tus datos vas a poder seleccionar cualquier servicio y vas a poder reservarlo a la hora que prefieras. Mientras lo haces te propondremos un horario y te diremos cuando hay menos aforo. Gracias a esto dispondrás de una mesa segura, de un masajista seguro,una niñera o servicio de guardería y aparte podrás disfrutar de la tranquilidad y no del barullo.


El hotel proporciona pulseras que  irán con NFC y los usuarios podrán fichar cada vez que entren, mediante este sistema podremos ver el aforo que tienen los servicios.

Apartados de la app:
Registro de usuarios, mediante el hotel cada vez que entre un usuario o mediante la app.
Lista de servicios con aforo
Formulario de reserva con propuestas de horario y aforo
Página del cliente con calendario.

## Flujo de nuestra app:

<img width="624" alt="Captura de pantalla 2024-08-07 a las 9 08 07" src="https://github.com/user-attachments/assets/a4caa16c-3334-4b19-a821-c86217581cfc">


## Casos de uso que soporta el flujo:

1. Lucas: Cliente final tiene una estancia en el Hotel Meliá y ha reservado el servicio SPA.
2. Pedro: Cliente final tiene una estancia en Hotel Meliá y ha reservado el servicio RV y tiene una estancia  en Hotel Samos el servicio  restaurante.
3. Mario: Staff del Hotel Samos, ha añadido un nuevo servicio al hotel Samos.



Estructura de datos:
Tenemos un Final Client que tiene relación con una estancia, debe tener relación con una estancia ya que si relacionamos con un hotel, un usuario no podría relacionarse con varios hoteles.
