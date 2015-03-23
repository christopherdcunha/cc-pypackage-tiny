import setuptools


setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}.dev0",
    url="{{ cookiecutter.package_url }}",

    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",

    description="{{ cookiecutter.package_description }}",
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
