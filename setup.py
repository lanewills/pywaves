import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysinewave",
    version="0.0.7",
    author="David Davini",
    author_email="daviddavini@g.ucla.edu",
    description="Generate and play sine waves in real time, that can make smooth, continuous transitions in pitch and volume.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daviddavini/pysinewave",
    project_urls={
        'Source': 'https://github.com/daviddavini/pysinewave',
        'Tracker': 'https://github.com/daviddavini/pysinewave/issues',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy',
          'sounddevice',
    ],
    python_requires='>=3.6',
)