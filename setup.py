from setuptools import setup

setup(
    name="GenshinWiki",
    version="0.1",
    author="DeViantUa",
    packages=["GenshinWiki"],
    description="Python wrapper API for the Project Ambert and genshin-db for getting game information.",
    keywords="python api database wiki genshin genshin-impact".split(),
    python_requires=">=3.7",
    url="https://github.com/DEViantUA/GenshinWiki",
    project_urls={
        "Documentation": "https://github.com/DEViantUA/GenshinWiki",
    },
    install_requires=["requests", "browser-cookie3"],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
