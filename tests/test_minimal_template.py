
def test_bake_project(cookies):
    result = cookies.bake(extra_context={'project_slug': 'simple'})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'simple'
    assert result.project.isdir()


def test_bake_project_with_tox_ini(cookies):
    result = cookies.bake(extra_context={'project_slug': 'simplewithtox','generate_tox_file': 'True' })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'simplewithtox'
    assert result.project.join('tox.ini').isfile()
    assert result.project.isdir()
