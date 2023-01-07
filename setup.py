import setuptools

install_requires = open('requirements.txt').read().splitlines()

setuptools.setup(
    name="rmrf",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'rmrf=src.rmrf:safe_rmrf',
            'rmundo=src.rmrf:undo_rmrf'
        ]
    },
    include_package_data=True,
)
