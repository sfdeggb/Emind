#!/usr/bin/env python3
"""
Emind - AI Music Recommendation and Generation System
"""

from setuptools import setup, find_packages
import os

# 读取README文件
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# 读取requirements文件
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="emind",
    version="1.0.0",
    author="Emind Team",
    author_email="emind@example.com",
    description="AI Music Recommendation and Generation System",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sfdeggb/Emind",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "ui": [
            "gradio>=3.0",
            "streamlit>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "emind=emind.cli.interface:main",
            "emind-server=emind.ui.web.server:main",
        ],
    },
    include_package_data=True,
    package_data={
        "emind": [
            "templates/**/*",
            "models/**/*",
            "skills/**/*",
        ],
    },
    zip_safe=False,
)
