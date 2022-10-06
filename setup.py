from setuptools import find_packages, setup


setup(
    name="sample-package",
    version="0.2.1",
    python_requires=">=3.8",
    install_requires=[
        "numpy >= 1.1.0",
        "matplotlib",
        "wheel"
    ],
    dependency_links = [
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "run_sample_package=sample_package.main:main",
        ]
    },
    author="Maksim Surov",
    author_email="maxim.surov@talantiuspeh.ru",
    description="Sample Package",
)
