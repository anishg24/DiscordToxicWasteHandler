from keras.models import load_model
import numpy as np
import pickle
import discord
from dotenv import load_dotenv
import os
from keras_preprocessing.sequence import pad_sequences
load_dotenv()

client = discord.Client()

rating_index = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
max_input_length = 1403
model = load_model("model/model.h5")
with open("model/tokenizer.pkl", "rb") as t:
    tokenizer = pickle.load(t)


def process_message_for_data(sentence):
    tokens = []
    for word in sentence.lower().split():
        try:
            tokens.append(tokenizer.word_index[word])
        except KeyError:
            tokens.append(0)
    transformed_sentence = pad_sequences([tokens], maxlen=max_input_length, padding="post")
    prediction = model.predict(transformed_sentence)[0]
    return np.argmax(prediction), np.amax(prediction)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    index, val = process_message_for_data(message.content)
    rating = rating_index[index]
    if val > 0.5:
        try:
            await message.delete()
        except:
            print("ERROR DELETING!")
            return
        await message.channel.send(f"Hey! Toxic Waste Handler here! {message.author} said something really toxic, so I deleted it!")
    return

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
