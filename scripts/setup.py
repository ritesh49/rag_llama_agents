# #!/usr/bin/env python3
import os
import argparse

from huggingface_hub import hf_hub_download, snapshot_download
from transformers import AutoTokenizer

# from rag_service.paths import models_path, models_cache_path
# from rag_service.settings.settings import settings

models_path = '/Users/ritesh/Desktop/projects/rag_llama_agents/data'
models_cache_path = models_path + '/cache'
resume_download = True
llm_model_id = ''


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(prog='Setup: Download models from Hugging Face')
#     parser.add_argument('--resume', default=True, action=argparse.BooleanOptionalAction,
#                         help='Enable/Disable resume_download options to restart the download progress interrupted')
#     args = parser.parse_args()
#     resume_download = args.resume


def main():
    parser = argparse.ArgumentParser(prog='Setup: Download models from Hugging Face')
    parser.add_argument('--resume', default=True, action=argparse.BooleanOptionalAction,
                        help='Enable/Disable resume_download options to restart the download progress interrupted')
    parser.add_argument('--llm-model-id', required=True, help='Attach LLM Model Id to download the '
                                                              'huggingface model locally.')
    args = parser.parse_args()
    resume_download = args.resume
    llm_model_id = args.llm_model_id
    print('Downloading LLM model -- ', llm_model_id)


os.makedirs(models_path, exist_ok=True)
os.makedirs(models_cache_path, exist_ok=True)

# # Download Embedding model
# embedding_path = models_path / "embedding"
# print(f"Downloading embedding {settings().huggingface.embedding_hf_model_name}")
# snapshot_download(
#     repo_id=settings().huggingface.embedding_hf_model_name,
#     cache_dir=models_cache_path,
#     local_dir=embedding_path,
#     token=settings().huggingface.access_token,
# )
# print("Embedding model downloaded!")

# Download LLM and create a symlink to the model file
# print(f"Downloading LLM {settings().llamacpp.llm_hf_model_file}")
hf_hub_download(
    repo_id=llm_model_id,
    # filename=settings().llamacpp.llm_hf_model_file,
    cache_dir=models_cache_path,
    local_dir=models_path,
    resume_download=resume_download,
    token=os.getenv('HF_TOKEN'),
)
print("LLM model downloaded!")
#
# # Download Tokenizer
# if settings().llm.tokenizer:
#     print(f"Downloading tokenizer {settings().llm.tokenizer}")
#     AutoTokenizer.from_pretrained(
#         pretrained_model_name_or_path=settings().llm.tokenizer,
#         cache_dir=models_cache_path,
#         token=settings().huggingface.access_token,
#     )
#     print("Tokenizer downloaded!")
#
# print("Setup done")
