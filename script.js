// --- LÓGICA PARA LEER Y FILTRAR LAS OFERTAS ---
    const contenedorDatos = document.getElementById('datos-api');
    const selectorZona = document.getElementById('selector-zona');
    const textoActualizacion = document.getElementById('ultima-actualizacion');
    
    // Aquí guardaremos TODAS las ofertas para no tener que volver a pedirlas
    let todasLasOfertas = [];

    // Función que "pinta" las tarjetas en pantalla
    function renderizarOfertas(ofertasParaMostrar) {
        contenedorDatos.innerHTML = ''; // Limpiamos la pantalla
        
        if(ofertasParaMostrar.length === 0) {
            contenedorDatos.innerHTML = '<p>No hay ofertas activas para esta zona en este momento.</p>';
            return;
        }

        ofertasParaMostrar.forEach(oferta => {
            const tarjeta = document.createElement('div');
            tarjeta.className = 'card';
            tarjeta.innerHTML = `
                <h3>${oferta.titulo}</h3>
                <p style="color: #666; font-size: 0.9rem; margin: 10px 0;">📍 Zona: ${oferta.municipio || 'No especificado'}</p>
                <a href="${oferta.enlace}" target="_blank" class="btn">Inscribirse en el SEF</a>
            `;
            contenedorDatos.appendChild(tarjeta);
        });
    }

    if (contenedorDatos) {
        // Ponemos la hora virtual de actualización para dar confianza
        const ahora = new Date();
        textoActualizacion.innerText = `Última actualización: Hoy a las ${ahora.getHours()}:00`;

        // 1. Descargamos el archivo JSON masivo
        fetch('empleos.json')
            .then(respuesta => respuesta.json())
            .then(datos => {
                todasLasOfertas = datos; // Guardamos las ofertas en la recámara
                renderizarOfertas(todasLasOfertas); // Al principio, las mostramos todas
            })
            .catch(error => {
                console.error("Error:", error);
                contenedorDatos.innerHTML = '<p>Error al cargar. Vuelve a intentarlo.</p>';
            });

        // 2. Escuchamos cuando el usuario cambie el desplegable
        if (selectorZona) {
            selectorZona.addEventListener('change', function(evento) {
                const zonaElegida = evento.target.value;
                
                if (zonaElegida === 'todas') {
                    renderizarOfertas(todasLasOfertas); // Mostramos todas
                } else {
                    // Filtramos buscando el nombre del pueblo en el título de la oferta
                    // (Lo pasamos a minúsculas para que no falle por mayúsculas/minúsculas)
                    const filtradas = todasLasOfertas.filter(oferta => 
                        oferta.titulo.toLowerCase().includes(zonaElegida.toLowerCase())
                    );
                    renderizarOfertas(filtradas); // Mostramos solo las que coinciden
                }
            });
        }
    }