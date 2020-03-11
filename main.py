import score
import discord
from pprint import pprint

codes = {
    "51527333": "KDUBS",
    #'51545388', #jay
    "51527130": "MARK",
    "61578951": "YOSHI",
    "51546306": "TSWIFT",
    "61573431": "MELODY"
}


def main():
    diff = '17'
    songid = "487"  # skeet
    scores_to_post = []

    for id, name in codes.items():
        print(f"Getting data for user {id}")
        scores = score.scorelist_to_dict(score.query_scorepage(id, diff))
        scores_to_post.append(f"{name:8} | {str(scores[songid])}")

    bot = discord.PostBot()
    bot.basic_post("\n".join(scores_to_post))


if __name__ == "__main__":
    main()
