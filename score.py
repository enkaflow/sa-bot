import requests
import csv


class Score:
    def __init__(
        self, songid, songname, difficulty, chart, rivalcode, score, combotype
    ):
        self.songid = songid
        self.difficulty = difficulty
        self.chart = chart
        self.songname = songname
        self.rivalcode = rivalcode
        self.score = score
        self.combotype = combotype

    def hasEmpty(self):
        """ returns true if one or more of the fields is empty """
        return (
            not self.songid
            or not self.difficulty
            or not self.chart
            or not self.songname
            or not self.rivalcode
            or not self.score
            or not self.combotype
        )

    def __str__(self):
        return f"{self.songname} | {self.difficulty} | {self.score}"

    def __repr__(self):
        return f"{self.rivalcode} | {self.songid} | {self.difficulty} | {self.songname} | {self.chart} | {self.score}"


def query_scorepage(rivalcode, difficulty):
    """returns a list of Scores """
    url = f"http://skillattack.com/sa4/dancer_score.php?_=rival&ddrcode={rivalcode}&style=0&difficulty={difficulty}"
    r = requests.get(url)
    r.encoding = 'shift_jis'
    parser = SAParser(r.text)
    songids = parser.get_songids()
    songnames = parser.get_songnames()
    charts = parser.get_charts()
    scores = parser.get_scores()
    combos = parser.get_combotype()

    full_data = zip(songids, songnames, charts, scores, combos)
    return list(
        map(
            lambda x: Score(x[0], x[1], difficulty, x[2], rivalcode, x[3], x[4]),
            full_data,
        )
    )


def scorelist_to_dict(scorelist):
    """ in: list<Score>. Out: Map<songid: Score> """
    out = {}
    for i in scorelist:
        out[i.songid] = i
    return out


class SAParser:
    def __init__(self, text):
        self.text = text

    def get_songids(self):
        anchor = self.text.index("ddIndex   =new")
        line = self.text[anchor : self.text.find("\n", anchor)]
        # Expect line = 'ddIndex   =new Array(587,838,....);'
        data = line[line.find("(") + 1 : line.find(")")]
        return data.split(",")

    def get_songnames(self):
        anchor = self.text.index("dsMusic   =new Array")
        line = self.text[anchor : self.text.find("\n", anchor)]
        data = line[line.find("(") + 1 : line.find(");")]
        return next(csv.reader([data], quotechar="'"))

    def get_charts(self):
        anchor = self.text.index("ddSequence=new")
        line = self.text[anchor : self.text.find("\n", anchor)]
        data = line[line.find("(") + 1 : line.find(")")]
        return data.split(",")

    def get_scores(self):
        """ scores have commas inside. use csv """
        anchor = self.text.index("ddsScore[0]=new")
        line = self.text[anchor : self.text.find("\n", anchor)]
        data = line[line.find("(") + 1 : line.find(")")]
        return next(csv.reader([data], quotechar="'"))

    def get_combotype(self):
        anchor = self.text.index("dddFc[0]   =new")
        line = self.text[anchor : self.text.find("\n", anchor)]
        data = line[line.find("(") + 1 : line.find(")")]
        return data.split(",")

    def debug(self):
        print(f"{len(self.get_songids())} song ids")
        print(f"{len(self.get_songnames())} songnames")
        print(f"{len(self.get_charts())} charts")
        print(f"{len(self.get_scores())} scores")
        print(f"{len(self.get_combotype())} combotypes")
