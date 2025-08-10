# shakespeare-qa
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

A Python project for performing [document question answering (QA)](https://huggingface.co/tasks/document-question-answering
) on the complete works of William Shakespeare using [LangChain](https://github.com/langchain-ai/langchain) and [OpenAI](https://openai.com/).

## Overview

This project leverages modern language models to answer questions about Shakespeare's works. The source text is obtained from [MIT OCW](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt), and is included in this repository as `shaks12.txt`.

## Features

- Document QA over the entire Shakespeare corpus
- Integration with LangChain and OpenAI APIs
- Easily extensible for other document sources

## Installation and Dependencies

You can set up the project using either `uv` or `pip`:

### Using uv

1. Install [uv](https://github.com/astral-sh/uv) if you don't have it:
   ```sh
      curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Install dependencies:
   ```sh
      uv sync
   ```

### Using pip

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Or, if using [pyproject.toml](pyproject.toml):
   ```sh
   pip install .
   ```

## Usage

Run the main script:
```sh
python main.py
```

You will need to set your OpenAI API key as an environment variable:
```sh
export OPENAI_API_KEY=your-api-key
```

## Data Source

The Shakespeare text is sourced from [MIT OCW](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt).

## License

This project is distributed under the terms specified in the Shakespeare file's license.  
See [`shaks12.txt`](shaks12.txt) for copyright and distribution information.

## Contributing

Pull requests and suggestions are welcome!

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://openai.com/)
- [MIT OCW](https://ocw.mit.edu/)