# RAG

## Intro

RAG stands for Retrieval-Augmented Generation.
Literally a LLM Generation Augmented with content Retrieved from an external source (through semantic search, web search, sql query, keyword search). 

Note that the augmentation applies to the LLM's input not the output. 

### RAG Flow when content is retrieved through semantic search 

Pre-step - Indexing the sources:
1. You index a list of documents (chunking + embedding)
2. You save the indexed chunks in an in-memory list or in a vector-db

Basic RAG Flow:
1. User gives you input
2. You embed the input and do semantic search against your indexed chunks 
3. You provide the retrieved chunks to the LLM
4. The LLM uses the chunks to generate an answer (you have to explicitly prompt it to do so, see the examples)

Agentic RAG Flow:
1. You tell the LLM that he can retrieve info from the external source (tool_calling)
2. The LLM tells you when he wants to use RAG and the input sentence
3. You embed the sentence received by the LLM and do semantic search among your indexed chunks
4. You give back the retrieved chunks to the LLM and tell the LLM to use this output to compose the answer
5. The LLM uses the search output to compose his answer

Note: 
- these are the flows for a RAG that uses semantic search (usually data in a vector db), similar flows happen for websearch, filesearch or other kinds of RAGs that do not require semantic search
- semantic search can have its own complexity and there are various techniques involved (different similarities, top n, rerank, llm as judge, ...)

Best practices:
- You should build the prompt by adding the retrieved content first and then the question so that the question is not lost in the middle of the content (the so-called lost in the middle effect).
- You should also explicitly tell the LLM that part of the input is retrieved info and that it should use only that to answer and should not add content from its own knowledge.

## Basic Example

```python

# this is a minimal rag, fixed content is retrieved from sql and given to the LLM
recipe = get_recipe_from_sql_query("pasta")

client = OpenAI()
response = client.responses.create(
    model="gpt-5-nano",
    instructions="you're a chef assistant, your goal is to create a bullet list of ingredients. You will be given a recipe retrieved from a database, use only ingredients found in the input to answer. If the input doesn't include any ingredients, say so explicitly instead of trying to answer with ungrounded info.",
    input=recipe
)
```


```python

# Another basic rag:
# the user selects a recipe using a GUI and asks a question about it
# the system retrieves the recipe from sql
# the system builds the prompt by appending the the user's question to the retrieved recipe
# 
# This example is closer to a realistic use case because it contains both retrieved content and a user question

user_selected_recipe = "pasta"
user_question = "can you tell me the ingredients needed for this recipe?" 
sql_recipe = get_recipe_from_sql_query(user_selected_recipe)

input = f"{sql_recipe} \n--- User question:\n {user_question}" 

client = OpenAI()
response = client.responses.create(
    model="gpt-5-nano",
    instructions="you're a chef assistant, your goal is to answer the user's question. You will be given a recipe retrieved from a database, use only the info included in the recipe to generate the answer. If the recipe doesn't contain enough info to answer, say so explicitly instead of trying to answer with ungrounded info.",
    input=input
)
```