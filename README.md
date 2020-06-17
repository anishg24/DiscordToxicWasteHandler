# Discord's Toxic Waste Handler
This project is made by Anish Govind. Other projects can be found at my [GitHub][github].
Huge thank you to the contributors of this [dataset][dataset] because it fuels the custom model
that this bot runs on.

![GitHub followers](https://img.shields.io/github/followers/anishg24?label=Follow&style=social)

## Project Description
This is a bot for [Discord](https://www.discord.com). It is designed to handle [toxic](https://www.urbandictionary.com/define.php?term=Toxic) 
messages sent by users. In this current release, it is not configurable, 
and solely made to delete any messages deemed toxic by the bot. 
This will be fixed in future releases.

## The Why behind this Project
I am a moderator of a video game's discord server. Moderating this server is not always easy
and the moderation team doesn't go 2 days without someone being really toxic. When I found this
[dataset][dataset] some gears started turning in my head and I decided to work on it. In this
repo you will find the notebook that I used (on Kaggle's servers) to train my own custom
toxicity detector model. My hopes are that this bot can be used wisely in servers to limit and
control some users of Discord who wish to make the servers toxic and not fun.

### Methods Used
* Inferential Statistics
* Deep Learning

### Technologies Involved
* Python 3
* Numpy
* Keras & Tensorflow
* discord.py
* Jupyter (for model creation in Kaggle instances)
    * Pandas

## Getting Started
1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Head to the releases to download the `model.h5` file and place it in `model/` (where `tokenizer.pkl` is located).
3. Setup a virtual environment, or use your default environment.
4. `pip install -r requirements.txt`
5. Follow these [instructions](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro) for creating
your own discord bot and invite it to your sever. Be sure to get the token!.
6. Create a `.env` file with the contents below:
    ```.env
    TOKEN=YOURTOKENHERE
    ```
7. `python main.py`

Your bot should come online and delete any toxic messages it finds.

### Features/To-Do:
-[x] Detects toxic messages
-[x] Deletes toxic messages
-[x] Notifies when deleting a toxic message
-[ ] Configurable
-[ ] Punishments based on what the comment is classified as (according to the model)
    * Possible options: `["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]`
    * These are supported by the model, and can be configured to dish out punishment in a future release
-[ ] Muting Users
-[ ] Kick/Ban Users based on conditions
-[ ] Logging

## Releases
- 1.0.0 (6/17/2020): First working release.

## Contributors
Creator: [Anish Govind][github]

Ways to contact:
* [E-Mail](anishg24@gmail.com)

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**


[github]: https://github.com/anishg24
[dataset]: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data