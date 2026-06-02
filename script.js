// Esperamos a que el navegador haya leído todo el documento HTML principal
document.addEventListener("DOMContentLoaded", function() {
    
    // Función para cargar componentes HTML
    function cargarComponente(idContenedor, archivoHTML) {
        fetch(archivoHTML)
            .then(response => {
                if (!response.ok) {
                    throw new Error('No se pudo cargar ' + archivoHTML);
                }
                return response.text();
            })
            .then(data => {
                document.getElementById(idContenedor).innerHTML = data;
            })
            .catch(error => console.error('Error:', error));
    }

    // Inyectamos el Header y el Footer
    cargarComponente('header-placeholder', 'header.html');
    cargarComponente('footer-placeholder', 'footer.html');

});