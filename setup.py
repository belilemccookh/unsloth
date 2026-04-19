from setuptools import setup, find_packages
import os

# Read the README for the long description
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="unsloth",
    version="2024.1.0",
    description="2x faster, 60% less memory LLM finetuning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Unsloth AI",
    url="https://github.com/unslothai/unsloth",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.1",
        "tyro>=0.5.11",
        "accelerate>=0.26.0",
        "peft>=0.7.1",
        "bitsandbytes>=0.41.3",
        "protobuf<4.0.0",
        "huggingface_hub",
        "hf_transfer",
        "triton",
        "xformers",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "isort",
            "flake8",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="llm finetuning lora qlora efficient training",
    license="Apache 2.0",
)
