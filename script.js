// --- LÓGICA PARA LEER LAS OFERTAS (Solo si existe la caja en la página) ---
    const contenedorDatos = document.getElementById('datos-api');
    
    if (contenedorDatos) {
        // Pedimos el archivo que ha generado nuestro Python
        fetch('empleos.json')
            .then(respuesta => respuesta.json())
            .then(datos => {
                // Vaciamos el mensaje de "Cargando..."
                contenedorDatos.innerHTML = '';
                
                // Si no hay datos
                if(datos.length === 0) {
                    contenedorDatos.innerHTML = '<p>No hay ofertas nuevas hoy.</p>';
                    return;
                }

                // Creamos una tarjeta bonita por cada empleo que encuentre
                datos.forEach(oferta => {
                    const tarjeta = document.createElement('div');
                    tarjeta.className = 'card';
                    tarjeta.innerHTML = `
                        <h3>${oferta.titulo}</h3>
                        <br>
                        <a href="${oferta.enlace}" target="_blank" class="btn">Inscribirse en el SEF</a>
                    `;
                    contenedorDatos.appendChild(tarjeta);
                });
            })
            .catch(error => {
                console.error("Error al cargar los datos:", error);
                contenedorDatos.innerHTML = '<p>Error al sincronizar con el radar. Vuelve a intentarlo más tarde.</p>';
            });
    }