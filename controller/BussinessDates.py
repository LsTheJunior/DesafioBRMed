import datetime

class Dates:
    def getBussinesDates(self):
        tem_today = datetime.datetime.today().strftime('%Y-%m-%d')

        datesList= []
        i = 0
        while i < 5:

            today = datetime.datetime(int(tem_today[:4]),int(tem_today[5:7]), int(tem_today[8:11]))
            offset = max(1, (today.weekday() + 6) % 7 - 3)

            timedelta = datetime.timedelta(offset)

            most_recent = today - timedelta
            most_recent = most_recent.strftime('%Y-%m-%d')
            tem_today = most_recent
            datesList.append(tem_today)
            i+=1
        return datesList    

        