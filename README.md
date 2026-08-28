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

- [x] Create Repository (see [Setup](#setup))
- [x] Poetry and VENV
- [x] f-string
- [x] Type hinting
- [x] Flow Control
- [x] List comprehension and generator expressions
- [x] Map, filter, zip, enumerate
- [x] Iterables, iterators, generator functions
- [x] Collections (list, tuples, set, dictionary, numpy arrays)
- [x] OOP (Dataclasses)
- [x] OOP (Pathlib Cross-platform file system)
- [x] Exceptions
- [x] Pydantic (validate input and output)
- [x] Context Managers (like the c# using)
- [x] Async/await using httpx (parallel api calls)
- [x] Pytest (fixtures, monkeypatch, marks)
- [ ] FastAPI (Starlette, ASGI, Raw ASGI implementation)
- [] More... (Logging, UUID, Regexp, Random, Threading, Numpy, Pandas, Pickle, SQLLite, Flask, Django)


### Module 2 - LLMs
- [ ] LLMs APIs (OpenAI, Anthropic, Deepseek v4 / Kimi K3)
- [ ] Handle LLM output with Pydantic
- [ ] Handle network errors with Tenacity
- [ ] LLMs SDKs
- [ ] Build yourself a multi-model architecture
- [ ] LangChain
- [ ] Task: app that communicate with LLM handling data streaming and network errors
- [ ] ...

### Module Futures
- [ ] Automate tests and evals in CICD
- [ ] Test that LLM produces only when the client is not saturated (token by token stream stops when client is saturated)
- [ ] Test that LLM drops if the client drops the connection
- [ ] Build an LLM - Andrej Karpathy
- [ ] Choose the right model
- [ ] Tradeoff between accuracy and speed, temperature, ...
- [ ] Bottlenecks 
- [ ] Lowra
- [ ] [Building AI Agents in Pure Python - Beginner Course](https://www.youtube.com/watch?v=bZzyPscbtI8)
- [ ] [Systematically Setup LLM Evals (Metrics, Unit Tests, LLM-as-a-Judge)](https://www.youtube.com/watch?v=a3SMraZWNNs)

## Structure

```
src/ai_engineer/   # Main source package
tests/             # Test files
```

## Notes

This is a learning repo — code here is exploratory and may be incomplete or experimental.

* Great source for python (including more): [mimo.org](https://mimo.org/glossary/python)
* Great tutorials: [Dave Ebbelaar on youtube](https://www.youtube.com/@daveebbelaar)