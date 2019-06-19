import unittest
from click.testing import CliRunner
from .commands import view, list

class TestCommands(unittest.TestCase):
    runner = CliRunner()

    def test_view_article(self):
        
        response = self.runner.invoke(view, ['dragon-rider'])
        assert response.exit_code == 0
        assert "dragon-rider" in response.output
        assert "article" in response.output

    def test_list_articles(self):
        response = self.runner.invoke(list)
        assert response.exit_code == 0
        assert "dragon-rider" in response.output
        assert "articles" in response.output

    def test_article_with_wrong_slug(self):
        response = self.runner.invoke(view, ['dra'])
        assert response.exit_code == 0
        assert "Something went wrong" in response.output

if __name__ == '__main__':
    unittest.main()
