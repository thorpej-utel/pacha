# pacha - Ollama assistant

Me having a play

- Install ollama for windows

```console
pip install streamlit PyPDF2 langchain-community langchain pillow PyMuPDF chromadb
pip install streamlit
pip install langchain_community
streamlit run main.py
```

## To create the AI model

Init only or reset

```console
ollama pull codel
ollama rm fang
```

```console
ollama create fang -f Modelfile
```

## To run the model

```console
ollama run fang
```
