from setuptools import setup, find_packages

setup(
    name='pranav_tic_tac_toe',
    version='1.0.0',
    author='Pranav',
    author_email='your.email@example.com',
    description='A simple Tic Tac Toe command-line game',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'tic-tac-toe=tic_tac_toe.game:play_game',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
