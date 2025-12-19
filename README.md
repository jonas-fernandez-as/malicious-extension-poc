# 🔐 Instagram Session Hijacking - Educational Proof of Concept

<div align="center">

![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask 2.0+](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)
![License MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange.svg)

**⚠️ EDUCATIONAL USE ONLY**

![YouTube Video Tutorial](https://img.shields.io/badge/YouTube-Video_Tutorial-red.svg)
[![Instagram @jonastrikex](https://img.shields.io/badge/Instagram-@jonastrikex-purple.svg)](https://www.instagram.com/jonastrikex/)
[![TikTok @jonastrikex](https://img.shields.io/badge/TikTok-@jonastrikex-black.svg)](https://www.tiktok.com/@jonastrikex)

</div>

### 🚨 CRITICAL WARNING - READ BEFORE PROCEEDING

<div align="center" style="border: 3px solid #ff4444; padding: 20px; border-radius: 10px; background-color: #fff0f0; margin: 20px 0;">

**⚠️ FOR EDUCATIONAL PURPOSES ONLY ⚠️**  
THIS IS A TECHNICAL DEMONSTRATION IN A CONTROLLED ENVIRONMENT  

**NEVER** use this knowledge to:  

- Access accounts that don't belong to you  
- Violate other people's privacy  
- Perform illegal activities  

**LEGAL CONSEQUENCES:**  

- Unauthorized computer access is a **CRIME** in most countries  
- Can result in severe fines and imprisonment  
- Permanent damage to your professional career  

**✅ PERMITTED USE:**  

- Learning in isolated labs  
- Authorized security research  
- Improving personal/organizational defenses  
- Ethical cybersecurity training  

</div>

### 📹 Complete Video Explanation

<div align="center">

[![WATCH FULL DEMONSTRATION](https://via.placeholder.com/800x450/ff0000/ffffff?text=WATCH+FULL+DEMONSTRATION)](https://www.youtube.com/watch?v=your_video_id_here)  

*Click the image to watch the complete demonstration on YouTube (reemplaza el link con tu video real)*

</div>

### 📖 Project Description

This repository contains an educational Proof of Concept (PoC) demonstrating Session Hijacking techniques through cookie theft. The objectives are:

1. Demonstrate how an attacker could potentially access accounts without credentials  
2. Educate about the risks of unverified browser extensions  
3. Provide practical defense tools and knowledge  

### ⚡ Technologies Used

- Python 3.8+ with Flask for the collector server  
- JavaScript for malicious browser extensions (DEMO)  
- HTML/CSS for the fake landing page  
- Multi-browser support (Firefox and Chrome)  

### 🗂️ Repository Structure

malicious-extension-poc/
│
├── malicious_v2/              # Firefox-based extension (Manifest V2)
│   ├── manifest.json
│   ├── background.js
│   ├── content.js
│   └── icons/
│       ├── icon-48.png
│       └── icon-96.png
│
├── malicious_v3/              # Chrome-based extension (Manifest V3)
│   ├── manifest.json
│   ├── background.js
│   ├── content.js
│   ├── popup.html
│   └── icons/
│       ├── icon-48.png
│       └── icon-96.png
│
├── server/                    # Attacker's collector server
│   ├── server.py
│   ├── requirements.txt
│   └── stolen_data.log
│
├── web_page/                  # Fake landing page for the attack
│   ├── index.html
│   ├── Privacy_Shield_ProV5.2.1.xpi
│   └── Privacy_Shield_ProV5.2.1.zip
│
├── cookie.png                 # Diagrama del ataque
└── README.md

### 🔬 How the Attack Works (Technical Overview)

#### Attack Architecture

<div align="center">

![Diagrama de robo de cookies](cookie.png)

</div>

**Key Components:**

1. **Malicious Extensions** (`malicious_v2/`, `malicious_v3/`)
   - v2: Firefox-compatible (Manifest V2)
   - v3: Chrome-compatible (Manifest V3)
   - Both steal cookies from multiple websites
   - Send stolen data to the attacker's server

2. **Collector Server** (`server/`)
   - Simple Flask application
   - Receives POST requests with stolen cookies
   - Logs all received data

3. **Fake Landing Page** (`web_page/`)
   - Professional-looking fake website to trick users into installing the extension

### 🌐 Connect with the Creator

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-Website-blue?style=for-the-badge)](https://jonas-fernandez-as.github.io)
[![Instagram](https://img.shields.io/badge/Instagram-@jonastrikex-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/jonastrikex/)
[![TikTok](https://img.shields.io/badge/TikTok-@jonastrikex-000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@jonastrikex)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jon%C3%A1s-fern%C3%A1ndez-as)
[![YouTube](https://img.shields.io/badge/YouTube-Channel-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@tu_canal) <!-- Pon tu canal real -->

</div>

<div align="center">

**Found this useful?**  
⭐ Star this repo · 📢 Share responsibly · 🔔 Subscribe for more cybersecurity content  

*"Cybersecurity knowledge is a scalpel: in wrong hands it causes harm, in expert hands it saves digital lives."*

</div>
