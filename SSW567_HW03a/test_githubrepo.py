"""
Author:Jinfeng Lan
Time:2026/2/16 05:02
Class:SSW 567
Project name:HW 03a
"""
from github_test import get_github_repo
from unittest.mock import patch, Mock
@patch('github_test.requests.get')
def test_github_repo(mock_get):
    def test_method(url):
        mock_resp = Mock()

        #for repo
        if url.endswith('/repos'):
            mock_resp.status_code = 200
            mock_resp.json.return_value = [{'name':'Helloworld'},{'name':'HelloSSW567'}]
            return mock_resp

        #for commit
        elif url.endswith('/commits'):
            mock_resp.status_code = 200
            mock_resp.json.return_value = [{},{},{}]
            return mock_resp

        else:
            return None
    mock_get.side_effect = test_method
    results = get_github_repo('Blue4u0610')
    expected = 2
    assert len(results) == expected
    assert "Number of commits: 3" in results[0]
    assert "Number of commits: 3" in results[1]