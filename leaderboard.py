class LeaderBoard:
    @staticmethod
    def change_format(time):
        t_dict = {
            "hour" : 3600,
            "minute" : 60,
            "second" : 1
        }
        result = {}
        temp_time = int(time)
        for unit, value in t_dict.items():
            result[unit], temp_time = temp_time // value, temp_time - (temp_time // value) * t_dict[unit]
        res = []
        for key, value in result.items():
            if value != 0:
                res.append(f"{value}{key}")
        return " ".join(res)
    @staticmethod
    def show():
        try:
            with open("leaderboard.txt", "r") as file:
                print("\nLeaderboard:")
                for line in file:
                    name, score, duration = line.strip().split("|")
                    print(f"{name}'s score is {score}/5 during this time - {LeaderBoard.change_format(duration)}")

        except Exception as e:
            print(e)
            print("There is an error with opening the file.")
