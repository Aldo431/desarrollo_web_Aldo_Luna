
const regiones = {
    "Arica-y-parinacota": ["Arica", "Camarones", "Putre", "General Lagos"],
    "Tarapaca": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Pica"],
    "Antofagasta": ["Antofagasta", "Mejillones", "Taltal", "Calama", "San Pedro de Atacama"],
    "Atacama": ["Copiapó", "Caldera", "Tierra Amarilla", "Vallenar", "Huasco"],
    "Coquimbo": ["La Serena", "Coquimbo", "Ovalle", "Illapel", "Salamanca"],
    "Valparaiso": ["Valparaíso", "Viña del Mar", "Quilpué", "Villa Alemana", "San Antonio"],
    "Metropolitana": ["Santiago", "Providencia", "Ñuñoa", "Las Condes", "Maipú", "La Florida",
    "Puente Alto", "La Reina", "Vitacura", "Lo Barnechea", "Pedro Aguirre Cerda",
    "San Miguel", "Pudahuel", "Peñalolén", "La Granja", "Macul", "Ñuñoa",
    "Recoleta", "Quinta Normal", "San Joaquín", "San Ramón", "Cerrillos",
    "El Bosque", "Huechuraba", "Independencia", "La Cisterna", "Lo Espejo",
    "Lo Prado", "Pedro Aguirre Cerda", "Penaflor", "San Bernardo", "Talagante"],
    "Ohiggins": ["Rancagua", "San Fernando", "Rengo", "Machalí", "Pichilemu"],
    "Maule": ["Talca", "Curicó", "Linares", "Maule", "San Javier"],
    "Ñuble": ["Chillán", "Chillán Viejo", "Quirihue", "San Carlos", "Bulnes"],
    "Biobio": ["Concepción", "Talcahuano", "Hualpén", "Chillán", "Los Ángeles", "Coronel"],
    "Araucania": ["Temuco", "Villarrica", "Angol", "Pucón", "Lautaro"],
    "Los-rios": ["Valdivia", "La Unión", "Río Bueno", "Lanco", "Paillaco"],
    "Los-lagos": ["Puerto Montt", "Puerto Varas", "Castro", "Osorno", "Ancud"],
    "Aysen": ["Coyhaique", "Puerto Aysén", "Chile Chico", "Cisnes", "Guaitecas"],
    "Magallanes": ["Punta Arenas", "Puerto Natales", "Porvenir", "Puerto Williams", "Cabo de Hornos"]
};

// Inputs de region y comuna
const regionInput = document.getElementById("region");
const ComunaInput = document.getElementById("comuna");

// Para crear las opciones del select de regiones
for (const region in regiones) {
    const option = document.createElement("option");
    option.value = region;
    option.textContent = region
    regionInput.appendChild(option);
}

// Para actualizar comunas según la región
regionInput.addEventListener("change", () => {
    // Limpiar comunas actuales
    ComunaInput.innerHTML = '<option value="" disabled selected>Seleccione una comuna</option>';

    const comunas = regiones[regionInput.value] || [];
    comunas.forEach(comuna => {
        const option = document.createElement("option");
        option.value = comuna.toLowerCase().replace(/\s+/g, '-');
        option.textContent = comuna;
        ComunaInput.appendChild(option);
    });
});

const maxContactos = 5;
const contactoInput = document.getElementById("contacto");
const infoInput = document.getElementById("contacto-info");
const containerContactos = document.getElementById("contactos-container");


containerContactos.addEventListener("change", (e) => {
    if (e.target.classList.contains("contacto-select")) {
        const input = e.target.nextElementSibling; 
        input.style.display = e.target.value ? "inline-block" : "none";
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

const maxFotos = 5;
const fotosContainer = document.getElementById("fotos-container");

fotosContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("agregar-foto")) {
        const items = fotosContainer.querySelectorAll(".foto-item");
        if (items.length >= maxFotos) {
            return;
        }

        const nuevoItem = items[0].cloneNode(true);
        nuevoItem.querySelector(".foto-input").value = ""; // limpiar archivo
        fotosContainer.appendChild(nuevoItem);
    }
});

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
    
    // validación de los id o url informados
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

     }
    return isValid;
}


let submitBtn = document.getElementById("enviar");
submitBtn.addEventListener("click", validarForm);