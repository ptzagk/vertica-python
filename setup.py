# Copyright (c) 2013-2017 Uber Technologies, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
import collections
from setuptools import setup, find_packages


ReqOpts = collections.namedtuple('ReqOpts', ['skip_requirements_regex', 'default_vcs'])

opts = ReqOpts(None, 'git')

# version should use the format 'x.x.x' (instead of 'vx.x.x')
setup(
    name='vertica-python',
    version='0.7.3',
    description='A native Python client for the Vertica database.',
    author='Justin Berka, Alex Kim',
    author_email='justin.berka@gmail.com, alex.kim@uber.com',
    url='https://github.com/uber/vertica-python/',
    keywords="database vertica",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        'python-dateutil>=1.5',
        'pytz',
        'future',
        'six>=1.10.0'
    ],
    extras_require={'namedparams': ['psycopg2>=2.5.1']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Operating System :: OS Independent"
    ]
)
