# shakespeare-qa

A Python project for performing document question answering (QA) on the complete works of William Shakespeare using [LangChain](https://github.com/langchain-ai/langchain) and [OpenAI](https://openai.com/).

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
   pip install uv
   ```
2. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   ```
   Or, to use the lockfile:
   ```sh
   uv pip install --system --frozen
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

**License:**  
You must include the license text provided with the file, as it specifies terms for personal use and non-commercial distribution.  
See the relevant section in [`shaks12.txt`](shaks12.txt) for details.

## License

This project is distributed under the terms specified in the Shakespeare file's license.  
See [`shaks12.txt`](shaks12.txt) for copyright and distribution information.

## Contributing

Pull requests and suggestions are welcome!

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
-