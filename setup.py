from setuptools import setup, find_packages

setup(
    name='cpt-automation-cisco-packet-tracer',
    version='0.1.0',
    author='Niladri Das',
    author_email='ndas1262000@outlook.com',
    description='A Python library for automating tasks in Cisco Packet Tracer simulation environments.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/niladrridas/cpt-automation',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Development Status :: 3 - Alpha',
    ],
    keywords='Cisco Packet Tracer, network automation, simulation, network configuration',
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'beautifulsoup4',
        'selenium',
        'pyautogui',
        'pytesseract',
        'paramiko',
        'netmiko',
        'pyserial',
    ],
)
