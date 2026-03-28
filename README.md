# DevSecOps CI/CD Security Pipeline

A fully automated DevSecOps pipeline built with GitHub Actions that integrates security scanning at every stage of the software development lifecycle.

## Pipeline Overview

Every push to `main` automatically triggers 4 security jobs in parallel:

| Job              | Tool      | Type             | Purpose                                       |
| ---------------- | --------- | ---------------- | --------------------------------------------- |
| SAST Scan        | Bandit    | Static Analysis  | Detects security issues in Python source code |
| Container Scan   | Trivy     | Image Scanning   | Finds CVEs in Docker image and dependencies   |
| DAST Scan        | OWASP ZAP | Dynamic Analysis | Tests running app for web vulnerabilities     |
| Security Summary | Custom    | Reporting        | Aggregates all scan results                   |

## Tools & Technologies

- **GitHub Actions** — CI/CD automation
- **Bandit** — Python SAST (Static Application Security Testing)
- **Trivy** — Container & dependency vulnerability scanning
- **OWASP ZAP** — DAST (Dynamic Application Security Testing)
- **Docker** — Application containerisation
- **Flask** — Target web application

## Project Structure

```
devsecops-pipeline/
├── .github/
│   └── workflows/
│       └── devsecops.yml   # Pipeline definition
├── app/
│   ├── app.py              # Flask web application
│   └── requirements.txt    # Python dependencies
└── Dockerfile              # Container definition
```

## Security Concepts Demonstrated

- Shift-left security — catching vulnerabilities before production
- SAST + DAST combined coverage
- Container image hardening and CVE scanning
- Automated security gates in CI/CD pipelines
- Security-as-Code using GitHub Actions
- OWASP Top 10 automated testing

## How to Run Locally

```bash
# Build and run the app
docker build -t devsecops-demo .
docker run -p 5000:5000 devsecops-demo

# Run SAST scan locally
pip install bandit
bandit -r app/

# Run container scan locally
docker run --rm aquasec/trivy:latest image devsecops-demo
```
