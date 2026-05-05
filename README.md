# AI Agents no DevOps — Lab (Codex CLI + GitHub)

Este repositório é um lab prático para demonstrar um fluxo real com **agentes de IA no DevOps**:

**issue → Codex CLI → commits → PR via `gh` → GitHub Actions valida**

## Pré-requisitos

- Python 3.11+ (ou 3.10+)
- `gh` autenticado (`gh auth status`)
- `codex` instalado e autenticado

## Rodando local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
make test
make lint
```

## O que o lab cobre

- Guardrails: PR obrigatório + CI como gate
- Instruções para agente via `AGENTS.md`
- Evidência “palpável”: PR, checks do Actions e histórico de issue
