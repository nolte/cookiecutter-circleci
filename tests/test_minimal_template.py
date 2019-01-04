import filecmp

def test_bake_project(cookies):
    result = cookies.bake(extra_context={'project_slug': 'simple'})
    verfiy_base_project_attributes(result,'simple')



def test_bake_project_with_tox_ini(cookies):
    result = cookies.bake(extra_context={'project_slug': 'simplewithtox','generate_tox_file': 'y' })
    verfiy_base_project_attributes(result,'simplewithtox')
    tox_file = result.project.join('tox.ini')
    assert filecmp.cmp(str(tox_file), 'tests/golden_files/minimal/tox.ini',shallow=0)
    assert result.project.join('docsRequirements.txt').check(exists=0)


def test_bake_project_with_tox_ini_and_sphinx(cookies):
    result = cookies.bake(extra_context={'project_slug': 'simplewithtox','generate_tox_file': 'y','generate_sphinx_doc': 'y' })
    verfiy_base_project_attributes(result,'simplewithtox')
    tox_file = result.project.join('tox.ini')
    print(open(str(tox_file)).read())
    assert filecmp.cmp(str(tox_file), 'tests/golden_files/sphinx/tox.ini',shallow=0)
    assert tox_file.isfile()
    assert result.project.join('docsRequirements.txt').check(exists=1)

def verfiy_base_project_attributes(result,expectedProjectName):
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == expectedProjectName
    assert result.project.isdir()
