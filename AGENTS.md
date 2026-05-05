# AGENTS.md

Estas instruções orientam o agente a trabalhar com segurança neste repositório.

## Build/Setup
- Use `python3 -m venv .venv` e ative o ambiente.
- Instale dependências com `pip install -r requirements-dev.txt`.

## Qualidade (antes de abrir PR)
- Rode `make lint` e `make test`.

## Regras de mudança
- Nunca faça push direto na `main`. Trabalhe em branch e abra PR.
- Para correções, sempre inclua teste cobrindo o caso.

## Segurança
- Não imprima tokens, secrets ou variáveis sensíveis.
- Não adicione dependências desnecessárias.
