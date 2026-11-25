# Vulnerability Scanner & Exploit Lab

A modular Python security testing toolkit designed for automated vulnerability scanning, response comparison, payload probing, and proof-of-concept exploitation against a local test server[span_0](start_span)[span_0](end_span).

## Project Structure

- `lab_server.py` – Local vulnerable target server used for safe testing and lab simulation[span_1](start_span)[span_1](end_span).
- `scanner.py` – Main scanning engine that coordinates probes and analyzes responses[span_2](start_span)[span_2](end_span).
- `probes.py` – Collection of test payloads and injection vectors used during scanning[span_3](start_span)[span_3](end_span).
- `comparator.py` – Response diffing and comparison utility to detect anomalies or behavioral changes[span_4](start_span)[span_4](end_span).
- `exploit.py` – Proof-of-concept exploitation script targeting identified vulnerabilities[span_5](start_span)[span_5](end_span).
- `step1_request.py` – Initial baseline HTTP request module[span_6](start_span)[span_6](end_span).
- `step2_singlepayload.py` – Single-payload injection and validation test script[span_7](start_span)[span_7](end_span).
- `test_step3.py` – Automated verification and multi-step test suite[span_8](start_span)[span_8](end_span).

## Getting Started

### Prerequisites
- Python 3.8+
- Required dependencies (install via `pip` if applicable, e.g., `requests`, `flask`)

### Usage

1. **Start the local test lab server:**
   ```bash
   python lab_server.py
2.Run the vulnerability scanner:
  bash
  python scanner.py
3.Run individual test steps or the exploit script:
 bash
 python step1_request.py
python step2_singlepayload.py
python test_step3.py
python exploit.py
Disclaimer!! 
​This tool is intended strictly for educational purposes and authorized security testing in controlled lab environments. Do not use against systems without explicit permission.*(Note: Feel free to share what specific vulnerability type—such as SQLi, XSS, or SSRF—this project targets or any CLI arguments it accepts if you'd like me to tailor the sections further!)*
