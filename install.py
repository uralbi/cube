import PyInstaller.__main__
PyInstaller.__main__.run([
    'cube.py',
    '-w',
    '-i',
    'cube.icns',
    '-n',
    'Cube',
    '--add-data',
    'cube.ui:.',
    '--add-data',
    'src/*.qss:src',
])