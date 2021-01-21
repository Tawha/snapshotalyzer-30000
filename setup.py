from setuptools import setup

setup(
	name="snapshotalyzer-30000",
	version="0.1",
	author="Syed Muhammad Tawha",
	description="Snapshotalyzer is a tool to manage snapshots",
	license="GPLv3+",
	packages=['shotty'],
	url="https://github.com/Tawha/snapshotalyzer-30000",
	install_requires=[
		'click',
		'boto3'
	],
	entry_points='''
		[console_scripts]
		shotty=shotty.shotty:cli
	''',
)
