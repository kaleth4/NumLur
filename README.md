# 📱 NumLur — Phone Number OSINT Tool

```
************************************
*        ___   _                   *
*       / / \ | |_   _ _ __ __     *
*      | ||  \| | | | | '_ ` _     *
*     < < | |\  | |_| | | | | | \  *
*      | ||_| \_|\__,_|_| |_| |_|  *
*       \_\                        *
************************************
```

Script de reconocimiento pasivo (OSINT) para números de teléfono móvil. Permite verificar si un número es real, obtener información de geolocalización del operador y abrir un chat directo en WhatsApp.

---

## ⚙️ Features

- ✅ Validación de formato del número (10–15 dígitos)
- 🌍 Consulta en tiempo real vía **APILayer Number Verification**
- 📋 Muestra: país, operador, tipo de línea, formato internacional/local, ubicación y estado de validez
- 💬 Apertura directa de chat en WhatsApp por número
- 🖥️ Compatible con Windows y Linux/macOS

---

## 📦 Requisitos

- Python 3.7+
- Cuenta en [apilayer.com](https://apilayer.com) (plan gratuito disponible)

### Instalación de dependencias

```bash
pip install requests colorama
```

---

## 🔑 Configuración

1. Crea una cuenta en [apilayer.com](https://apilayer.com/marketplace/number_verification-api)
2. Copia tu API Key
3. En el archivo principal, reemplaza:

```python
API_KEY = "TU_API_KEY_AQUI"
```

---

## 🚀 Uso

```bash
python numlur.py
```

### Menú principal

```
1) Consultar número     → Verifica si el número existe y muestra info del operador
2) Abrir chat WhatsApp  → Abre el número directamente en WhatsApp Web
3) Salir
```

### Ejemplo de output

```
[+] Result:

Country code        : CO
Number              : 3216543210
Country name        : Colombia
Country prefix      : +57
International format: +573216543210
Line type           : mobile
Local format        : 3216543210
Location            : Colombia
Valid               : True
```

---

## ⚠️ Disclaimer

Esta herramienta es solo para fines educativos y de investigación en seguridad. Úsala únicamente sobre números de tu propiedad o con autorización explícita. El autor no se responsabiliza por el uso indebido.

---

## 👤 Autor

**Kaled Corcho** — [github.com/kaleth4](https://github.com/kaleth4)  
Cybersecurity Analyst Jr. | Ethical Hacking | OSINT
