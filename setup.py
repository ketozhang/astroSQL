from setuptools import setup

setup(name='astrosql',
      version='0.1',
      description='Simple API to access to existing astronomical MySQL database',
      url='https://github.com/ketozhang/astroSQL',
      author='Keto Zhang, Weikang Zheng',
      author_email='keto.zhang@gmail.com, NA',
      packages=['astrosql'],
      install_requires=['peewee', 'termcolor', 'pymysql'],
      include_package_data=True,
      zip_safe=False)

