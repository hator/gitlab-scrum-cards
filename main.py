import click
import gitlab
from jinja2 import Environment, select_autoescape, FileSystemLoader

IGNORED_LABELS = ["Doing", "Review", "To Do"]

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)


def get_gitlab_issues(project_id, milestone, token, gitlab_url):
    gl = gitlab.Gitlab(gitlab_url, private_token=token)
    project = gl.projects.get(project_id)
    issues = project.issues.list(scope="all", milestone=milestone, with_labels_details=True, all=True)
    return issues


def render_issues(issues):
    template = env.get_template('cards_template.html')
    print(template.render(issues=issues, ignored_labels=IGNORED_LABELS))


@click.command()
@click.argument('milestone', type=click.STRING)
@click.option('--token', '-t', required=True, help='Personal Access Token for Gitlab (requires API scope)')
@click.option('--url', '-u', 'gitlab_url', required=True, help='URL of gitlab instance')
@click.option('--project', '-p', 'project_id', required=True, help='Path to gitlab project')
def generate_issues_cards(milestone, token, gitlab_url, project_id):
    issues = get_gitlab_issues(project_id, milestone, token, gitlab_url)

    render_issues(issues)


if __name__ == '__main__':
    generate_issues_cards()
