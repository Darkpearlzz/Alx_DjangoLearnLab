# Security Review Report

## Implemented Security Measures

1. Forced HTTPS using SECURE_SSL_REDIRECT.
2. Configured HSTS to ensure browsers always use secure connections.
3. Secured session and CSRF cookies.
4. Added headers:
   - X-Frame-Options: DENY
   - X-Content-Type-Options: nosniff
   - Browser XSS Filter
5. HTTPS enabled via SSL certificate on the server.

## Improvements Possible

- Implement CSP (Content Security Policy)
- Add rate limiting at server level
- Configure automated certificate renewals with Certbot
