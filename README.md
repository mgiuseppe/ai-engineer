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
- [x] Async/await using httpx (parallel api calls, retries with tenacity)
- [x] Pytest (fixtures, monkeypatch, marks)
- [] More... (Logging, UUID, Regexp, Random, Threading, Numpy, Pandas, Pickle, SQLLite, Flask, Django)


### Module 2 - LLMs
- [x] LLMs APIs (OpenAI)
    - [x] Chatcompletion/v1 OPENAI
- [ ] LLMs SDKs
    - [x] OpenAI SDK
    - [x] Async endpoints
    - [x] Another provider/model using OpenAI SDK (Deepseek v4 / Kimi K3 / Qwen 3.8 / Groq)
    - [x] Handle LLM output with Pydantic
    - [x] Streaming
    - [x] Send file, audio, images, ...
    - [x] [Tool calling](https://developers.openai.com/api/docs/guides/tools)
        - [x] websearch / filesearch /
        - [x] function calling / tool search
        - [x] mcp
    - [ ] Anthropic SDK
- [ ] Evals
    - [ ] Simple Golden dataset (JSONL: input + expected output) and manually check evals
    - [ ] Compare models with evals (see 3_openai_sdk_structured_output to retrieve a nice usecase)
    - [ ] Regression check
    - [ ] Promptfoo
- [ ] Pipeline to load documents
    - [ ] [Get your data ready for AI](https://www.youtube.com/watch?v=9lBTS5dM27c)
        - [ ] Normalize and reduce noise (clean data and enrich with metadata)
        - [ ] Chunking and [embedding] (https://developers.openai.com/api/docs/guides/embeddings)
        - [ ] Vector DB and semantic search 
            - [ ] Choose a vector db (ChromaDB, PineCone, ...)
            - [ ] Similarity search and filtering algorithms 
- [ ] Cost Tracking
    - [ ] Tiktoken (estimation)
    - [ ] OpenAI Cost API
- [ ] Modular Architecture
    - [ ] Build yourself a multi-model architecture
    - [ ] LangChain (in 2023 this was the standard way to structure LLM apps, as of 2026/08 many consider its abstractions leaky and prefer a thin hand-built layer over the SDK)
- [ ] Prompt techniques ([prompting guide](https://developers.openai.com/api/docs/guides/prompt-engineering?prompt-example=prompt))
    - [ ] Chain of thought (as of today reasoning is directly provided by LLM models)
    - [ ] Zero shot / One shot / Few shot 
    - [ ] Role prompting
- [ ] Costing and latency (caching, choose a model, batching)
    - [ ] Choose the right model https://developers.openai.com/api/docs/guides/model-selection
    - [ ] Tradeoff between accuracy and speed, temperature
    - [ ] [Cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization)
    - [ ] [Prompt Caching](https://developers.openai.com/api/docs/guides/prompt-caching)
    - [ ] [Batching](https://developers.openai.com/api/docs/guides/batch)
    - [ ] [Flex Processing](https://developers.openai.com/api/docs/guides/flex-processing?api-mode=responses)
- [ ] Task: app that communicate with LLM handling data streaming and network errors

### Module 3 - RAGS
- [ ] RAG Pattern and LangChain to interact with external docs in real time
- [ ]
- [ ] Advanced Research
    - [ ] Conversational memory and retrieval
    - [ ] Re-Ranking
- [ ] Tool Calling
    - [ ] Web research
    - [ ] Interrogate Db
- [ ] Evaluate RAGS
    - [ ] RAGAS 
- [ ] Create a Golden Dataset
    - [ ] Benchmark
    - [ ] Failure points
- [ ] Optimize user queries
    - [ ] HyDE
    - [ ] Multi-Query
- [ ] Production hardening
    - [ ] Caching
    - [ ] Rate limiting
    - [ ] Error handling

### Module 4 - Agents
- [ ] Agentic Theory
    - [ ] Reasoning Loop -> Action
    - [ ] Linear Chains and Autonomous Agents
- [ ] ReACT Pattern (plan intermediate steps and interact with external environment)
- [ ] LangGraph (state and non-linear flows)
    - [ ] Graph architecture (nodes, conditional arcs, state)
    - [ ] Build System that can handle feedbacks and non-linear logics
        - [ ] HILT (Human in the loop)
            - [ ] Breakpoints and approvals
            - [ ] Checkpointing (pause, feedback, resume) 
- [ ] Multi Agent Systems
    - [ ] Specialized agents coordinated by a supervisor
    - [ ] Handoff strategies
    - [ ] Communication protocols among agents
- [ ] MCP
- [ ] [Voice Angent](https://developers.openai.com/api/docs/guides/voice-agents)
- [ ] Agentic RAG and Self Correction
    - [ ] Agents that decide when to use a tool and correct their own answers
    - [ ] Self-reflections techniques to score the results and guarantee accuracy (confidence) 

### Module 5 - Deploy and Agentic Coding
- [ ] Rest API with FastAPI (Starlette, ASGI, Raw ASGI implementation)
    - [x] Introduction and ASGI specification
    - [ ] Async Endpoints
    - [ ] DI
    - [ ] Streaming
- [ ] Dockerization
    - [ ] Multi-stage build
    - [ ] Securing environment variables
- [ ] CI/CD with GitHub actions
    - [ ] CI/CD Definitions 
    - [ ] Workflow to automate tests and evals (Automatic testing)
    - [ ] Code Quality validation
    - [ ] Continuous Deployment
- [ ] Observability (logs, tracing to understand where a multi-step chain breaks)
    - [ ] Monitoring LLM using Langsmith
        - [ ] LLM Calls Tracing
        - [ ] LLM Calls Debugging
    - [ ] Trulens (Alternative to Langsmith tracing and evals)
    - [ ] Langfuse (Alternative to Langsmith tracing and evals)
- [ ] Security Hardening 
    - [ ] Security protocols against prompt injection
    - [ ] Rate-Limiting systems
    - [ ] Validate input to protect infrastructure
    - [ ] Guardrails
- [ ] Agentic coding
    - [ ] Claude Code / Cursor / GitHub Copilot
    - [ ] VSCode + Claude Code
    - [ ] Autogenerate docs with AI
    - [ ] Autogenerate unit tests with AI
    - [ ] Refactor with AI  
        - [ ] LLMWiki
        - [ ] Graphify
    
### Module Futures
- [ ] [OpenAI Production BestPractices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ ] [Road Map by Dave Ebbelaar](https://www.youtube.com/watch?v=O2UmHpNlwUw)
- [ ] Pi Agent + Qwen 3.7 4b
- [ ] Realtime APIs
- [ ] LoRA (Fine-tuning)(another way to give info to the model)
- [ ] AI / Agentic Apps Architecture (High Level Architecture)
- [ ] [OpenResponses](https://www.openresponses.org/specification)
- [ ] Evals (dataset, metrics, regression test on prompts)
    - [ ] Golden dataset
    - [ ] [Systematically Setup LLM Evals (Metrics, Unit Tests, LLM-as-a-Judge)](https://www.youtube.com/watch?v=a3SMraZWNNs)
        - [ ] LLM Evals
        - [ ] Iteration and improvement
        - [ ] The analyze, measure, improve cycle
        - [ ] Unit Tests for LLMs
        - [ ] Human and model evaluations
        - [ ] Aligning LLM evaluators
        - [ ] Automated evaluators
        - [ ] A/B Testing
        - [ ] Evaluation Metrics
        - [ ] Common mistakes and key principles
- [ ] Failure design (what does the system do when the llm gives the wrong answer? not a technical matter but a business one!)
- [ ] Test that LLM produces only when the client is not saturated (token by token stream stops when client is saturated)
- [ ] Test that LLM drops if the client drops the connection
- [ ] Build an LLM - Andrej Karpathy
- [ ] Bottlenecks 
- [ ] Langfuse
- [ ] OpenRouter
- [ ] LiteLLM (alternative to OpenRouter, it also lets you define rate limit at gateway level)
- [ ] [Building AI Agents in Pure Python - Beginner Course](https://www.youtube.com/watch?v=bZzyPscbtI8)
    - [ ] Structured Output
    - [ ] Tool calling
    - [ ] Memory and retrieval
    - [ ] Prompt chaining
    - [ ] Routing Requests
    - [ ] Parallelization
    - [ ] Deploy AI App
- [ ] [Build reliable agents](https://www.youtube.com/watch?v=T1Lowy1mnEg)
    - [ ] AI Agents principles
    - [ ] Intelligence Layer
    - [ ] Memory
    - [ ] Tools
    - [ ] Validation
    - [ ] Control
    - [ ] Recovery
    - [ ] Feedback
- [ ] [Build a complete e2e AI project](https://www.youtube.com/watch?v=E8zpgNPx8jE)
    - [ ] News Scraper built on OpenAI 
    - [ ] News Scraper built on Anthropic
    - [ ] Create the pipeline
    - [ ] Database
    - [ ] Process articles
    - [ ] Implement Digest feature
    - [ ] Aggregator agent
    - [ ] Ranking articles by user profile
    - [ ] Email agent
    - [ ] Deploy and handling deployment errors
    - [ ] Optimizing code structure
- [x] [Pydantic crash course - build reliable Python and AI Applications](https://www.youtube.com/watch?v=PkQIREapb9o)
    - [x] Typehints
    - [x] BaseModel
    - [x] Validation and Fields
    - [x] Nested Models
    - [x] Pydantic Settings
    - [x] Structured Output with LLMs

## Structure

```
src/ai_engineer/   # Main source package
tests/             # Test files
```

## Notes

This is a learning repo — code here is exploratory and may be incomplete or experimental.

* Great source for python (including more): [mimo.org](https://mimo.org/glossary/python)
* Great tutorials: [Dave Ebbelaar on youtube](https://www.youtube.com/@daveebbelaar)