from setuptools import setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'octobot_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    	(os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
    	(os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    	(os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
        (os.path.join('share', package_name, 'params'), glob('params/*.yaml')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='deivideich',
    maintainer_email='deivideich@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
