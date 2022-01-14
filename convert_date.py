from Google import convert_to_RFC_datetime
class Text_convert:
    def convert_to_date(self,text):
        month_dict = {'ม.ค. ':1,
                        'ก.พ. ':2,
                        'มี.ค. ':3,
                        'เม.ย. ':4,
                        'พ.ค. ':5,
                        'มิ.ย. ':6,
                        'ก.ค. ':7,
                        'ส.ค. ':8,
                        'ก.ย. ':9,
                        'ต.ค. ':10,
                        'พ.ย. ':11,
                        'ธ.ค. ':12,
                        ' ม.ค.':1,
                        ' ก.พ.':2,
                        ' มี.ค.':3,
                        ' เม.ย.':4,
                        ' พ.ค.':5,
                        ' มิ.ย.':6,
                        ' ก.ค.':7,
                        ' ส.ค.':8,
                        ' ก.ย.':9,
                        ' ต.ค.':10,
                        ' พ.ย.':11,
                        ' ธ.ค.':12}
        try:
            day = int(text[9:11])
        except ValueError:
            day = int(text[9])
        month = month_dict[text[11:16]]
        year = int(text[-11:-9])+2500-543
        hour = int(text[-8:-6])
        minute = int(text[-5:-3])
        return convert_to_RFC_datetime(year, month, day, hour, minute)

tc = Text_convert()
