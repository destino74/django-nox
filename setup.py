from setuptools import setup
setup(name='django-nox',
      version='0.1',
      description='Statistics middleware and analysis tools for django',
      url='https://github.com/destino74/django-nox',
      author='destino74',
      author_email='ljf6670601@gmail.com',
      license='MIT',
      packages=['nox'],
      install_requires=[
            'texttable',
            'markdown',
      ],
      classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            'Operating System :: OS Independent',
            'Programming Language :: Python',
      ],
      zip_safe=False)
