from setuptools import setup

setup(
    name='urlfwd',
    version='0.0.2',
    py_modules=['urlfwd','urlfwd.genpage','urlfwd.manage_links',
                'urlfwd.cli'
                ],
    install_requires=[
        'Click', 'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'genlinks = urlfwd.cli:generate_links',
            'addlink = urlfwd.cli:add_short_link',
        ],
    },
)