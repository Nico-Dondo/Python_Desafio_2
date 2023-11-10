from setuptools import setup, find_packages

setup(
    name='NombreDelPaquete',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    package_data={
        '': ['pre_entrega_1/*'],
    },
    entry_points={
        'console_scripts': [
            'mi_programa=paquete.main:main',
        ],
    },
)
