import score
import discord
from pprint import pprint

codes = [
    "51527333",  # me
    #'51545388', #jay
    "51527130",  # mark
    "61578951",  # yoshi
    "51546306",  # tswift
    "61573431",  # melody
]


def main():
    songid = "576"  # deadball
    scores_to_post = []

    for id in codes:
        print(f"Getting data for user {id}")
        scores = score.scorelist_to_dict(score.query_scorepage(id, "13"))
        scores_to_post.append(str(scores[songid]))

    bot = discord.PostBot()
    bot.basic_post("\n".join(scores_to_post))


if __name__ == "__main__":
    main()
