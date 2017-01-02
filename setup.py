from setuptools import setup, find_packages

setup(name='django-nox',
      version='0.0.4',
      description='Statistics middleware and analysis tools for django',
      url='https://github.com/destino74/django-django_nox',
      author='destino74',
      author_email='ljf6670601@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests', 'config']),
      # packages=['django_nox', 'django_nox.migrations', 'django_nox.management', 'django_nox.management.commands'],
      install_requires=[
            'texttable',
            'markdown',
      ],
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
      ],
      zip_safe=False)
