
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
            alert("Se alcanzó el máximo de 5 contactos.");
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

const validarForm = () => {
    let isValid = false;
    // funciones auxiliares
    const validadorNombre = (nombre) => nombre && nombre.length >= 3 && nombre.length < 200;
    const validadorMail = (mail) => {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(mail);
    }
    const validadorTelefono = (tel) => !tel || (tel.length <= 13 && /^\+\d{3}\.\d{8}$/.test(tel));
    const validadorContacto = (valor) => valor.length >= 4 && valor.length <= 50;

    // inputs
    const sectorInput = document.getElementById("sector");
    const nombreInput = document.getElementById("nombre");
    const emailInput = document.getElementById("email");
    const telInput = document.getElementById("tel");
    const id_url_Input = containerContactos.querySelectorAll(".contacto-info");
    const radiosMascotaInput = document.querySelectorAll('input[name="mascota"]');

    if (!regionInput.value) {
       regionInput.style.borderColor = "red";
    } else {
        regionInput.style.borderColor = "";
    }

    if (!ComunaInput.value) {
        ComunaInput.style.borderColor = "red";
    } else {
        ComunaInput.style.borderColor = "";
    }

    if (sectorInput.value.length > 100) {
        sectorInput.style.borderColor = "red";
    } else {
        sectorInput.style.borderColor = "";
    }

    if (!validadorNombre(nombreInput.value)) {
        nombreInput.style.borderColor = "red";
    } else {
        nombreInput.style.borderColor = "";
    }

    if (!validadorMail(emailInput.value)) {
        emailInput.style.borderColor = "red";
    } else {
        emailInput.style.borderColor = "";
    }

    if (!validadorTelefono(telInput.value)) {
        telInput.style.borderColor = "red";
    } else {
        telInput.style.borderColor = "";
    }
    
    // validación de los id o url informados
    id_url_Input.forEach(input => {
        if (input.offsetParent !== null) {
            const id_url = input.value.trim();
            if (!validadorContacto(id_url)) {
                input.style.borderColor = "red";
            } else {
                input.style.borderColor = "";
            }
        }
    });

    return isValid;
}


let submitBtn = document.getElementById("enviar");
submitBtn.addEventListener("click", validarForm);