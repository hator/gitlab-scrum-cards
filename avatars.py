import click
import gitlab
from jinja2 import Environment, select_autoescape, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)


def get_milestone_assignees_avatars(project_id, milestone, token, gitlab_url):
    gl = gitlab.Gitlab(gitlab_url, private_token=token)
    project = gl.projects.get(project_id)
    issues = project.issues.list(scope="all", milestone=milestone, with_labels_details=True, all=True)
    avatars = list(set([i.assignee['avatar_url'] for i in issues if i.assignee]))
    return avatars


def render_avatars(avatars):
    template = env.get_template('avatars_template.html')
    print(template.render(avatars=avatars))


@click.command()
@click.argument('milestone', type=click.STRING)
@click.option('--token', '-t', required=True, help='Personal Access Token for Gitlab (requires API scope)')
@click.option('--url', '-u', 'gitlab_url', required=True, help='URL of gitlab instance')
@click.option('--project', '-p', 'project_id', required=True, help='Path to gitlab project')
def generate_avatars_cmd(milestone, token, gitlab_url, project_id):
    avatars = get_milestone_assignees_avatars(project_id, milestone, token, gitlab_url)

    render_avatars(avatars)


if __name__ == "__main__":
    generate_avatars_cmd()
