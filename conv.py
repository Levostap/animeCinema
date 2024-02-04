class CSVConverter:
    def __init__(self):
        self.data = {}

    def load_csv(self, filename):
        i = 0
        with open(filename, 'r', encoding="cp1251") as file:
            line = file.readline()
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                keyys_json = [x for x in row.keys()]
                break
            for row in reader:
                b = {keyys_json[0]: row[keyys_json[0]], "uName": "Тест студии"}
                c = dict()
                for j in range(1, len(keyys_json)):
                    c[keyys_json[j]] = row[keyys_json[j]]
                b["data"] = c
                self.data[i] = b
                i += 1

    def get_json_data(self):
        return json.dumps(self.data)
