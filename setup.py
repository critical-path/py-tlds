from setuptools import (
    find_packages,
    setup
)


setup(
    name="py-tlds",
    version="1.0.0",
    description="util that retrieves and validates a list of top-level domains from the internet assigned names authority",
    url="https://github.com/critical-path/py-tlds",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords="python util top-level-domains tlds internet-assigned-names-authority iana",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "responses"
        ]
    },
    entry_points={
        "console_scripts": [
            "tlds=tlds.cli:get_tlds"
        ]
    }
)
