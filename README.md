# AI Engineer

Personal learning repository for AI engineering as an integrator — exploring how to build applications on top of LLMs and AI infrastructure using Python.

## Goals

- Understand and use LLM APIs (Claude, OpenAI, etc.)
- Experiment with tool calling / function calling patterns
- Explore vector databases and embedding workflows
- Build retrieval-augmented generation (RAG) pipelines
- Test agent frameworks and orchestration patterns

## Setup

Requires Python >= 3.14 and [Poetry](https://python-poetry.org/).

```bash
poetry install
```

* .venv will be gitignored and generated at poetry install
* poetry.lock will be committed

## Structure

```
src/ai_engineer/   # Main source package
tests/             # Test files
```

## Topics

| Topic | Description | Status |
|-------|-------------|--------|
| Python | Python Fundamentals | planned |
| LLM Tool Calls | Function/tool calling with LLMs | planned |
| Vector DBs | Embeddings and similarity search | planned |
| RAG | Retrieval-augmented generation pipelines | planned |
| Agents | Agentic workflows and orchestration | planned |
| Deploy and agentic coding | FastAPI, CI/CD, LangSmith, Unit Tests | planned |

<hr>

- [X] Repository
- [X] Poetry
- [X] VENV
- [x] f-string
- [x] Type hinting
- [x] List comprehension
- [ ] Manipolazione dati
    - Collezioni (liste, set, dizionari)
	- Controllo del flusso (zip, enumerate, filter)
- [ ] OOP
	- Dataclasses (per modello dati)
	- Pathlib (gestione fs cross-platform)
- [ ] Gestione eccezione
- [ ] Pydantic (validare input e output) e lavorare con risposte imprevedibili degli LLM
- [ ] Async/await con httpx (chiamate api parallele)
- [ ] Prompt engineering (zero shot, few-shot, role prompting)
- [ ] Task: applicazione che comunica con llm gestendo streaming dati ed errori di rete

## Notes

This is a learning repo — code here is exploratory and may be incomplete or experimental.

Steps done to initialize the project:
```bash
poetry new ai-engineer
poetry config virtualenvs.in-project true --local
poetry install
git init
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
```
