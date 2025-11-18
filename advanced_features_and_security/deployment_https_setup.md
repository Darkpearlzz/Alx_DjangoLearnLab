# HTTPS & Security Configuration for Django Project

## 1. Django Security Settings

The following Django settings were added:

- SECURE_SSL_REDIRECT: Forces all connections over HTTPS
- HSTS enabled with a 1-year duration
- Cookies set to secure-only
- Clickjacking protection via X_FRAME_OPTIONS
- MIME sniffing disabled
- Browser XSS filter enabled

These settings ensure the application is only accessible securely.

## 2. SSL Certificate Setup

- Installed SSL certificates on the server under /etc/ssl/
- Configured Nginx/Apache to serve HTTPS traffic
- HTTP is redirected to HTTPS

## 3. Verification Steps

- Tested redirects from HTTP → HTTPS
- Verified secure cookies
- Confirmed HSTS using online tools
