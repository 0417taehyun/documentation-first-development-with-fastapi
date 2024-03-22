NAME=oapi-codegen-example-

.PHONY: build
build:
	@go build -o $(NAME)

.PHONY: run
run: build
	@./$(NAME)

.PHONY: docs
docs:
	@go run -mod=mod github.com/deepmap/oapi-codegen/cmd/oapi-codegen --config=openapi/.oapi-codegen/config.yaml openapi/openapi.yaml
	