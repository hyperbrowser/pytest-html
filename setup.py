from setuptools import setup

setup(
    name="pytest-html-profiling",
    use_scm_version=True,
    description="pytest plugin for generating HTML reports",
    long_description=open("README.rst").read(),
    author="Dave Hunt",
    author_email="dhunt@mozilla.com",
    url="https://github.com/hyperbrowser/pytest-html-profiling",
    packages=["pytest_html_profiling"],
    package_data={"pytest_html_profiling": ["resources/*"]},
    entry_points={"pytest11": ["html = pytest_html_profiling.plugin"]},
    setup_requires=["setuptools_scm"],
    install_requires=["pytest>=3.0", "pytest-metadata"],
    license="Mozilla Public License 2.0 (MPL 2.0)",
    keywords="py.test pytest html report",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
