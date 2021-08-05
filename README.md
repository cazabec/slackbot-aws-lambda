# slackbot-aws-lambda

![Bot architecture](architecture/slackbot.png)

## Inspiration

This project is in production on the [techcareergrowth.slack.com](https://techcareergrowth.slack.com) slack workspace (2.6K users)
The goal of this project was to do a bot that would reply automatically with tips when someone posts his resume in the #resume-sharing-and-reviews channel.

## Medium article
The documentation for the code in this repository is in my [medium article](https://medium.com/@colin.cazabet/create-and-distribute-a-slack-bot-with-python-and-aws-in-1-hour-41c4a6c0f99d)

## Lambdas

| File                     	| Description                                                     	|
|--------------------------	|-----------------------------------------------------------------	|
| [lambda/oauth2.py](https://github.com/cazabec/slackbot-aws-lambda/blob/main/lambda/oauth2.py)         	| Called by slack when someone clicks on your public install link 	|
| [lambda/slash_command.py](https://github.com/cazabec/slackbot-aws-lambda/blob/main/lambda/slash_command.py)  	| Called by slack when a slash command is entered                 	|
| [lambda/event_receiver.py](https://github.com/cazabec/slackbot-aws-lambda/blob/main/lambda/event_receiver.py) 	| Called by slack when there is an event in the workspace         	|
