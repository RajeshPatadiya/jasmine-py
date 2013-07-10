import re
from setuptools import setup, find_packages

requirements = []
non_pypi_requirements = []

with open("requirements.txt", 'r') as f:
    for requirement in f:
        requirement = requirement.strip()

        if requirement.startswith("#") or not requirement:
            continue
        elif requirement.startswith("http"):
            non_pypi_requirements.append(requirement)
            requirements.append(re.match(r'.*#egg=(?P<egg>.*)', requirement).group('egg'))
        else:
            requirements.append(requirement)

setup(
    name="jasmine-py",
    version="2.0",
    url="http://pivotal.github.io/jasmine/",
    author="Pivotal Labs",
    author_email="jasmine-js@googlegroups.com",
    description=('A high-level Python Web framework that encourages '
                 'rapid development and clean, pragmatic design.'),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    scripts=['jasmine/standalone.py', 'jasmine/ci.py'],

    packages=find_packages(),

    install_requires=requirements,

    include_package_data=True,

    dependency_links=non_pypi_requirements
)
