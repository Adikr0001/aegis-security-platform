# Aegis

**Aegis** is a security detection and attack-path analysis platform designed to identify security-relevant activity, correlate evidence into attack chains, and analyze potential attack paths.

> 🚧 **Work in Progress**

## Overview

Aegis analyzes security evidence and transforms individual observations into structured security findings. It then correlates related findings to identify attack chains and potential paths an attacker could take through a system.

## Current Capabilities

* Evidence normalization
* Authentication pattern detection
* Process pattern detection
* Network pattern detection
* Resource pattern detection
* Attack-chain correlation
* Attack-chain selection
* Security risk scoring
* Security finding generation
* Finding graph construction
* Attack-path discovery
* Attack-path analysis

## Architecture

```text
Security Evidence
       ↓
Evidence Normalization
       ↓
Pattern Detection
       ↓
Attack-Chain Correlation
       ↓
Chain Selection & Scoring
       ↓
Security Findings
       ↓
Finding Graph
       ↓
Attack-Path Analysis
```

## Project Structure

```text
Aegis/
├── aegis-api/
├── backend/
├── data/
├── frontend/
└── .gitignore
```

## Roadmap

* [x] Evidence normalization
* [x] Security pattern detection
* [x] Attack-chain correlation
* [x] Security finding generation
* [x] Finding graph
* [x] Attack-path analysis
* [ ] Spring Boot API layer
* [ ] Finding management API
* [ ] Attack-path visualization
* [ ] Security dashboard
* [ ] End-to-end integration
* [ ] Production hardening

## Status

Aegis is currently under active development. The Python security analysis engine is being developed first, followed by the Spring Boot platform/API layer and frontend integration.
