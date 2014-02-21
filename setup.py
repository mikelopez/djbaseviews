from setuptools import setup, find_packages
import sys, os

setup(
    name='djbaseviews',
    version='0.1',
    description="djbaseviews Description",
    keywords='',
    author='',
    author_email='',
    url='',
    license='MIT',
    package_dir={'djbaseviews': 'djbaseviews'},
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Security",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)

