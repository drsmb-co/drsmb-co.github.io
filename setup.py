from setuptools import setup

setup(
    name='urlfwd',
    version='0.0.1',
    py_modules=['urlfwd','urlfwd.genpage'
                ],
    install_requires=[
        'Click', 'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'genlinks = urlfwd.genpage:generate_links',
        ],
    },
)