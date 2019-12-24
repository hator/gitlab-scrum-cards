# Gitlab Scrum Cards

Print scrum cards from Gitlab Issues

## Installation
Install all dependencies from requirements.txt. Preferably use virtual env.

`pip install -f requirements.txt`

## Usage
```
$ python main.py
    --token <GITLAB_TOKEN>
    --url <GITLAB_URL>
    --project <PATH/TO/PROJECT>
    "<MILESTONE>"
        > scrum_cards.html
```

For example:
```
$ python main.py --token Aabc1234 --url my-gitlab.my-domain.com --project mygroup/myproject "Sprint 2" > sprint2.html
```

## Avatars
Print avatars of people assigned to tasks in given milestone.

### Usage
`$ python avatars.py -t <TOKEN> -u <GITLAB_URL> -p <PROJECT> "<MILESTONE>" > avatars.html`
