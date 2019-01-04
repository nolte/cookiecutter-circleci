Cookiecutter Template for circleci BuildJobs
=====================================================================

|Travis CI build status| |CircleCI build status| |Documentation Status| |Github Project Stars| |Github Issue Tracking| |Github Latest Release|

`Cookiecutter Template <https://cookiecutter.readthedocs.io>`_ for a `CircleCI <https://circleci.com/>`_, `Continuous integration <https://en.wikipedia.org/wiki/Continuous_integration>`_/`Continuous delivery <https://en.wikipedia.org/wiki/Continuous_delivery>`_ Pipeline, for different types of projects.

Features
---------------------------------------------------------------------

* Handle `Semantic Versioning <https://semver.org/>`_ of the project. (*planed*)
* Create a `Github Releases <https://help.github.com/articles/creating-releases/>`_. (*planed*)
* Push generated `sphinx <http://www.sphinx-doc.org/en/master/>`_ page to `GithubPage <https://pages.github.com/>`_. (*planed*)
* Create GitHub Based Cangelog with `ferrarimarco/docker-github-changelog-generator <https://github.com/ferrarimarco/docker-github-changelog-generator>`_. (*planed*)


Usage
--------------------------------------------------------------------

Install `cookiecutter <https://pypi.org/project/cookiecutter/>`_ to your local machine.

.. danger::

   Be carefull when the config are generated to a existing project. Existing files will be overwrite.



Creating the `.circleci/config.yml <https://circleci.com/docs/2.0/configuration-reference/#section=configuration>`_ Job Configuration.



.. |Travis CI build status| image:: https://travis-ci.org/nolte/cookiecutter-circleci.svg?branch=develop
    :target: https://travis-ci.org/nolte/cookiecutter-circleci
.. |CircleCI build status| image:: https://circleci.com/gh/nolte/cookiecutter-circleci.svg?style=svg
    :target: https://circleci.com/gh/nolte/cookiecutter-circleci
.. |Documentation Status| image:: https://readthedocs.org/projects/cookiecutter-circleci/badge/?version=latest
    :target: https://cookiecutter-circleci.readthedocs.io/en/stable/?badge=stable
.. |Github Project Stars| image:: https://img.shields.io/github/stars/nolte/cookiecutter-circleci.svg?label=Stars&style=social
    :target: https://github.com/nolte/cookiecutter-circleci
.. |Github Issue Tracking| image:: https://img.shields.io/github/issues-raw/nolte/cookiecutter-circleci.svg
    :target: https://github.com/nolte/cookiecutter-circleci
.. |Github Latest Release| image:: https://img.shields.io/github/release/nolte/cookiecutter-circleci.svg
    :target: https://github.com/nolte/cookiecutter-circleci
