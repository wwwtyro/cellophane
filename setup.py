from distutils.core import setup
setup (
    name='cellophane',
    version='0.1',
    description='A dead simple web terminal that gets all of the boilerplate out of the way and lets you do 100% of your work on the server side and in python.',
    author='Rye Terrell',
    author_email='ryeterrell@ryeterrell.net',
    url='',
    packages=['cellophane'],
    package_dir={'cellophane': 'cellophane'},
    package_data={'cellophane': ['license.txt',
                                 'cellophane.html', 
                                 'static/*']},
    data_files=[('.', ['license.txt', 'README']),
                ('examples', ['examples/authentication.py', 'examples/echo.py', 'examples/simple-chat.py'])]
)

