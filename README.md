# DFD(Documentation-First Development) with FastAPI


## Introduce

### About this project

### Requirements

- You need to prepare some environments to run and test appliations.

#### Programming Language

- Python needs over 3.12
- Go needs over 1.20

#### Package Management

- Use [Poetry](https://python-poetry.org/) for managing Python packages.


## Table of Contents

### 1. Code generator through Open API for client developers

#### 1-1. openapi-typescript-codegen

- Introduce how client developers generate client codes through Open API specification on [01-code-generator-through-open-api-for-client-developers](./01-code-generator-through-open-api-for-client-developers/README.md).

### 2. A Conventional method of documentation

#### 2-1. Comments

- Introduce a conventional method to write a comment-based documentation on [02-introduce-a-conventional-method-to-write-a-comment-based-documentation](./02-introduce-a-conventional-method-to-write-a-comment-based-documentation/README.md).

#### 2-2. Metaprogramming

- Introduce metaprogramming with Open API generator in Go lanauge on [03-introduce-metaprogramming-with-open-api-generator-in-go-language](./03-introduce-metaprogramming-with-open-api-generator-in-go-language/README.md).

### 3. Code-based documentation

#### 3-1. FastAPI and Pydantic

- Introduce FastAPI and Pydantic with a code-based documentation on [04-introduce-fastapi-and-pydantic-with-a-code-based-documentation](./04-introduce-fastapi-and-pydantic-with-a-code-based-documentation/README.md).

### 4. A way of good documentation

#### 4-1. Efficientcy

- Introduce how to write a good code-based documentation on [05-introduce-how-to-write-a-good-code-based-documentation](./05-introduce-how-to-write-a-good-code-based-documentation/README.md).

#### 4-2. Security

- Introduce how to make a code-based documentation secured on [06-introduce-how-to-make-a-code-based-documentation-secured](./06-introduce-how-to-make-a-code-based-documentation-secured/README.md).


## Reference

### Conventional ways to build a documenation

- [Notion](https://0417taehyun.notion.site/e3104581f2d14c39be669a8de7b09b85?v=d2e0ef00d1704ff88bd59a21015b027f&pvs=4)
- [Postman](https://documenter.getpostman.com/view/25716380/2sA35Ba3WG)

### Code generator through Open API

- [openapi-typescript-codegen](https://github.com/ferdikoomen/openapi-typescript-codegen)
- [oapi-codegen](https://github.com/deepmap/oapi-codegen)

### Open API generator in Flask

- [flasgger](https://github.com/flasgger/flasgger)
- [apispec](https://github.com/marshmallow-code/apispec)

### FastAPI and Pydantic

- [fastapi](https://github.com/tiangolo/fastapi)
- [Sub application pattern with mount method in FastAPI](https://fastapi.tiangolo.com/advanced/sub-applications/)
- [Open API `docs` in FastAPI](https://fastapi.tiangolo.com/reference/openapi/docs/)
- [Declare request example data in FastAPI](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
- [pydantic](https://github.com/tiangolo/fastapi)
- [computed_fields decorator in Pydantic](https://docs.pydantic.dev/2.0/usage/computed_fields/)
- [json_schema_extra field in Pydantic](https://docs.pydantic.dev/2.0/usage/fields/#customizing-json-schema)
