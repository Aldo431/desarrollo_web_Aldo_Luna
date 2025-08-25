
const regiones = {
    "Arica y parinacota": ["Arica", "Camarones", "Putre", "General Lagos"],
    "Tarapaca": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Pica", "Huara", "Camiña", "Colchane"],
    "Antofagasta": ["Antofagasta", "Mejillones", "Taltal", "Calama", "San Pedro de Atacama", "Tocopilla", "María Elena", "Ollagüe", "Sierra Gorda"],
    "Atacama": ["Copiapó", "Caldera", "Tierra Amarilla", "Vallenar", "Huasco", "Chañaral", "Diego de Almagro", "Freirina", "Alto del Carmen"],
    "Coquimbo": ["La Serena", "Coquimbo", "Ovalle", "Illapel", "Salamanca", "Vicuña", "Andacollo", "Los Vilos", "Combarbalá", "Punitaqui", "Paihuano", "Río Hurtado", "Monte Patria", "La Higuera", "Mincha"],
    "Valparaíso": [
        "Valparaíso", "Viña del Mar", "Quilpué", "Villa Alemana", "San Antonio", "Quillota", "La Calera", "Limache", "Olmué", "Puchuncaví", "Quintero", "Casablanca", "Concón", "Cartagena",
        "Algarrobo", "El Quisco", "El Tabo", "Juan Fernández", "Petorca", "Cabildo", "Papudo", "La Ligua", "Zapallar", "Putaendo", "Santa María", "San Felipe", "Catemu", "Llay Llay",
        "Nogales", "Hijuelas", "Isla de Pascua", "Santo Domingo", "Calle Larga", "Rinconada", "San Esteban"
    ],
    "Ohiggins": [
        "Rancagua", "San Fernando", "Rengo", "Machalí", "Pichilemu", "San Vicente", "Santa Cruz", "Requínoa", "Mostazal", "Navidad", "Codegua", "Graneros", "Olivar", "Doñihue", "Coinco",
        "Coltauco", "Quinta de Tilcoco", "Las Cabras", "Peumo", "Pichidegua", "Malloa", "La Estrella", "Marchigüe", "Litueche", "Paredones", "Peralillo", "Placilla", "Chimbarongo",
        "Palmilla", "Nancagua", "Pumanque", "Chépica", "Lolol"
    ],
    "Maule": [
        "Talca", "Curicó", "Linares", "Maule", "San Javier", "Constitución", "Parral", "Cauquenes", "Molina", "Teno", "Romeral", "Rauco", "Sagrada Familia", "Hualañé", "Vichuquén", "Licantén",
        "Río Claro", "Curepto", "Pelarco", "Pencahue", "San Clemente", "Empedrado", "San Rafael", "Colbún", "Villa Alegre", "Yerbas Buenas", "Longaví", "Retiro", "Chanco", "Pelluhue"
    ],
    "Ñuble": [
        "Chillán", "Chillán Viejo", "San Carlos", "Quirihue", "Bulnes", "Coihueco", "Pemuco", "Ñiquén", "Cobquecura", "San Fabián", "Ninhue", "Trehuaco", "San Nicolás", "Portezuelo", "Pinto",
        "Coelemu", "San Ignacio", "Ránquil", "Quillón", "El Carmen", "Yungay"
    ],
    "Biobío": [
        "Concepción", "Talcahuano", "Hualpén", "Chiguayante", "Los Ángeles", "Coronel", "Lota", "San Pedro de la Paz", "Tomé", "Florida", "Penco", "Hualqui", "Santa Juana", "Cabrero", "Yumbel",
        "Tucapel", "Antuco", "San Rosendo", "Laja", "Quilleco", "Nacimiento", "Negrete", "Santa Bárbara", "Quilaco", "Mulchén", "Alto Biobío", "Arauco", "Curanilahue", "Los Álamos", "Lebu",
        "Cañete", "Contulmo", "Tirúa"
    ],
    "Araucanía": [
        "Temuco", "Padre Las Casas", "Villarrica", "Pucón", "Angol", "Nueva Imperial", "Carahue", "Traiguén", "Lautaro", "Victoria", "Cholchol", "Curacautín", "Lonquimay", "Melipeuco", "Cunco",
        "Perquenco", "Galvarino", "Freire", "Pitrufquén", "Teodoro Schmidt", "Gorbea", "Tolten", "Curarrehue", "Loncoche", "Puerto Saavedra", "Ercilla", "Renaico", "Collipulli", "Los Sauces",
        "Purén", "Lumaco"
    ],
    "Los Ríos": [
        "Valdivia", "La Unión", "Río Bueno", "Lanco", "Mariquina", "Panguipulli", "Corral", "Paillaco", "Futrono", "Lago Ranco", "Máfil", "Los Lagos"
    ],
    "Los Lagos": [
        "Puerto Montt", "Puerto Varas", "Castro", "Osorno", "Ancud", "Quellón", "Frutillar", "Fresia", "Chaitén", "Puyehue", "Río Negro", "Purranque", "Puerto Octay", "Maullín", "Calbuco",
        "Cochamó", "Quemchi", "Dalcahue", "Curaco de Vélez", "Chonchi", "Queilén", "Quinchao", "Puqueldón", "Futaleufú", "Palena", "Hualaihué", "San Pablo", "San Juan"
    ],
    "Aysén": [
        "Coyhaique", "Puerto Aysén", "Chile Chico", "Cisnes", "Guaitecas", "Lago Verde", "Río Ibáñez", "Cochrane", "Tortel", "O’Higgins"
    ],
    "Magallanes": [
        "Punta Arenas", "Puerto Natales", "Porvenir", "Puerto Williams", "Torres del Paine", "Laguna Blanca", "San Gregorio", "Río Verde", "Primavera", "Timaukel", "Antártica"
    ],
    "Metropolitana": [
        "Santiago", "Providencia", "Ñuñoa", "Las Condes", "Maipú", "La Florida", "Puente Alto", "La Reina", "Vitacura", "Lo Barnechea", "Pedro Aguirre Cerda", "San Miguel", "Pudahuel",
        "Peñalolén", "La Granja", "Macul", "Recoleta", "Quinta Normal", "San Joaquín", "San Ramón", "Cerrillos", "El Bosque", "Huechuraba", "Independencia", "La Cisterna", "Lo Espejo", "Lo Prado",
        "Cerro Navia", "Estación Central", "Peñaflor", "San Bernardo", "Talagante", "Buin", "Calera de Tango", "Padre Hurtado", "Tiltil", "Colina", "Lampa", "Conchalí", "Quilicura", "Renca",
        "San José de Maipo", "Pirque", "Isla de Maipo", "Curacaví", "María Pinto", "Melipilla", "San Pedro", "Alhué", "El Monte"
    ]
};

// Inputs de region y comuna
const regionInput = document.getElementById("region");
const ComunaInput = document.getElementById("comuna");

// Para crear las opciones del select de regiones
for (const region in regiones) {
    const option = document.createElement("option");
    option.value = region;
    option.textContent = region;
    regionInput.appendChild(option);
}

// Para actualizar comunas según la región
regionInput.addEventListener("change", () => {
    ComunaInput.innerHTML = '<option value="" disabled selected>Seleccione una comuna</option>';

    const comunas = regiones[regionInput.value] || [];
    comunas.forEach(comuna => {
        const option = document.createElement("option");
        option.value = comuna;
        option.textContent = comuna;
        ComunaInput.appendChild(option);
    });
});

// Logica para agregar contactos
const maxContactos = 5;
const contactoInput = document.getElementById("contacto");
const infoInput = document.getElementById("contacto-info");
const containerContactos = document.getElementById("contactos-container");

containerContactos.addEventListener("change", (e) => {
    if (e.target.classList.contains("contacto-select")) {
        const input = e.target.nextElementSibling; 
        if (e.target.value) {
            input.style.display = "inline-block";
        } else {
            input.style.display = "none";
        }
    }
});

containerContactos.addEventListener("click", (e) => {
    if (e.target.classList.contains("agregar-contacto")) {
        const items = containerContactos.querySelectorAll(".contacto-item");
        if (items.length >= maxContactos) {
            return;
        }
        const nuevoItem = items[0].cloneNode(true);
        nuevoItem.querySelector(".contacto-select").value = "";
        const nuevoInput = nuevoItem.querySelector(".contacto-info");
        nuevoInput.value = "";
        nuevoInput.style.display = "none";
        containerContactos.appendChild(nuevoItem);
    }
});

// Logica para la fecha
const fechaInput = document.getElementById("fecha-disponible");
const fechaInicio = new Date();
fechaInicio.setHours(fechaInicio.getHours() + 3);

const año = fechaInicio.getFullYear();
const mes = String(fechaInicio.getMonth() + 1).padStart(2, '0');
const dia = String(fechaInicio.getDate()).padStart(2, '0');
const hora = String(fechaInicio.getHours()).padStart(2, '0');
const minuto = String(fechaInicio.getMinutes()).padStart(2, '0');
const fechaFormateada = `${año}-${mes}-${dia}T${hora}:${minuto}`;
fechaInput.value = fechaFormateada;
fechaInput.min = fechaFormateada;

//Logica para agregar fotos
const maxFotos = 5;
const fotosContainer = document.getElementById("fotos-container");

fotosContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("agregar-foto")) {
        const items = fotosContainer.querySelectorAll(".foto-item");
        if (items.length >= maxFotos) {
            return;
        }

        const nuevoItem = items[0].cloneNode(true);
        nuevoItem.querySelector(".foto-input").value = ""; 
        fotosContainer.appendChild(nuevoItem);
    }
});

// Logica para validar formulario
const validarForm = () => {

    let msg = "";
    let isValid = false;
    // funciones auxiliares
    const validadorNombre = (nombre) => nombre && nombre.length >= 3 && nombre.length < 200;
    const validadorMail = (mail) => {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(mail);
    };
    const validadorTelefono = (tel) => !tel || (tel.length <= 13 && /^\+\d{3}\.\d{8}$/.test(tel));
    const validadorContacto = (valor) => valor.length >= 4 && valor.length <= 50;
    const validadorRadio = (name) => {
        const radios = document.querySelectorAll(`input[name="${name}"]`);
        return Array.from(radios).some(radio => radio.checked);
    };
    const validadorCantidad = (cantidad) => cantidad && cantidad > 0;
    const validarFechaDisponible = () => {
    const valor = new Date(fechaInput.value);
    const ahoraMas3 = new Date();
    ahoraMas3.setHours(ahoraMas3.getHours() + 3, ahoraMas3.getMinutes(), 0, 0);
    if (valor >= ahoraMas3) {
        return true;
    } else {
        return false;
    }
    };
    const validadorFotos = () => {
        const fotoInputs = fotosContainer.querySelectorAll(".foto-input");
        let contador = 0;

        fotoInputs.forEach(input => {
            if (input.files.length > 0) contador++;
        });

        if (contador < 1 || contador > maxFotos) {
            return false;
        } else {
            return true;
        }
    };

    // inputs
    const sectorInput = document.getElementById("sector");
    const nombreInput = document.getElementById("nombre");
    const emailInput = document.getElementById("email");
    const telInput = document.getElementById("tel");
    const id_url_Input = containerContactos.querySelectorAll(".contacto-info");
    const cantidadInput = document.getElementById("cantidad");
    const edadInput = document.getElementById("edad");

    // validaciones
    if (!regionInput.value) {
       msg += "n";
       regionInput.style.borderColor = "red";
    } else {
        regionInput.style.borderColor = "";
    }

    if (!ComunaInput.value) {
        msg += "n";
        ComunaInput.style.borderColor = "red";
    } else {
        ComunaInput.style.borderColor = "";
    }

    if (sectorInput.value.length > 100) {
        msg += "n";
        sectorInput.style.borderColor = "red";
    } else {
        sectorInput.style.borderColor = "";
    }

    if (!validadorNombre(nombreInput.value)) {
        msg += "n";
        nombreInput.style.borderColor = "red";
    } else {
        nombreInput.style.borderColor = "";
    }

    if (!validadorMail(emailInput.value)) {
        msg += "n";
        emailInput.style.borderColor = "red";
    } else {
        emailInput.style.borderColor = "";
    }

    if (!validadorTelefono(telInput.value)) {
        msg += "n";
        telInput.style.borderColor = "red";
    } else {
        telInput.style.borderColor = "";
    }
    id_url_Input.forEach(input => {
        if (input.offsetParent !== null) {
            const id_url = input.value.trim();
            if (!validadorContacto(id_url)) {
                msg += "n";
                input.style.borderColor = "red";
            } else {
                input.style.borderColor = "";
            }
        }
    }); 

    if (!validadorRadio("mascota")) {
        msg += "n";
        document.getElementById("tipo-mascota-input").style.border = "2px solid red";
    } else {
        document.getElementById("tipo-mascota-input").style.border = "";
    }

    if (!validadorCantidad(cantidadInput.value)) {
        msg += "n";
        cantidadInput.style.borderColor = "red";
    } else {
           cantidadInput.style.borderColor = "";
    }

    if (!validadorCantidad(edadInput.value)) {
        msg += "n";
        edadInput.style.borderColor = "red";
    } else {
        edadInput.style.borderColor = "";
    }

    if (!validadorRadio("unidad")) {
        msg += "n";
        document.getElementById("tipo-unidad-input").style.border = "2px solid red";
    } else {
        document.getElementById("tipo-unidad-input").style.border = "";
    }

    if (!validarFechaDisponible()) {
        msg += "n";
        fechaInput.style.borderColor = "red";        
    } else {
        fechaInput.style.borderColor = "";
    }

    if (!validadorFotos()) {    
        msg += "n";
        fotosContainer.style.border = "2px solid red";      
    } else {
        fotosContainer.style.border = "";
    }

    if (msg === ""){
       isValid = true;
       window.open(
        "confirmacion.html",   
        "Confirmacion",  
        "width=500,height=300,top=150,left=400,resizable=no"
        );
    }

    return isValid;
}


let submitBtn = document.getElementById("enviar");
submitBtn.addEventListener("click", validarForm);