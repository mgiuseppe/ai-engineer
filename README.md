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

1. Install poetry using pipx (pipx let you install packages as standalone application in a separate environment)

2. Use poetry to create the project
```powershell
    # create the project
    > poetry new ai-engineer
    
    # enforce poetry to create .venv inside the project folder instead of using a centralized folder.
    # This ensures that vscode automatically recognizes the venv
    > poetry config virtualenvs.in-project true
    
    # generate the .venv and poetry.lock
    > poetry install

	# init repo and add default gitignore for python (this excludes .venv folder)
	git init
	curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore

	# .venv will be gitignored
	# poetry.lock will be committed (best practice for apps, should be gitignored for libraries)
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

### Module 1 - Python Fundamentals

- [X] Create Repository
- [X] Poetry and VENV
- [x] f-string
- [x] Type hinting
- [x] List comprehension, map
- [x] Control Flow (filter, zip, enumerate)
- [ ] Collections (list, set, dictionary)
- [ ] OOP
	- Dataclasses (per modello dati)
	- Pathlib (gestione fs cross-platform)
- [ ] Gestione eccezione
- [ ] Pydantic (validare input e output) e lavorare con risposte imprevedibili degli LLM
- [ ] Async/await con httpx (chiamate api parallele)
- [ ] Prompt engineering (zero shot, few-shot, role prompting)
- [ ] Task: applicazione che comunica con llm gestendo streaming dati ed errori di rete

## Structure

```
src/ai_engineer/   # Main source package
tests/             # Test files
```

## Notes

This is a learning repo — code here is exploratory and may be incomplete or experimental.