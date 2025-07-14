# Flask HTTPS Simulation

A Flask application that demonstrates HTTPS enforcement and secure cookie handling in a development environment. This project simulates production-like behavior where HTTPS is mandatory for accessing secure features.

## Features

- **HTTPS Enforcement**: Automatically redirects HTTP requests to HTTPS
- **Secure Cookie Handling**: Demonstrates proper secure cookie implementation
- **SSL/TLS Support**: Uses self-signed certificates for local development
- **Production Simulation**: Mimics real-world security requirements

## Project Structure

```
flask_simulate_https/
├── app_https.py          # Main HTTPS-enabled Flask application
├── app_http.py           # HTTP server that enforces HTTPS redirect
├── srv.crt              # SSL certificate (self-signed)
├── srv.key              # SSL private key
├── templates/
│   ├── index.html       # Main secure page template
│   └── force_https.html # HTTPS enforcement warning page
├── env/                 # Virtual environment (excluded from git)
└── .gitignore          # Git ignore rules
```

## Prerequisites

- Python 3.6+
- Flask
- OpenSSL (for certificate generation)

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flask_simulate_https
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Generate SSL certificates** (if not present)
   ```bash
   openssl req -x509 -newkey rsa:4096 -keyout srv.key -out srv.crt -days 365 -nodes
   ```
   When prompted, you can use `localhost` as the Common Name (CN).

## Usage

### Running the HTTPS Server

Start the secure HTTPS server on port 5001:

```bash
python app_https.py
```

Access the application at: `https://localhost:5001`

**Note**: Your browser will show a security warning due to the self-signed certificate. Click "Advanced" and "Proceed to localhost" to continue.

### Running the HTTP Server (Optional)

To demonstrate HTTPS enforcement, you can also run the HTTP server:

```bash
python app_http.py
```

This server runs on port 5000 and will show an HTTPS enforcement message for any requests.

## How It Works

### HTTPS Enforcement (`app_https.py`)

- Uses Flask's `@app.before_request` decorator to check if requests are secure
- Non-HTTPS requests receive a 403 Forbidden response with instructions
- Secure requests proceed to the main application

### Secure Cookie Implementation

The application demonstrates secure cookie handling:

```python
resp.set_cookie("secure-token", "secure123", 
                secure=True,      # Only sent over HTTPS
                httponly=True,    # Not accessible via JavaScript
                samesite="None")  # Cross-site request handling
```

### Certificate Files

- `srv.crt`: Self-signed SSL certificate
- `srv.key`: Private key for the certificate

**Security Note**: These files are excluded from version control via `.gitignore` for security reasons.

## Security Features

- **Secure Cookies**: Cookies are only transmitted over HTTPS connections
- **HTTP-Only Cookies**: Prevents XSS attacks by making cookies inaccessible to JavaScript
- **HTTPS Enforcement**: All HTTP requests are blocked with informative error pages
- **SameSite Protection**: Helps prevent CSRF attacks

## Development vs Production

This setup simulates production behavior in a development environment:

- **Development**: Uses self-signed certificates for local testing
- **Production**: Would use certificates from a trusted Certificate Authority (CA)

## Browser Certificate Warnings

When accessing `https://localhost:5001`, browsers will show security warnings because:

1. The certificate is self-signed (not from a trusted CA)
2. The certificate may not match the exact hostname

This is expected behavior for development environments.

## Troubleshooting

### Certificate Issues

If you encounter certificate errors:

1. Regenerate certificates:
   ```bash
   rm srv.crt srv.key
   openssl req -x509 -newkey rsa:4096 -keyout srv.key -out srv.crt -days 365 -nodes
   ```

2. Ensure `localhost` is used as the Common Name when generating certificates

### Port Conflicts

If ports 5000 or 5001 are in use:

- Modify the `port` parameter in the respective `app.run()` calls
- Update documentation and templates accordingly

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and development purposes. Please ensure proper security measures are implemented before using in production environments.

## Security Disclaimer

This application uses self-signed certificates and is intended for development and educational purposes only. Do not use self-signed certificates in production environments. Always use certificates from trusted Certificate Authorities for production applications.
