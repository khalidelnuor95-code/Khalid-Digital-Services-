# Khalid Digital Services — Starter MVP

Arabic-first web platform starter for customers, service catalogue, orders, payment submissions, and transparent payment-risk triage.

## Stack
- Frontend: Next.js 15 / React 19
- Backend: FastAPI / SQLAlchemy
- Database: PostgreSQL 16
- Deployment: Docker Compose on Ubuntu 24.04

## Local / VPS deployment
1. Install Docker Engine and the Docker Compose plugin on Ubuntu 24.04.
2. Copy `.env.example` to `.env` and replace every placeholder with strong secrets.
3. Set `DATABASE_URL` password to the same value as `POSTGRES_PASSWORD`.
4. Run `docker compose up -d --build`.
5. Put Nginx or Caddy in front for HTTPS; do not expose database port publicly.
6. Open the web app on port 3000 and API docs at `/docs` on the API host.

## Current scope
- Customer records
- Service catalogue endpoint
- Order creation and listing
- Payment submission and review queue
- Basic duplicate-reference / missing-proof risk rules
- Dashboard counters

## Important before production
This is a development foundation, not a production-ready financial system. Add authentication, role-based authorization, audit logs, rate limits, backups, migrations, monitoring, secure file uploads, and admin approval controls before real use. The approval endpoint is deliberately marked as requiring admin authorization. Do not store bank passwords, OTPs, card data, or customers' sensitive credentials.

### Integrations
- MikroTik: implement RouterOS REST integration only after router address, RouterOS version, and restricted API credentials are supplied. Support Hotspot and PPPoE is planned; no router commands are executed by this starter.
- Banks: use official merchant/API or verified statement exports. SMS/screenshots are evidence to review, not authoritative proof of settlement.
- Starlink, Netflix, beIN, games: connect only through authorized partner/API or legitimate gift-card supply channels. This starter does not bypass provider restrictions or perform account verification on behalf of a provider.
- AI: current risk engine is explainable rule-based triage. Connect a hosted AI model later for OCR and anomaly explanations, with human review and privacy controls.

## Seed services
Add service rows to the `services` table before accepting orders. Suggested codes: `mikrotik-hotspot`, `mikrotik-pppoe`, `starlink-bill`, `starlink-verification-assistance`, `games-giftcards`, `netflix-giftcards`, `bein-renewal`.
