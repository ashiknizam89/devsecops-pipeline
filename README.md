# DevSecOps CI/CD Security Pipeline

[![DevSecOps Security Pipeline](https://github.com/ashiknizam89/devsecops-pipeline/actions/workflows/devsecops.yml/badge.svg)](https://github.com/ashiknizam89/devsecops-pipeline/actions/workflows/devsecops.yml)

A DevSecOps pipeline built with GitHub Actions that runs static, container and dynamic security scans against a small Flask application.

The Flask app is intentionally vulnerable: it contains a hardcoded secret and runs with debug mode on, so the scanners have findings to report. Running Bandit locally on `app/` currently reports B105 (possible hardcoded password, `app.py` line 6) and B104 (binding to all interfaces, `app.py` line 30).

## Pipeline Overview

Every push to `main` and every pull request to `main` runs three scans in parallel, then a summary job:

| Job              | Tool      | Type             | Purpose                                                        |
| ---------------- | --------- | ---------------- | -------------------------------------------------------------- |
| SAST Scan        | Bandit    | Static Analysis  | Detects security issues in Python source code                  |
| Container Scan   | Trivy     | Image Scanning   | Finds CVEs (CRITICAL, HIGH) in the Docker image and dependencies |
| DAST Scan        | OWASP ZAP | Dynamic Analysis | Baseline scan of the running app for web vulnerabilities       |
| Security Summary | Custom    | Reporting        | Runs after the three scans and prints a completion summary; it doesn't read the reports |

The three scans report findings as artifacts (`bandit-sast-report`, `trivy-container-report`, `zap-dast-report`) without failing the build. A green run means the scans ran, not that nothing was found.

## Supply-chain pinning

- The third-party action `aquasecurity/trivy-action` is pinned to a full commit SHA, with the release tag in a comment.
- The scanner images are pinned by version tag and digest (`aquasec/trivy:0.70.0@sha256:…`, `ghcr.io/zaproxy/zaproxy:2.17.0@sha256:…`), so a moved tag can't change what runs.
- GitHub-owned actions (`actions/*`) use their current major version.

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
│   ├── app.py              # Intentionally vulnerable Flask application
│   └── requirements.txt    # Python dependencies
└── Dockerfile              # Container definition
```

## Security Concepts Demonstrated

- Shift-left security — scanning on every push and pull request, before deployment
- SAST + DAST combined coverage
- Container image CVE scanning
- Pinning third-party actions and scanner images against supply-chain changes
- Security-as-Code using GitHub Actions
- OWASP ZAP baseline scan of the running app

## How to Run Locally

```bash
# Build and run the app
docker build -t devsecops-demo .
docker run -p 5000:5000 devsecops-demo

# Run SAST scan locally
pip install bandit
bandit -r app/

# Run container scan locally
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:0.70.0 image devsecops-demo
```

## Next steps

- Fail pull requests on high/critical findings, with a reviewed baseline for known issues.
