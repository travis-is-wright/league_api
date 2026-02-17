import requests

class League:
    def __init__(self, champion):
        self.champion = champion
        self.url = f"https://ddragon.leagueoflegends.com/cdn/16.3.1/data/en_US/champion/{self.champion}.json"

    def retrieve_champion_data(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error occured: ", e)

# {
#     "type": "champion",
#     "format": "standAloneComplex",
#     "version": "16.3.1",
#     "data": {
#         "Kindred": {
#             "id": "Kindred",
#             "key": "203",
#             "name": "Kindred",
#             "title": "The Eternal Hunters",
    def format_title(self, data):
        return data['data'][self.champion]['title']
    
    def format_lore(self, data):
        return data['data'][self.champion]['lore']
    
    def format_class(self, data):
        class_info = data['data'][self.champion]['tags']
        return (', '.join(class_info).title())
    
    def format_energy_type(self, data):
        return data['data'][self.champion]['partype']
    
    def format_spells(self, data):
        spells_info = data['data'][self.champion]['spells']
        spell_dict = {}
        
        for spell in spells_info:
            spell_dict[spell.get('id')] = [spell.get('name'), spell.get('description')]
        return spell_dict


def main():
    selected_champion = input("Please select a Champion: ").title()
    print(selected_champion)

    summoner = League(selected_champion)
    json_data = summoner.retrieve_champion_data()

    if not json_data:
        return None
    
    print(summoner.format_spells(json_data))


if __name__ == "__main__":
    main()