# pacha - Ollama assistant

Me having a play

Firstly install Ollama for windows, and probably reboot, then create the model

## To create the AI model

Init only or reset

```console
ollama pull llama3.2
ollama rm pacha
```

```console
ollama create pacha -f Modelfile
```

## To run the model

```console
ollama serve pacha
```

or to run interactively

```console
ollama run pacha
```

## Use python to create a chat interface

create a python environment

```console
python -m venv
````

```console
pip install streamlit PyPDF2 langchain-community langchain pillow PyMuPDF chromadb

streamlit run main.py
```
