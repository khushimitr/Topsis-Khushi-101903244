from distutils.core import setup
setup(
  name = 'Topsis-Khushi-101903244',         
  packages = ['Topsis-Khushi-101903244'],  
  version = '0.1',      
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Calculate Topsis score and save it in a csv file',
  author = 'Khushi Singhal',                   
  author_email = 'khushi.mitr03@gmail.com',     
  url = 'https://github.com/khushimitr/Topsis-Khushi-101903244',
  download_url = 'https://github.com/khushimitr/Topsis-Khushi-101903244/archive/refs/tags/v0.1.tar.gz',
  keywords = ['TOPSISSCORE', 'RANK', 'DATAFRAME'],
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.9',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)