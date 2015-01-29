import setuptools

import {{ cookiecutter.module_name }}


setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version={{ cookiecutter.module_name }}.__version__,
    url="{{ cookiecutter.package_url }}",

    author={{ cookiecutter.module_name }}.__author__,
    author_email={{ cookiecutter.module_name }}.__email__,

    description=next(s for s in {{ cookiecutter.module_name }}.__doc__.split('\n') if s),
    long_description=open('README.rst').read(),

    py_modules=[
        "{{ cookiecutter.module_name }}",
    ],

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
