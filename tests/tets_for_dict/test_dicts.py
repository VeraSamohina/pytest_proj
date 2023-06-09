import pytest

from utils.dicts import get_val


def test_get_val():
    assert get_val({'project': 'bazaar', 'project1': 'mercurial', 'project2': 'SVN'}, 'project') == 'bazaar'
    assert get_val({'project': 'bazaar'}, 'project2') == 'git'
    assert get_val({}, 'vcs') == 'git'

