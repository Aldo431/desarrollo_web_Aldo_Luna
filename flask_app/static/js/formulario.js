
// Inputs de región y comuna
const regionInput = document.getElementById("region");
const comunaInput = document.getElementById("comuna");

// Logica para el select de comuna

Array.from(comunaInput.options).forEach(option => {
    if (option.value) {  
        option.style.display = "none";
    }
});

regionInput.addEventListener("change", () => {
    const regionId = regionInput.value;

    Array.from(comunaInput.options).forEach(option => {
        if (!option.value) return; 
        if (option.dataset.region == regionId) {
            option.style.display = "block";
        } else {
            option.style.display = "none";
        }
    });

    comunaInput.selectedIndex = 0;
});

// Lógica para agregar contactos
const maxContactos = 5;
const containerContactos = document.getElementById("contactos-container");

const cambiarVisibilidadInput = (select) => {
    const input = select.nextElementSibling;
    if (select.value) {
        input.style.display = "inline-block";
    } else {
        input.style.display = "none";
    }
};

const actualizarBotonesAgregar = () => {
    const items = containerContactos.querySelectorAll(".contacto-item");
    items.forEach((item, index) => {
        const boton = item.querySelector(".agregar-contacto");
        if (boton) {
            if (index === items.length - 1 && items.length < maxContactos) {
                boton.style.display = "inline-block";
            } else {
                boton.style.display = "none";
            }
        }
    });
};

const agregarContacto = () => {
    const items = containerContactos.querySelectorAll(".contacto-item");
    if (items.length >= maxContactos) return;

    const nuevoItem = items[0].cloneNode(true);
    const select = nuevoItem.querySelector(".contacto-select");
    const input = nuevoItem.querySelector(".contacto-info");

    select.value = "";
    input.value = "";
    input.style.display = "none";

    containerContactos.appendChild(nuevoItem);
    actualizarBotonesAgregar();
};

containerContactos.addEventListener("change", (e) => {
    if (e.target.classList.contains("contacto-select")) {
        cambiarVisibilidadInput(e.target);
    }
});

containerContactos.addEventListener("click", (e) => {
    if (e.target.classList.contains("agregar-contacto")) {
        agregarContacto();
    }
});


// Lógica para la fecha
const fechaInput = document.getElementById("fecha-disponible");

if (!fechaInput.value) {   
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
}

// Lógica para agregar fotos
const maxFotos = 5;
const fotosContainer = document.getElementById("fotos-container");

const agregarFoto = () => {
    const items = fotosContainer.querySelectorAll(".foto-item");

    if (items.length >= maxFotos) {
        return;
    }

    const nuevoItem = items[0].cloneNode(true);
    const input = nuevoItem.querySelector(".foto-input");

    input.value = "";
    fotosContainer.appendChild(nuevoItem);

    actualizarBotonesFotos();
};

const actualizarBotonesFotos = () => {
    const items = fotosContainer.querySelectorAll(".foto-item");
    items.forEach((item, index) => {
        const boton = item.querySelector(".agregar-foto");
        if (boton) {
            if (index === items.length - 1 && items.length < maxFotos) {
                boton.style.display = "inline-block";
            } else {
                boton.style.display = "none";
            }
        }
    });
};

fotosContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("agregar-foto")) {
        agregarFoto();
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

    if (!comunaInput.value) {
        msg += "n";
        comunaInput.style.borderColor = "red";
    } else {
        comunaInput.style.borderColor = "";
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
        "/confirmacion",   
        "Confirmacion",  
        "width=500,height=300,top=150,left=400,resizable=no"
        );
    }

    return isValid;
}


let submitBtn = document.getElementById("enviar");
submitBtn.addEventListener("click", validarForm);