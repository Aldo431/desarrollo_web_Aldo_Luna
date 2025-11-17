# Tarea 4 - Desarrollo Web

## Github
Para la tarea se creó la rama Tarea-4 donde se encuentra todos los archivos relacionados con la tarea 4.

## Descripción

Se implementa una aplicación web con el framework springboot y usando comunicación asíncrona.

## Decisiones tomadas

- Para esta tarea se esta usando versión de Java 25 y springboot v3.5.7.
- Para esta tarea se creó un solo html que es index.html, que contiene todo para la tarea 4.
- Para la comunicación asíncrona use la función fetch.
- Las creación de carpetas tiene la misma disposición que la vista en auxiliar.
- Se hace la validación de la nota por parte del cliente y del servidor, si no pasa la validación, se envía una alerta indicando que la nota no es válida.

# Tarea 3 - Desarrollo Web

## Github
Para la tarea se creó la rama Tarea-3 donde se encuentra todos los archivos relacionados con la tarea 3.

## Descripción
Se implementa la comunicación asíncrona con el servidor usando fetch para obtener y enviar datos dinámicamente sin recargar la página para la página creada en la tarea 2.

## Decisiones tomadas

- Para la comunicación asíncrona use la función fetch.
- Para los gráficos utilice la biblioteca Highcharts.
- Para el formulario de comentarios se siguió una implementación parecida para los errores usada en el formulario de adopción, por parte de Javascript marca la casilla en color rojo si está mal y por parte del servidor si ve un error, manda el error en un json y sale un mensaje en el mismo formulario indicando que está mal.
- Se agrego seguridad extra en la parte de revisar el comentario por parte del servidor.

# Tarea 2 - Desarrollo Web

## Github
Para la tarea se creó la rama Tarea-2 donde se encuentra todos los archivos relacionados con la tarea 2.

## Descripción
Esta tarea incluye la implementación flask y jinja en la página creada en la tarea 1.

## Decisiones tomadas
- La estructura de las carpetas es la siguiente:
DESARROLLO_WEB_ALDO_LUNA/
│── flask_app/ 
│ ├── database/ 
│ ├── static/ 
│ │ ├── css/ 
│ │ ├── js/ 
│ │ ├── svg/ 
│ │ └── uploads/ 
│ ├── templates/
│ │ ├── adopcion/ 
│ │ └── form/ 
│ ├── utils/ 
│ │ └── validations.py 
│ └── app.py
│
├── img/ 
├── .gitignore
├── README.md 
└── requirements.txt

- Se mantiene casi todo con respecto a la tarea 1, solamente se realiza un cambio cuando se muestra el mensaje
al subirse el formulario a la base de datos, ya que antes se hacía en la pestaña que se abre al querer enviar el
formulario, pero ahora se muestra en la página principal luego de validar y subir el formulario.
- Al hacerse las validaciones por parte del servidor, si existe algún error se genera un mensaje de error que se muestra por sobre el formulario indicando que campo esta mal.
- Para la validación de las imágenes, se valida que se haya cargado una imagen, que tenga una extensión correcta,
que no tenga un nombre mal formado y además que su tamaño máximo sea de 5 MB.
- En las validaciones por parte del servidor, si un campo está mal, agrega un mensaje de error y recarga el formulario con los valores correctos ya ingresados y reinicia el valor que estaba malo, además que por temas de implementación cada vez que se recarga el formulario no se guardan las imágenes ingresadas pero todos los demas campos del formulario se guardan en caso de que se haya ingresado un valor.
- Todas las funcionalidades de la portada, listado, detalle y formulario están funcionando ahora con la base de datos.

# Tarea 1 - Desarrollo Web

## Github
Para la tarea se creó la rama Tarea-1 donde se encuentra todos los archivos relacionados con la tarea 1.

## Descripción
Esta tarea incluye la implementación de una página HTML con CSS.
   
## Decisiones tomadas
- Para la página principal y del listado se usaron tablas estáticas con un estilo que se encuentra en estilos.css
- Para el formulario, sus validaciones se encuentran en el archivo formulario.js, además para la confirmación se abre una nueva ventana que indica si quieres enviar el formulario o no, en caso de apretar si, en esa misma ventana sale un mensaje indicando el mensaje de que se envió el formulario, espera 4 segundos, luego se cierra la página y la página del formulario lleva a la página principal.
- Al hacer clic en una fila del listado, se carga una nueva página con el detalle, en esta, al hacer clic sobre la imagen, esta se amplía a un tamaño de 800x600 y aparece un botón "Cerrar" que permite restaurar la imagen a su tamaño original y ocultar nuevamente el botón.
- Los HTML que requerían poco Código de javascript, tienen el mismo código en el HTML, pero para el caso del formulario, cree un archivo aparte para que quedara más ordenado.
- Utilicé flexbox para organizar los elementos en el formulario.
- Agregué comentarios en el código para mayor claridad.
- Cree un css llamado estilos.css para que se utilice en cada HTML de la página.

