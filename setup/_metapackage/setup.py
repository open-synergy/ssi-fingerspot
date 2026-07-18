import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-fingerspot",
    description="Meta package for open-synergy-ssi-fingerspot Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_fingerspot',
        'odoo14-addon-ssi_fingerspot_operating_unit',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
