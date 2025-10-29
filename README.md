# GitLeaks Pattern Testing Repository

A comprehensive security testing repository containing intentionally vulnerable code and exposed secrets for testing various security scanning tools.

## 🎯 Purpose

This repository is designed for testing and demonstrating:
- **CodeQL** - Static code analysis for security vulnerabilities
- **GitLeaks** - Secret detection and credential scanning
- **Dependabot** - Automated dependency updates
- **GitHub Secret Scanning** - Native GitHub secret detection

## 📂 Repository Structure

```
gitleaks-pattern/
├── patterns/                          # 154+ files with exposed secrets
│   └── *.py                          # Test cases for various API keys, tokens, passwords
├── vulnerable_sql_injection.py       # SQL Injection vulnerabilities
├── vulnerable_xss.py                 # Cross-Site Scripting (XSS) vulnerabilities
├── vulnerable_command_injection.py   # Command Injection vulnerabilities
├── vulnerable_path_traversal.py      # Path Traversal vulnerabilities
├── vulnerable_insecure_deserialization.py  # Deserialization vulnerabilities
├── vulnerable_weak_crypto.py         # Weak cryptography examples
├── vulnerable_xxe.py                 # XML External Entity (XXE) vulnerabilities
├── vulnerable_ssrf.py                # Server-Side Request Forgery (SSRF)
├── requirements.txt                  # Python dependencies
└── .github/
    ├── dependabot.yml               # Dependabot configuration
    └── workflows/
        ├── codeql.yml               # CodeQL advanced scanning
        ├── codeql-analysis.yml      # CodeQL standard scanning
        └── gitleaks.yml             # GitLeaks secret scanning
```

## 🔐 Vulnerabilities Included

### 1. **SQL Injection** (`vulnerable_sql_injection.py`)
- String concatenation in queries
- Unparameterized SQL statements
- Dynamic query construction

### 2. **Cross-Site Scripting (XSS)** (`vulnerable_xss.py`)
- Unescaped user input
- Reflected XSS
- Template injection

### 3. **Command Injection** (`vulnerable_command_injection.py`)
- Shell command execution with user input
- `os.system()` vulnerabilities
- `subprocess` with `shell=True`

### 4. **Path Traversal** (`vulnerable_path_traversal.py`)
- Unsanitized file paths
- Directory traversal attacks
- File access vulnerabilities

### 5. **Insecure Deserialization** (`vulnerable_insecure_deserialization.py`)
- `pickle.loads()` from untrusted data
- Unsafe YAML loading
- `eval()` and `exec()` usage

### 6. **Weak Cryptography** (`vulnerable_weak_crypto.py`)
- MD5/SHA1 hashing
- Weak encryption algorithms (DES)
- Hardcoded credentials and API keys

### 7. **XML External Entity (XXE)** (`vulnerable_xxe.py`)
- Unsafe XML parsing
- DTD processing enabled

### 8. **Server-Side Request Forgery (SSRF)** (`vulnerable_ssrf.py`)
- Unvalidated URL fetching
- Internal network access

### 9. **Exposed Secrets** (`patterns/*.py`)
- API keys (AWS, Azure, Google Cloud, etc.)
- Database credentials
- Authentication tokens
- Private keys

## 🛠️ GitHub Actions Workflows

### CodeQL Analysis
- **Workflow**: `.github/workflows/codeql.yml`, `.github/workflows/codeql-analysis.yml`
- **Triggers**: Push to main/git-leaks-code, PRs, weekly schedule
- **Purpose**: Detects security vulnerabilities in Python code

### GitLeaks Secret Scanning
- **Workflow**: `.github/workflows/gitleaks.yml`
- **Triggers**: Push, PRs, daily schedule
- **Purpose**: Scans for exposed secrets and credentials

### Dependabot
- **Config**: `.github/dependabot.yml`
- **Target Branch**: `git-leaks-code`
- **Purpose**: Automated dependency updates for `requirements.txt`

## ⚠️ WARNING

**THIS CODE IS INTENTIONALLY INSECURE!**

- **DO NOT** use this code in production
- **DO NOT** deploy these applications
- **FOR TESTING PURPOSES ONLY**

This repository is meant for:
- Security tool validation
- Training and education
- CI/CD pipeline testing
- Vulnerability scanner benchmarking

## 🚀 Setup

```bash
# Clone the repository
git clone <repository-url>
cd gitleaks-pattern

# Install dependencies (optional, for local testing)
pip install -r requirements.txt

# Run vulnerable apps (for testing only)
python vulnerable_sql_injection.py
```

## 📊 Expected Scan Results

When properly configured, security scans should detect:

- **CodeQL**: 50+ security vulnerabilities across all files
- **GitLeaks**: 154+ exposed secrets in the patterns directory
- **Dependabot**: Outdated dependencies with known CVEs

## 🔧 Configuration

### Dependabot
- Checks for updates weekly
- Targets branch: `git-leaks-code`
- Labels PRs with: `pip dependencies`

### CodeQL
- Runs on: Push, Pull Requests, Weekly schedule
- Language: Python
- Queries: Security-extended pack

### GitLeaks
- Runs daily at 2 AM UTC
- Uploads reports as artifacts
- Comments on PRs with findings

## 📝 License

This is a testing repository. Use at your own risk for educational purposes only.

## 🤝 Contributing

This is a testing repository. Contributions should maintain the intentionally vulnerable nature of the code for security scanning validation.

---

**Remember**: This code contains real vulnerability patterns. Never use these patterns in production code!
