CURDIR    := $(abspath .)
API_DIR   := E:\projects\neurochar\backend\api
OUT_DIR   := $(CURDIR)/pb
DEPS_DIR  := $(CURDIR)/_proto_deps

ifeq ($(OS),Windows_NT)
  PYTHON := C:\Users\PC\AppData\Local\Programs\Python\Python311\python.exe
else
  PYTHON := python3
endif

GRPC_TOOLS_PROTO := $(shell "$(PYTHON)" -c "import grpc_tools, os; print(os.path.join(os.path.dirname(grpc_tools.__file__), '_proto').replace(os.sep, '/'))" 2>/dev/null)

ifeq ($(OS),Windows_NT)
  SHELL := cmd
  .SHELLFLAGS := /C
  MKDIR := mkdir
  RMDIR := rmdir /s /q
else
  MKDIR := mkdir -p
  RMDIR := rm -rf
endif

.PHONY: bin-deps deps generate-api generate

bin-deps:
ifeq ($(OS),Windows_NT)
	@ECHO == Installing Python deps ==
	@"$(PYTHON)" -m pip install grpcio-tools -q
	@ECHO == Python deps installed ==
else
	@echo "== Installing Python deps =="
	@$(PYTHON) -m pip install grpcio-tools -q
	@echo "== Python deps installed =="
endif

deps:
ifeq ($(OS),Windows_NT)
	@ECHO == Downloading external proto deps ==
	@IF NOT EXIST "$(DEPS_DIR)" $(MKDIR) "$(DEPS_DIR)"
	@curl -sL --create-dirs -o "$(DEPS_DIR)\google\type\date.proto" https://raw.githubusercontent.com/googleapis/googleapis/master/google/type/date.proto
	@curl -sL --create-dirs -o "$(DEPS_DIR)\google\api\annotations.proto" https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/annotations.proto
	@curl -sL --create-dirs -o "$(DEPS_DIR)\google\api\http.proto" https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/http.proto
	@curl -sL --create-dirs -o "$(DEPS_DIR)\google\api\httpbody.proto" https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/httpbody.proto
	@curl -sL --create-dirs -o "$(DEPS_DIR)\buf\validate\validate.proto" https://raw.githubusercontent.com/bufbuild/protovalidate/main/proto/protovalidate/buf/validate/validate.proto
	@curl -sL --create-dirs -o "$(DEPS_DIR)\protoc-gen-openapiv2\options\annotations.proto" https://raw.githubusercontent.com/grpc-ecosystem/grpc-gateway/main/protoc-gen-openapiv2/options/annotations.proto
	@curl -sL --create-dirs -o "$(DEPS_DIR)\protoc-gen-openapiv2\options\openapiv2.proto" https://raw.githubusercontent.com/grpc-ecosystem/grpc-gateway/main/protoc-gen-openapiv2/options/openapiv2.proto
	@ECHO == External deps ready ==
else
	@echo "== Downloading external proto deps =="
	@$(MKDIR) $(DEPS_DIR)
	@curl -sL --create-dirs -o $(DEPS_DIR)/google/type/date.proto https://raw.githubusercontent.com/googleapis/googleapis/master/google/type/date.proto
	@curl -sL --create-dirs -o $(DEPS_DIR)/google/api/annotations.proto https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/annotations.proto
	@curl -sL --create-dirs -o $(DEPS_DIR)/google/api/http.proto https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/http.proto
	@curl -sL --create-dirs -o $(DEPS_DIR)/google/api/httpbody.proto https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/httpbody.proto
	@curl -sL --create-dirs -o $(DEPS_DIR)/buf/validate/validate.proto https://raw.githubusercontent.com/bufbuild/protovalidate/main/proto/protovalidate/buf/validate/validate.proto
	@curl -sL --create-dirs -o $(DEPS_DIR)/protoc-gen-openapiv2/options/annotations.proto https://raw.githubusercontent.com/grpc-ecosystem/grpc-gateway/main/protoc-gen-openapiv2/options/annotations.proto
	@curl -sL --create-dirs -o $(DEPS_DIR)/protoc-gen-openapiv2/options/openapiv2.proto https://raw.githubusercontent.com/grpc-ecosystem/grpc-gateway/main/protoc-gen-openapiv2/options/openapiv2.proto
	@echo "== External deps ready =="
endif

generate-api: bin-deps deps
ifeq ($(OS),Windows_NT)
	@ECHO == Windows: generating Python pb ==
	-@$(RMDIR) "$(OUT_DIR)"
	@IF NOT EXIST "$(OUT_DIR)" $(MKDIR) "$(OUT_DIR)"
	@dir /s /b "$(API_DIR)\*.proto" > "$(CURDIR)\_proto_files.rsp"
	@"$(PYTHON)" -m grpc_tools.protoc -I"$(API_DIR)" -I"$(DEPS_DIR)" -I"$(GRPC_TOOLS_PROTO)" --python_out="$(OUT_DIR)" --grpc_python_out="$(OUT_DIR)" --pyi_out="$(OUT_DIR)" @"$(CURDIR)\_proto_files.rsp"
	-@del "$(CURDIR)\_proto_files.rsp"
	@ECHO == generation pb complete ==
else
	@echo "== Unix: generating Python pb =="
	-@$(RMDIR) $(OUT_DIR)
	@$(MKDIR) $(OUT_DIR)
	@find $(API_DIR) -name '*.proto' > $(CURDIR)/_proto_files.rsp
	@$(PYTHON) -m grpc_tools.protoc -I$(API_DIR) -I$(DEPS_DIR) -I$(GRPC_TOOLS_PROTO) --python_out=$(OUT_DIR) --grpc_python_out=$(OUT_DIR) --pyi_out=$(OUT_DIR) @$(CURDIR)/_proto_files.rsp
	-@rm -f $(CURDIR)/_proto_files.rsp
	@echo "== generation pb complete =="
endif

generate: generate-api
